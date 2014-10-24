*** Settings ***
Library      LibraryClass
Library      LibraryClass.TestSuiteScope

*** Test Cases ***
Keyword name and args
    Keyword    arg

State
    Add    1    2
    Result should be    3
    Result should be    2

Test case scope
    Result should be    3

Test suite scope 1a
    Add 2    1    2
    Result should be 2    3

Test suite scope 1b
    Result should be 2    3
