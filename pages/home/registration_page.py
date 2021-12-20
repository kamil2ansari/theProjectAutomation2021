from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class RegistrationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  locators for Registration Page
    _sign_in_button = "//*[@class='login']"
    _email_add_field = "//*[@id='email_create']"
    _create_an_account = "//*[@id='SubmitCreate']"
    _first_name = "//input[contains(@id,'customer_firstname')]"
    _last_name = "//input[contains(@id,'customer_lastname')]"
    _password_account = "//input[contains(@id,'passwd')]"
    _first_name_address = "//*[@id='firstname']"
    _last_name_address = "//*[@id='lastname']"
    _address_one = "//*[@id='address1']"
    _address_two = "//*[@id='address2']"
    _city = "//*[@id='city']"
    _state = "//*[@id='id_state']/option[6]"
    _zip_code = "//*[@id='postcode']"
    _mobile_number = "//*[@id='phone_mobile']"
    _registration_button = "//*[@id='submitAccount']/span/i"

    def signInButton(self):
        self.elementClick(self._sign_in_button, locatorType="xpath")

    def enterNewMail(self, emailReg):
        self.sendKeys(emailReg, self._email_add_field, locatorType="xpath")

    def createAnAccount1(self):
        self.elementClick(self._create_an_account, locatorType="xpath")

    def firstName(self, fName):
        self.sendKeys(fName, self._first_name, locatorType="xpath")

    def lastName(self, lName):
        self.sendKeys(lName, self._last_name, locatorType="xpath")

    def passwordField(self, pwd):
        self.sendKeys(pwd, self._password_account, locatorType="xpath")

    def fNameAddress(self, fNameAdd):
        self.sendKeys(fNameAdd, self._first_name_address, locatorType="xpath")

    def lNameAddress(self, lNameAdd):
        self.sendKeys(lNameAdd, self._last_name_address, locatorType="xpath")

    def addressOne(self, address1):
        self.sendKeys(address1, self._address_one, locatorType="xpath")

    def addressTwo(self, address2):
        self.sendKeys(address2, self._address_two, locatorType="xpath")

    def cityAdd(self, city1):
        self.sendKeys(city1, self._city, locatorType="xpath")

    def stateAdd(self, state1):
        self.sendKeys(state1, self._state, locatorType="xpath")

    def zipCode(self, codeZip):
        self.sendKeys(codeZip, self._zip_code, locatorType="xpath")

    def mobilePhone(self, mobileNumber):
        self.sendKeys(mobileNumber, self._mobile_number, locatorType="xpath")

    def registrationClick(self):
        self.elementClick(self._registration_button, locatorType="xpath")

    # def enterRegistrationPass(self, passwordRegistration):
    #     self.sendKeys(passwordRegistration, self._passwordRegistration_field, locatorType="xpath")
    #
    # def enterRegistrationName(self, nameRegistration):
    #     self.sendKeys(nameRegistration, self._name_field, locatorType="xpath")
    #
    # def createAnAccount(self):
    #     self.elementClick(self._create_an_account, locatorType="xpath")
    #
    # def cancelIconButton(self):
    #     self.elementClick(self._cancel_icon, locatorType="xpath")

    def registration(self, emailReg="", fName="", lName="", pwd="", fNameAdd="", lNameAdd="", address1="",
                     address2="", city1="", state1="", codeZip="", mobileNumber=""):
        time.sleep(3)
        self.signInButton()
        time.sleep(7)
        self.enterNewMail(emailReg)
        time.sleep(2)
        self.createAnAccount1()
        time.sleep(8)
        self.firstName(fName)
        self.lastName(lName)
        time.sleep(5)
        self.passwordField(pwd)
        time.sleep(5)
        self.fNameAddress(fNameAdd)
        self.lNameAddress(lNameAdd)
        self.addressOne(address1)
        self.addressTwo(address2)
        self.cityAdd(city1)
        self.stateAdd(state1)
        self.zipCode(codeZip)
        self.mobilePhone(mobileNumber)
        self.registrationClick()
        # self.enterRegistrationPass(passwordRegistration)
        # self.enterRegistrationName(nameRegistration)
        # self.createAnAccount()

    def verifyRegistrationSuccessful(self):
        result = self.isElementPresent("//h1[@class='page-heading']", locatorType="xpath")
        return result

    def logoutInitial(self):
        self.elementClick("//a[@class='logout']", locatorType="xpath")

    # def verifyValidationMessageForEmail(self):
    #     result = self.isElementPresent("//div[contains(@class,'form-group')]//div[1]/span", locatorType="xpath")
    #     return result
