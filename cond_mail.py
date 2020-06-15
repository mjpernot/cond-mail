#!/usr/bin/python
# Classification (U)

"""Program:     cond_mail.py

    Description:  Receives text input and pushes it into sendmail.  Will only
        send if there is data in the text input.

    Usage:
        Text Input | cond_mail.py -s subject -t to_email(s) [-f from_email]
            [-v | -h]
        cond_mail.py -s subject -t to_email(s) [-f from_email] < text_file

    Arguments:
        -s subject line => Subject line.  Required argument.
        -t to_email(s) => To email address(es).  Multiple email addresses are
            space-delimited.  Required argument.
        -f from_email => From email address.  Format:  user_name@domain_name.
        -v => Display version of this program.
        -h => Help and usage message.

    Example:
        cat text_file | cond_mail.py -s text -t d123456@coe.ic.gov
        cond_mail.py -s subject line -t d123456@coe.ic.gov < text_file

"""

# Libraries and Global Variables

# Standard
import sys
import socket
import getpass

# Local
import lib.gen_class as gen_class
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def run_program(args_array, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) **kwargs:
            None

    """

    args_array = dict(args_array)

    mail = gen_class.Mail(
        args_array["-t"], " ".join(args_array["-s"]),
        args_array.get("-f", getpass.getuser() + "@" + socket.gethostname()))

    mail.read_stdin()

    if mail.msg and len(mail.msg.rstrip()) > 0:
        mail.send_mail()


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

    opt_multi_list = ["-t", "-s"]
    opt_req_list = ["-s", "-t"]
    opt_val_list = ["-s", "-t", "-f"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list):
        run_program(args_array)


if __name__ == "__main__":
    sys.exit(main())
