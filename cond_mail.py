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
from __future__ import absolute_import

# Standard
import sys
import socket
import getpass

# Local
try:
    from .lib import gen_class
    from .lib import gen_libs
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_class as gen_class
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


def run_program(args):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance

    """

    mail = gen_class.Mail(
        args.get_val("-t"), args.get_val("-s"),
        args.get_val(
            "-f", def_val=getpass.getuser() + "@" + socket.gethostname()))

    if args.arg_exist("-i"):
        with open(args.get_val("-i")) as f_hdlr:
            for line in f_hdlr:
                mail.add_2_msg(line)

    else:
        mail.read_stdin()

    if mail.msg and len(mail.msg.rstrip()) > 0:
        mail.send_mail(use_mailx=args.arg_exist("-u"))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        file_perm_chk -> file check options with their perms in octal
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains the options that are required for the program
        opt_val_list -> contains options which require values

    Arguments:
        (input) argv -> Arguments from the command line

    """

    file_perm_chk = {"-i": 4}
    opt_multi_list = ["-t", "-s"]
    opt_req_list = ["-s", "-t"]
    opt_val_list = ["-s", "-t", "-f", "-i"]

    # Process argument list from command line
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, multi_val=opt_multi_list)

    if args.arg_parse2()                                            \
       and not gen_libs.help_func(args, __version__, help_message)  \
       and args.arg_require(opt_req=opt_req_list)                   \
       and args.arg_file_chk(file_perm_chk=file_perm_chk):
        run_program(args)


if __name__ == "__main__":
    sys.exit(main())
