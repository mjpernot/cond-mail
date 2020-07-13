#!/usr/bin/python
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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_run_program -> Test with run_program.
        test_file_chk_false -> Test with arg_file_chk returns False.
        test_file_chk_true -> Test with arg_file_chk returns True.
        test_require_false -> Test with arg_require returns False.
        test_require_true -> Test with arg_require returns True.
        test_help_false ->  Test with help_func returns False.
        test_help_true -> Test with help_func returns True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = {"-s": "Subject line", "-t": "To Line Address"}

    @mock.patch("cond_mail.run_program", mock.Mock(return_value=True))
    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.arg_parser")
    def test_run_program(self, mock_arg):

        """Function:  test_run_program

        Description:  Test with run_program.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_arg.arg_require.return_value = False
        mock_arg.arg_file_chk.return_value = False

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.run_program", mock.Mock(return_value=True))
    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.arg_parser")
    def test_file_chk_false(self, mock_arg):

        """Function:  test_file_chk_false

        Description:  Test with arg_file_chk returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_arg.arg_require.return_value = False
        mock_arg.arg_file_chk.return_value = False

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.arg_parser")
    def test_file_chk_true(self, mock_arg):

        """Function:  test_file_chk_true

        Description:  Test with arg_file_chk returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_arg.arg_require.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.arg_parser")
    def test_require_false(self, mock_arg):

        """Function:  test_require_false

        Description:  Test with arg_require returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_arg.arg_require.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.arg_parser")
    def test_require_true(self, mock_arg):

        """Function:  test_require_true

        Description:  Test with arg_require returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_arg.arg_require.return_value = True

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=False))
    @mock.patch("cond_mail.arg_parser")
    def test_help_false(self, mock_arg):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_arg.arg_require.return_value = True

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func", mock.Mock(return_value=True))
    @mock.patch("cond_mail.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args

        self.assertFalse(cond_mail.main())


if __name__ == "__main__":
    unittest.main()
