# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [4.0.0] - 2024-12-03
Breaking Changes

- Removed support for Python 2.7.
- Updated python-lib v4.0.0

### Changed
- run_program: Added encoding parameter to open() command.

### Removed
- Removed "from \_\_future\_\_ import" library modules.


## [3.4.5] - 2024-11-15

### Fixed
- Set chardet==3.0.4 for Python 3.

### Deprecated
- Support for Python 2.7


## [3.4.4] - 2024-11-07
- Updated simplejson==3.13.2 for Python 3
- Updated python-lib to v3.0.7


## [3.4.3] - 2024-09-10

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [3.4.2] - 2024-02-26
- Further updated to work in Red Hat 8
- Updated python-lib to v3.0.3

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [3.4.1] - 2024-01-30
- Updated to work in Red Hat 8
- Updated python-lib to v3.0.1

### Changed
- Documentation updates.


## [3.4.0] - 2023-10-16
- Replaced the arg_parser code with gen_class.ArgParser code.
- Upgraded python-lib to v2.10.1

### Changed
- main: Removed gen_libs.get_inst call.
- Documentation updates.


## [3.3.2] - 2022-09-28
- Updated to work in Python 3 too.
- Upgraded python-lib to v2.9.4
- Added \_\_future\_\_ modules for Python 2.


## [3.3.1] - 2021-12-13
- Allow to override the default sendmail (postfix) and use mailx command.

### Fixed
- run_program:  Removed rstrip calls on the input file lines.

### Changed
- run_program:  Determine whether to use sendmail or mailx when using the send_mail method.
- Removed non-required \*\*kwargs from function parameter list.
- Documentation updates.


## [3.3.0] - 2020-06-15
### Added
- Added -i option to allow for reading from a file instead of using standard in or pipes.

### Fixed
- main:  Fixed handling command line arguments from SonarQube scan finding.

### Changed
- run_program:  Added -i option to handle file processing.
- main: Added -i option to handle file and validating the file.
- Documentation updates.


## [3.2.3] - 2019-05-07
### Fixed
- run_program:  Fixed problem with mutable default arguments issue.


## [3.2.2] - 2019-03-01
### Changed
- main:  Refactored code to bring into standard convention.


## [3.2.1] - 2018-11-01
### Changed
- run_program:  Changed Mail instance name from "MAIL" to "mail".
- Documentation updates


## [3.2.0] - 2018-10-02
### Changed
- run_program:  The "From line" in the email will always be set with a default value or user-defined value, changed "-s" option to allow for multiple values in subject line and checked that the Mail message is not an empty string.
- main:  Allow "-s" option to have multiple values.


## [3.1.0] - 2018-08-23
### Added
- Added gen_class module.

### Changed
- main:  Added ability to pass multiple email addresses to the "To Line".
- run_program:  Changed Mail class over to the "gen_class" module.

### Removed
- Removed system module.


## [3.0.0] - 2018-06-04
Breaking Change

### Changed
- Changed "arg_parser" calls to new naming schema.
- Changed "gen_libs" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.


## [2.2.0] - 2017-08-16
### Changed
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.
- Change single quotes to double quotes.
- Changed local libraries to use modules in ./lib directory.


## [2.1.0] - 2017-01-27
### Fixed
- From line was being ignored by the mail program as the -f option was not being passed correctly to the Mail class.
- Run_Program:  Corrected error on how from line passed to class.
- Help_Message: Updated documentation.


## [2.0.0] - 2016-04-13
### Changed
- Modified the program to use the system class instances for creating and sending out emails.  Revamped the entire program to use the system.Mail class instance.
- Added: "-f" option to the program - from address.

### Added
- Run_Program:  To control running of program.

### Removed
- Read_Text
- Create_Body
- Send_Mail
- smtplib module.


## [1.2.0] - 2016-04-12
### Changed
- main:  Added exit call.
- main:  Made a number of changes to streamline the code and argument processing to include changing from Arg_Parse to Arg_Parse2, add a Help_Func call, change arguments to pass by value verus passing by array in a number of function calls, removed a number of "else" statements and opt_noval_list variable.
- Send_Mail:  Changed argument args_array to to_line.
- Create_Body:  Changed argument args_array to subj_line.
- Read_Text:  Added "sys." to stdin.
- Added Version information, added gen_libs library, and modified sys library.

### Added
- Help_Message function.


## [1.1.0] - 2015-10-01
### Changed
- Replaced the Arg_Parse and Arg_Require functions with calls to the arg_parser library module.


## [1.0.0] - 2015-09-30
- Initial Creation.

