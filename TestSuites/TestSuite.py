import unittest
from testCases.LoginTest import LoginTest
import sys
sys.path.append("D:\Automation Projects\POM_using_unittest")

# For getting all the test cases
TC1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)

#Creating test Suites

functionalTestSuite = unittest.TestSuite([TC1])

unittest.TextTestRunner().run(functionalTestSuite)