# Python project for check for and emailing out data.
# Classification (U)

# Description:
  This program is used to receive text input and pushes it into sendmail.  Will only send if there is data in the text input.  This program is typically used in conjunction with other project programs.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Email data received from standard in.
  * Email data from an ASCII text file.
  * Ensure there is data sent to the program, otherwise ignore request.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/gen_class
    - lib/arg_parser
    - lib/gen_libs


# Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/cond-mail.git
```

Install/upgrade system modules.

```
cd cond-mail
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Program Descriptions:
### Program: cond_mail.py
##### Description: Receives text input and pushes it into sendmail.  Will only send if there is data in the text input.


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/cond-mail/cond_mail.py -h
```


# Help Message:
  Below is the help message for the program the program.  Run the program with the -h option get the latest help message for the program.

    Program:     cond_mail.py

    Description:  Receives text input and pushes it into sendmail.  Will only
        send if there is data in the text input.

    Usage:
        Text Input | cond_mail.py -s subject -t to_email(s) [-f from_email]
            [-v | -h]
        cond_mail.py -s subject -t to_email(s) [-f from_email] < text_file

    Arguments:
        -s subject line => Subject line.  Required argument.
        -t to_email(s) => To email address(es).  Multiple email addresses are
            space-delimited.  Required argument.
        -f from_email => From email address.  Format:  user_name@domain_name.
        -v => Display version of this program.
        -h => Help and usage message.

    Example:
        cat text_file | cond_mail.py -s text -t d123456@coe.ic.gov
        cond_mail.py -s subject line -t d123456@coe.ic.gov < text_file


# Testing:

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the cond_mail.py program.

### Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/cond-mail.git
```

Install/upgrade system modules.

```
cd cond-mail
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for cond_mail.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/cond-mail
```

### Unit:  help_message

```
test/unit/cond_mail/help_message.py
```

### Unit:  

```
test/unit/cond_mail/
```

### Unit:  

```
test/unit/cond_mail/
```

### Unit:  run_program

```
test/unit/cond_mail/run_program.py
```

### Unit:  main

```
test/unit/cond_mail/main.py
```

### All unit testing

```
test/unit/cond_mail/unit_test_run.sh
```

### Code coverage program

```
test/unit/cond_mail/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the cond_mail.py program.

### Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/cond-mail.git
```

Install/upgrade system modules.

```
cd cond-mail
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Integration test runs for cond_mail.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/cond-mail
```

### Integration:  

```
test/integration/cond_mail/
```

### All integration testing

```
test/integration/cond_mail/integration_test_run.sh
```

### Code coverage program

```
test/integration/cond_mail/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the cond_mail.py program.

### Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/cond-mail.git
```

Install/upgrade system modules.

```
cd cond-mail
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Blackbox test run for cond_mail.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/cond-mail
```

### Blackbox:  

```
test/blackbox/cond_mail/blackbox_test.sh
```

