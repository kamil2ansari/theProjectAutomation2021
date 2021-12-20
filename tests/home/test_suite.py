import unittest
from tests.home.login_tests import LoginTests
from tests.home.item_buying_tests import ItemToBuysTests
from tests.home.registration_tests import RegistrationTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ItemToBuysTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(RegistrationTests)

# create a test suite combining all test classes

smokeTest = unittest.TestSuite([tc1, tc2, tc3])
unittest.TextTestRunner(verbosity=2).run(smokeTest)

