'''
Testing (1..2..3..)

Regression = Going in reverse
Regression Testing => As we make changes to code, we don't (re)introduce
bugs that we've already fixed or break functionality that used to work

Interface contract:
  name
  parameter(s)
  expected output / return value

Unit testing
    QA (Quality Assurance)
    Formal specifications for tests that test whether
    a interface (visual or contract) functions as specified
    Can be automated

Automated Unit Tests

Regression Testing??
    Create a library of tests for EVERY module
        Basic functionality
        Edge cases
        etc.
    Every time a change is made to code, (re)run the test library
    Create a test to "flex" or "surface" each bug

TDD - Test-Driven Development (TFirstD)
    Forces us to create testable code


Solution we looked at: doctest
Much betterer solution: unittest
                        (similar to jUnit,nUnit,"xUnit")
'''


from newfuncs326 import pythag

print(pythag(3,4))
