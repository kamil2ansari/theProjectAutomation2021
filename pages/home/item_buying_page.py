from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class ItemBuyingPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  locators for Registration Page
    _search_box = "//*[@id='search_query_top']"
    _search_icon = "//*[@name='submit_search']"
    _hover_item = "//*[@class='product-image-container']"
    _add_to_cart = "//*[@id='center_column']/ul/li/div/div[2]/div[2]/a[1]"
    _proceed_to_checkout = "//*[@id='layer_cart']/div[1]/div[2]/div[4]/a"
    _proceed_to_checkout_summary = "//*[@id='center_column']/p[2]/a[1]"
    _proceed_to_checkout_address = "//*[@id='center_column']/form/p/button"
    _terms_of_services = "//*[@id='cgv']"
    _proceed_to_checkout_shipping = "//*[@id='form']/p/button"
    _payment_via_wire = "//*[@id='HOOK_PAYMENT']/div[1]/div"
    _confirm_order = "//*[@id='cart_navigation']/button"

    def searchItem(self, item_value):
        self.sendKeys(item_value, self._search_box, locatorType="xpath")
        self.elementClick(self._search_icon, locatorType="xpath")

    def plpHover(self):
        self.mouseHovering(self._hover_item, self._add_to_cart, locatorType="xpath")

    def plpPopUp(self):
        self.elementClick(self._proceed_to_checkout, locatorType="xpath")

    def Summary(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        self.elementClick(self._proceed_to_checkout_summary, locatorType="xpath")

    def Address(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        self.elementClick(self._proceed_to_checkout_address, locatorType="xpath")

    def shippingTerms(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        self.elementClick(self._terms_of_services, locatorType="xpath")

    def shipping(self):
        self.elementClick(self._proceed_to_checkout_shipping, locatorType="xpath")

    def Payment(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        self.elementClick(self._payment_via_wire, locatorType="xpath")

    def PaymentConfirm(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        self.elementClick(self._confirm_order, locatorType="xpath")

    def itemBuyingPage(self, item_value=''):
        time.sleep(7)
        self.searchItem(item_value)
        time.sleep(5)
        self.plpHover()
        time.sleep(4)
        self.plpPopUp()
        time.sleep(5)
        self.Summary()
        time.sleep(2)
        self.Address()
        time.sleep(5)
        self.shippingTerms()
        time.sleep(2)
        self.shipping()
        time.sleep(2)
        self.Payment()
        time.sleep(2)
        self.PaymentConfirm()
        time.sleep(15)

    def verifyItemBuysSuccessful(self):
        result = self.isElementPresent("//*[@id='center_column']/div/p/strong", locatorType="xpath")
        return result

    # def verifyValidationMessageForEmail(self):
    #     result = self.isElementPresent("//div[contains(@class,'form-group')]//div[1]/span", locatorType="xpath")
    #     return result
