#!/bin/bash
# Unit testing program for the modules in the program.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:"
test/unit/cond-mail/help_message.py
test/unit/cond-mail/run_program.py
test/unit/cond-mail/main.py

