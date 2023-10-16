# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in cond_mail.py.

    Usage:
        test/unit/cond_mail/main.py

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
        arg_add_def
        arg_cond_req
        arg_dir_chk
        arg_file_chk
        arg_require
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()
        self.opt_val = None
        self.multi_val = None
        self.do_parse = None
        self.file_perm_chk = None
        self.arg_file_chk2 = True
        self.opt_req = None
        self.opt_req2 = True

    def arg_file_chk(self, file_perm_chk):

        """Method:  arg_file_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_file_chk.

        Arguments:

        """

        self.file_perm_chk = file_perm_chk

        return self.arg_file_chk2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_help_true
        test_help_false
        test_require_false
        test_require_true
        test_arg_file_false
        test_arg_file_true
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args.args_array = {"-s": "Subject line", "-t": "To Line Address"}

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=True))
    @mock.patch("cond_mail.gen_class.ArgParser")
    def test_help_true(self, mock_arg):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.gen_class.ArgParser")
    def test_help_false(self, mock_arg):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.gen_class.ArgParser")
    def test_require_false(self, mock_arg):

        """Function:  test_require_false

        Description:  Test with arg_require returns False.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.gen_class.ArgParser")
    def test_require_true(self, mock_arg):

        """Function:  test_require_true

        Description:  Test with arg_require returns True.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.gen_class.ArgParser")
    def test_arg_file_false(self, mock_arg):

        """Function:  test_arg_file_false

        Description:  Test with arg_file_chk returns False.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.run_program", mock.Mock(return_value=True))
    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.gen_class.ArgParser")
    def test_arg_file_true(self, mock_arg):

        """Function:  test_arg_file_true

        Description:  Test with arg_file_chk returns True.

        Arguments:

        """

        mock_arg.return_value = self.args

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.run_program", mock.Mock(return_value=True))
    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.gen_class.ArgParser")
    def test_run_program(self, mock_arg):

        """Function:  test_run_program

        Description:  Test with run_program.

        Arguments:

        """

        mock_arg.return_value = self.args

        self.assertFalse(cond_mail.main())


if __name__ == "__main__":
    unittest.main()
