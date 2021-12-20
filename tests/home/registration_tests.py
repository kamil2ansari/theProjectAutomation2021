from pages.home.registration_page import RegistrationPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegistrationTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.rp = RegistrationPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validRegistration(self):
        self.rp.logoutInitial()
        # self.rp.registrationLink()
        self.rp.registration("testing7840046437@mailinator.com", "Kamil", "Testing", "Testing@123", "Testing", "Test",
                             "AddressOne", "addressTwo", "TestCity", "New Delhi", "00000", "9876543210")
        result = self.rp.verifyRegistrationSuccessful()
        assert result == True



    # @pytest.mark.run(order=2)
    # def test_validationMessageEmail(self):
    #     self.rp.registrationLink()
    #     self.rp.joinButtonClick()
    #     result = self.rp.verifyValidationMessageForEmail()
    #     assert result == True

