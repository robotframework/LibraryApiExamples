*** Settings ***
Library     DynamicLibrary

*** Test Cases ***
Example
    Keyword
    Keyword    arg1    arg2

Argument spec
    Another keyword    first
    Another keyword    first    second    third
    Another keyword    mandatory    arg3=given

Kwargs
    Kwargs    a=1    b=2    c=3
