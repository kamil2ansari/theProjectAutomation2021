import time
from pages.home.item_buying_page import ItemBuyingPage
from utilities.teststatus import TestStatus
from utilities.read_data import getCSVData
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ItemToBuysTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ibp = ItemBuyingPage(self.driver)
        self.ts = TestStatus(self.driver)

    # def setUp(self):
    #     self.driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/kamil/projects/theVintageBar/testdata.csv"))
    @unpack
    def test_itemBuyValid(self, itemV, lk):
        # self.ibp.registrationLink()
        self.ibp.itemBuyingPage(itemV)
        result = self.ibp.verifyItemBuysSuccessful()
        assert result == True
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()




