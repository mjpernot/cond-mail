# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.2.4] - 2020-06-15
### Changed
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
- run_program:  The "From line" in the email will always be set with a default value or user-defined value.
- run_program:  Changed "-s" option to allow for multiple values in subject line.
- run_program:  Checked that the Mail message is not an empty string.
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
- Read_Text function.
- Create_Body function.
- Send_Mail function.
- Removed smtplib module.


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

