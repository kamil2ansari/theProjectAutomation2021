# from selenium import webdriver
from base.basepage import BasePage
# from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

'''
Registration link x-path: //ul[contains(@class,'cart-sign')]//span[2]
Email input x-path: //div[contains(@class,'register-form')]//div[2]/input
Join us button x-path: //button[contains(text(),' JOIN US NOW ')]
NEXT FORM
Password field x-path: //input[contains(@placeholder,'Password *')]
Name field x-path: //input[contains(@placeholder,'Name *')]
Create an Account X: // button[contains(text(),'CREATE AN ACCOUNT ')]
'''


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for login page
    _sign_in_button = "//a[contains(@class,'login')]"
    _email_field = "//input[(@id='email')]"
    _password_field = "//input[contains(@id,'passwd')]"
    _login_button = "//button[contains(@id,'SubmitLogin')]"

    # _close_icon = "//button/i[contains(@class,'material-icons')]"

    # def waiting(self):
    #   self.waitForElement(self._login_link, locatorType="xpath")

    # def clickLoginLink(self):
    #  self.elementClick(self._login_link, locatorType="xpath")

    def signInLink(self):
        self.elementClick(self._sign_in_button, locatorType="xpath")

    # def jumpToPopUP(self):
    #    self.driver.switch_window

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    # def closeLoginForm(self):
    # self.elementClick(self._close_icon, locatorType="xpath")

    def login(self, email="", password=""):
        # self.waiting()
        # self.clickLoginLink()
        # self.clearFields()
        # time.sleep(3)
        self.signInLink()
        # self
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//li/a/i", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent('//*[@id="center_column"]/div[1]/p', locatorType="xpath")
        return result

    def verifyLoginValid(self):
        result = self.isElementPresent("//h1[@class='page-heading']", locatorType="xpath")
        return result

    def verifyNotLoginBlankPass(self):
        result = self.isElementPresent("//h1[contains(@class,'page-heading')]", locatorType="xpath")
        return result

    def verifyNotLoginBlankNMailId(self):
        result = self.isElementPresent("//span[contains(text(),'Email address is required')]", locatorType="xpath")
        return result

    def verifyPassMasked(self):
        result = self.isElementDisplayed("//input[contains(@type,'password')]", locatorType="xpath")
        return result

    def verifyLoginPage(self):
        result = self.isElementPresent("//h3[contains(text(),'MEMBER SIGN IN')]", locatorType="xpath")
        return result

    def verifyLoginPage2(self):
        result = self.isElementPresent("//li/a/i", locatorType="xpath")
        return result

    def verifyLogout(self):
        # menu_button = self.elementClick('//button[contains(@id, "react-burger-menu-btn")]', locatorType="xpath")
        # time.sleep(7)
        menu_list = self.elementClick("//ul[contains(@class,'cart-sign')]//a[2]", locatorType="xpath")
        result = self.isElementPresent("//ul[contains(@class,'cart-sign')]//span[2]", locatorType="xpath")
        return result

    def refreshBrowser(self):
        return self.driver.refresh()

    def scrollPage(self):
        return self.webScroll(direction="down")

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Testing the login")

    def logoutInitial(self):
        self.elementClick("//a[@class='logout']", locatorType="xpath")


    # def verifyPassMasked(self):
    # result = self.

    # def verifyLoginFailedBlank(self):
    # result = self.isElementPresent("//center/b", locatorType="xpath")
    # return result

    # def verifyLoginBlankPass(self):
    #  result = self.isElementPresent("//center/b", locatorType="xpath")
    #  return result

    def clearFields(self):
        emailField = self.getElement(self._email_field, locatorType="xpath")
        emailField.clear()
        passwordField = self.getElement(self._password_field, locatorType="xpath")
        passwordField.clear()

# //div[contains(text(),'Invalid email or password.')]
# //center/b[contains(text(),'**Failed Login**')]
