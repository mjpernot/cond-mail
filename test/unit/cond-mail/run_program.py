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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import cond_mail
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = dict()

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Mail(object):

    """Class:  Mail

    Description:  Class representation of the gen_class.Mail class.

    Methods:
        __init__
        read_stdin
        send_mail
        add_2_msg

    """

    def __init__(self, to_line, subj, frm_line=None):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.to_line = to_line
        self.subj = subj
        self.frm_line = frm_line
        self.msg = "String"
        self.line = None

    def read_stdin(self):

        """Method:  read_stdin

        Description:  Mock of reading from standard in.

        Arguments:

        """

        return True

    def send_mail(self, use_mailx=False):

        """Method:  send_mail

        Description:  Mock of sending an email.

        Arguments:

        """

        status = True

        if use_mailx:
            status = True

        return status

    def add_2_msg(self, line):

        """Method:  add_2_msg

        Description:  Mock of adding lines to an email.

        Arguments:

        """

        self.line = line

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mailx
        test_multiline_file
        test_empty_file
        test_input_file
        test_empty_str_mail_msg2
        test_empty_str_mail_msg
        test_mail_msg
        test_empty_mail_msg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toline = "To line"
        self.subject = "Subject Line"
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args5 = ArgParser()
        self.args.args_array = {"-t": self.toline, "-s": self.subject}
        self.args2.args_array = {
            "-t": self.toline, "-s": self.subject,
            "-i": "test/unit/cond-mail/basefiles/infile1.txt"}
        self.args3.args_array = {
            "-t": self.toline, "-s": self.subject,
            "-i": "test/unit/cond-mail/basefiles/infile2.txt"}
        self.args4.args_array = {
            "-t": self.toline, "-s": self.subject,
            "-i": "test/unit/cond-mail/basefiles/infile3.txt"}
        self.args5.args_array = {
            "-t": self.toline, "-s": self.subject, "-u": True}
        self.mail = Mail(self.args.get_val("-t"), self.args.get_val("-s"))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_mailx(self, mock_mail):

        """Function:  test_mailx

        Description:  Test using mailx command.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.assertFalse(cond_mail.run_program(self.args5))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_multiline_file(self, mock_mail):

        """Function:  test_multiline_file

        Description:  Test with -i option with multiple lines.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.assertFalse(cond_mail.run_program(self.args4))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_empty_file(self, mock_mail):

        """Function:  test_empty_file

        Description:  Test with -i option with empty file.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.assertFalse(cond_mail.run_program(self.args3))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_input_file(self, mock_mail):

        """Function:  test_input_file

        Description:  Test with -i option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.assertFalse(cond_mail.run_program(self.args2))

    @mock.patch("cond_mail.gen_class.Mail.read_stdin")
    def test_empty_str_mail_msg2(self, mock_stdin):

        """Function:  test_empty_str_mail_msg

        Description:  Test if mail message is an empty string.

        Arguments:

        """

        mock_stdin.read_stdin.return_value = True

        self.assertFalse(cond_mail.run_program(self.args))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_empty_str_mail_msg(self, mock_mail):

        """Function:  test_empty_str_mail_msg

        Description:  Test if mail message is an empty string.

        Arguments:

        """

        mock_mail.return_value = self.mail
        mock_mail.return_value.msg = ""

        self.assertFalse(cond_mail.run_program(self.args))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_mail_msg(self, mock_mail):

        """Function:  test_mail_msg

        Description:  Test mail message.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.assertFalse(cond_mail.run_program(self.args))

    @mock.patch("cond_mail.gen_class.Mail")
    def test_empty_mail_msg(self, mock_mail):

        """Function:  test_empty_mail_msg

        Description:  Test if mail message is empty.

        Arguments:

        """

        mock_mail.return_value = self.mail
        mock_mail.return_value.msg = None

        self.assertFalse(cond_mail.run_program(self.args))


if __name__ == "__main__":
    unittest.main()
