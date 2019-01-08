#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      main.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               cond_mail       => v2.1.0 or higher
#               lib/gen_libs    => v2.5.0 or higher
#
###############################################################################

"""Program:  main.py

    Description:  Unit testing of main in cond_mail.py.

    Usage:
        test/unit/cond_mail/main.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_require_false -> Test with arg_require returns False.
        test_require_true -> Test with arg_require returns True.
        test_help_false ->  Test with help_func returns False.
        test_help_true -> Test with help_func returns True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args = {"-s": "Subject line", "-t": "To Line Address"}

    @mock.patch("cond_mail.run_program")
    @mock.patch("cond_mail.gen_libs.help_func")
    @mock.patch("cond_mail.arg_parser")
    def test_require_false(self, mock_arg, mock_help, mock_run):

        """Function:  test_require_false

        Description:  Test with arg_require returns False.

        Arguments:
            mock_arg -> Mock Ref:  cond_mail.arg_parser
            mock_help -> Mock Ref:  cond_mail.gen_libs.help_func
            mock_run -> Mock Ref:  cond_mail.run_program

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_run.return_value = True

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func")
    @mock.patch("cond_mail.arg_parser")
    def test_require_true(self, mock_arg, mock_help):

        """Function:  test_require_true

        Description:  Test with arg_require returns True.

        Arguments:
            mock_arg -> Mock Ref:  cond_mail.arg_parser
            mock_help -> Mock Ref:  cond_mail.gen_libs.help_func

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func")
    @mock.patch("cond_mail.arg_parser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:
            mock_arg -> Mock Ref:  cond_mail.arg_parser
            mock_help -> Mock Ref:  cond_mail.gen_libs.help_func

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(cond_mail.main())

    @mock.patch("cond_mail.gen_libs.help_func")
    @mock.patch("cond_mail.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:
            mock_arg -> Mock Ref:  cond_mail.arg_parser.arg_parse2
            mock_help -> Mock Ref:  cond_mail.gen_libs.help_func

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(cond_mail.main())


if __name__ == "__main__":
    unittest.main()
