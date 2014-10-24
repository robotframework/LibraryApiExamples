*** Settings ***
Library     basics.py

*** Test Cases ***
Keyword name
    Keyword

Arguments
    Argument    arg
    Two Arguments    a1    a2
    Default Values    mandatory
    Default Values    mandatory    optional 1
    Default Values    mandatory    optional 1    optional 2
    Default Values    mandatory    arg3=optional 2
    Varargs
    Varargs    1
    Varargs    1    2    3    4    5
    Kwargs    a=1    b=2    c=3
    Combined    required
    Combined    required    foo=bar
    Combined    required    optional    hello=world
    Combined    required    optional    1    2   3

Logging
    Use print
    Print with levels
    Use standard logging
    Use Robot logger

Traceback
    Buggy keyword

Failures
    Should be positive    1
    Should be positive    ${42}
    Should be positive    0

Continuable failures
    Should be negative    -1
    Should be negative    0
    Should be negative    1

Return values
    ${result} =    Add    1    2
    ${result} =    Add    ${result}    4    5
    Should be equal    ${result}   ${12}

Object as return value
    ${unit} =    Get Unit    xyz
    Should be equal    ${unit.name}    xyz
    Should be equal    ${unit.type}    foo
    Should be equal    ${unit.id}    3

