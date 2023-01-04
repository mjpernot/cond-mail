#!/usr/bin/python
# Classification (U)

"""Program:     cond_mail.py

    Description:  Receives text input and pushes it into sendmail.  Will only
        send an email if there is data in the text input.

    Usage:

        Pipe usage:
            Text Input | cond_mail.py -s subject
                -t to_email1 [to_email2 ...] [-f from_email] [-u]

        Redirect in usage:
            cond_mail.py -s subject -t to_email1 [to_email2 ...] [-u]
                [-f from_email] < text_file

        File option usage:
            cond_mail.py -s subject -t to_email1 [to_email2 ...] [-u]
                [-f from_email] [-i [path] filename]

    Arguments:
        -s subject line -> Subject line.  Required argument.
        -t to_email(s) -> To email address(es).  Multiple email addresses are
            space-delimited.  Required argument.
        -f from_email -> From email address.  Format:  user_name@domain_name.
        -i filename -> Path and file name to read into email body.
        -u => Override the default mail command and use mailx.
        -v -> Display version of this program.
        -h -> Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  -i option will override the standard in or pipe syntax.

    Example:
        cat text_file | cond_mail.py -s text -t d123456@coe.ic.gov
        cond_mail.py -s subject line -t d123456@coe.ic.gov < text_file
        cond_mail.py -s subject line -t d123456@coe.ic.gov -i text_file

"""

# Libraries and Global Variables
from __future__ import print_function

# Standard
import sys
import socket
import getpass

# Local
import lib.gen_class as gen_class
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def run_program(args_array):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.

    """

    args_array = dict(args_array)
    mail = gen_class.Mail(
        args_array["-t"], " ".join(args_array["-s"]),
        args_array.get("-f", getpass.getuser() + "@" + socket.gethostname()))

    if args_array.get("-i", False):

        with open(args_array["-i"]) as f_hdlr:
            for line in f_hdlr:
                mail.add_2_msg(line)

    else:
        mail.read_stdin()

    if mail.msg and len(mail.msg.rstrip()) > 0:
        mail.send_mail(use_mailx=args_array.get("-u", False))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    cmdline = gen_libs.get_inst(sys)
    file_chk_list = ["-i"]
    opt_multi_list = ["-t", "-s"]
    opt_req_list = ["-s", "-t"]
    opt_val_list = ["-s", "-t", "-f", "-i"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(
        cmdline.argv, opt_val_list, multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list):
        run_program(args_array)


if __name__ == "__main__":
    sys.exit(main())
