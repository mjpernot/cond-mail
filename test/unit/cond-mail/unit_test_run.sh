#!/bin/bash
# Unit testing program for the cond_mail.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  help_message"
test/unit/cond-mail/help_message.py

echo ""
echo "Unit test:  run_program"
test/unit/cond-mail/run_program.py

echo ""
echo "Unit test:  main"
test/unit/cond-mail/main.py

