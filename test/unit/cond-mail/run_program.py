#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in cond_mail.py.

    Usage:
        test/unit/cond_mail/run_program.py

    Arguments:

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
import version

__version__ = version.__version__


class Mail(object):

    """Class:  Mail

    Description:  Class representation of the gen_class.Mail class.

    Methods:

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

        """

        return True

    def send_mail(self):

        """Method:  send_mail

        Description:  Mock of sending an email.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_multiline_file -> Test with -i option with multiple lines.
        test_empty_file -> Test with -i option with empty file.
        test_input_file -> Test with -i option.
        test_empty_str_mail_msg2 -> Test if mail message is an empty string.
        test_empty_str_mail_msg -> Test if mail message is an empty string.
        test_mail_msg -> Test mail message.
        test_empty_mail_msg -> Test if mail message is empty.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toline = "To line"
        self.subject = "Subject Line"
        self.args_array = {"-t": self.toline, "-s": self.subject}
        self.args_array2 = {"-t": self.toline, "-s": self.subject,
                            "-i": "test/unit/cond-mail/basefiles/infile1.txt"}
        self.args_array3 = {"-t": self.toline, "-s": self.subject,
                            "-i": "test/unit/cond-mail/basefiles/infile2.txt"}
        self.args_array4 = {"-t": self.toline, "-s": self.subject,
                            "-i": "test/unit/cond-mail/basefiles/infile3.txt"}

    @mock.patch("cond_mail.gen_class.Mail")
    def test_multiline_file(self, mock_send):

        """Function:  test_multiline_file

        Description:  Test with -i option with multiple lines.

        Arguments:

        """

        mock_send.send_mail.return_value = True

        self.assertFalse(cond_mail.run_program(self.args_array4))

    def test_empty_file(self):

        """Function:  test_empty_file

        Description:  Test with -i option with empty file.

        Arguments:

        """

        self.assertFalse(cond_mail.run_program(self.args_array3))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_input_file(self, mock_send):

        """Function:  test_input_file

        Description:  Test with -i option.

        Arguments:

        """

        mock_send.send_mail.return_value = True

        self.assertFalse(cond_mail.run_program(self.args_array2))

    @mock.patch("cond_mail.gen_class.Mail.read_stdin")
    def test_empty_str_mail_msg2(self, mock_stdin):

        """Function:  test_empty_str_mail_msg

        Description:  Test if mail message is an empty string.

        Arguments:

        """

        mock_stdin.read_stdin.return_value = True

        self.assertFalse(cond_mail.run_program(self.args_array))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_empty_str_mail_msg(self, mock_mail):

        """Function:  test_empty_str_mail_msg

        Description:  Test if mail message is an empty string.

        Arguments:

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

        """

        mock_mail.return_value = Mail(self.args_array["-t"],
                                      self.args_array["-s"])

        self.assertFalse(cond_mail.run_program(self.args_array))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_empty_mail_msg(self, mock_mail):

        """Function:  test_empty_mail_msg

        Description:  Test if mail message is empty.

        Arguments:

        """

        mock_mail.return_value = Mail(self.args_array["-t"],
                                      self.args_array["-s"])
        mock_mail.return_value.msg = None

        self.assertFalse(cond_mail.run_program(self.args_array))


if __name__ == "__main__":
    unittest.main()
