#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      run_program.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               cond_mail       => v3.2.0 or higher
#               lib/gen_libs    => v2.2.0 or higher
#
###############################################################################

"""Program:  run_program.py

    Description:  Unit testing of run_program in cond_mail.py.

    Usage:
        test/unit/cond_mail/run_program.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import cond_mail
import lib.gen_libs as gen_libs
import version

# Version Information
__version__ = version.__version__


class Mail(object):

    """Class:  Mail

    Description:  Class representation of the gen_class.Mail class.

    Super-Class:  object

    Sub-Classes:  None

    Methods:
        __init__ -> Initialize configuration environment.
        read_stdin -> Mock of reading from standard in.
        send_mail -> Mock of sending an email.

    """

    def __init__(self, to_line, subj, frm_line=None):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:
            to_line -> To line on email.
            sub -> Subject line on email.
            frm_line -> From line on email.

        """

        self.to_line = to_line
        self.subj = subj
        self.frm_line = frm_line
        self.msg = "String"

    def read_stdin(self):

        """Method:  read_stdin

        Description:  Mock of reading from standard in.

        Arguments:
            None

        """

        return True

    def send_mail(self):

        """Method:  send_mail

        Description:  Mock of sending an email.

        Arguments:
            None

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_empty_str_mail_msg -> Test if mail message is an empty string.
        test_mail_msg -> Test mail message.
        test_empty_mail_msg -> Test if mail message is empty.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args_array = {"-t": "To line", "-s": "Subject Line"}

    @mock.patch("cond_mail.gen_class.Mail")
    def test_empty_str_mail_msg(self, mock_mail):

        """Function:  test_empty_str_mail_msg

        Description:  Test if mail message is an empty string.

        Arguments:
            mock_mail -> Mock Ref:  cond_mail.gen_class.Mail

        """

        mock_mail.return_value = Mail(self.args_array["-t"],
                                      self.args_array["-s"])

        mock_mail.return_value.msg = ""

        self.assertFalse(cond_mail.run_program(self.args_array))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_mail_msg(self, mock_mail):

        """Function:  test_mail_msg

        Description:  Test mail message.

        Arguments:
            mock_mail -> Mock Ref:  cond_mail.gen_class.Mail

        """

        mock_mail.return_value = Mail(self.args_array["-t"],
                                      self.args_array["-s"])

        self.assertFalse(cond_mail.run_program(self.args_array))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_empty_mail_msg(self, mock_mail):

        """Function:  test_empty_mail_msg

        Description:  Test if mail message is empty.

        Arguments:
            mock_mail -> Mock Ref:  cond_mail.gen_class.Mail

        """

        mock_mail.return_value = Mail(self.args_array["-t"],
                                      self.args_array["-s"])

        mock_mail.return_value.msg = None

        self.assertFalse(cond_mail.run_program(self.args_array))


if __name__ == "__main__":
    unittest.main()
