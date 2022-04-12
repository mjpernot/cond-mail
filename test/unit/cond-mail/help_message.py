#!/usr/bin/python
# Classification (U)

"""Program:  help_message.py

    Description:  Unit testing of help_message in cond_mail.py.

    Usage:
        test/unit/cond_mail/help_message.py

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

# Local
sys.path.append(os.getcwd())
import cond_mail
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_help_message

    """

    def test_help_message(self):

        """Function:  test_help_message

        Description:  Test help_message function.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(cond_mail.help_message())


if __name__ == "__main__":
    unittest.main()
