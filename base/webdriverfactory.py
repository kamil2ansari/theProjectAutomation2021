"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        # baseURL = "https://dev.thevintagebardev.com/"
        baseURL = "http://automationpractice.com/index.php"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=r'C:\Users\kamil\projects\theVintageBar\drivers\geckodriver'
                                                       r'.exe')

        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(executable_path=r'C:\Users\kamil\projects\theVintageBar\drivers\chromedriver.exe')
        else:
            driver = webdriver.Firefox(executable_path=r'C:\Users\kamil\projects\theVintageBar\drivers\geckodriver'
                                                       r'.exe')
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
