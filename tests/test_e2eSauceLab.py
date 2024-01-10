
import time
from telnetlib import EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from TestData.LoginData import LoginData
from pageObjects.CheckoutInfo import CheckoutInfoPage
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductsPage import ProductsPage
from utilities.BaseClass import BaseClass


class TestE2ESauceLab(BaseClass):

    def test_e2eSauceLab(self, getData):
    #def test_e2eSauceLab(self):
        loginpage = LoginPage(self.driver)
        loginpage.enterUsername().send_keys(getData["username"])
        time.sleep(2)
        loginpage.enterPassword().send_keys(getData["password"])
        time.sleep(2)
        productsPage = loginpage.clickLoginButton()
        time.sleep(3)

        productsPage.click_addtocartbackpack().click()
        time.sleep(2)
        productsPage.click_addtocartbikelight().click()
        time.sleep(2)
        checkoutPage = productsPage.click_shoppingcartbadge()
        time.sleep(2)

        checkoutInfoPage = checkoutPage.click_CheckoutButton()
        time.sleep(2)
        checkoutInfoPage.enterFirstname().send_keys("rahul")
        time.sleep(2)
        checkoutInfoPage.enterLastname().send_keys("acharya")
        time.sleep(2)
        checkoutInfoPage.enterPostalcode().send_keys("440022")
        time.sleep(2)
        checkoutOverviewPage = checkoutInfoPage.click_ContinueButton()
        time.sleep(2)
        checkoutCompletePage = checkoutOverviewPage.clickFinishButton()
        time.sleep(2)
        checkMessage = checkoutCompletePage.successMessage()
        print(checkMessage)
        assert "Thank you for your order!" in checkMessage

    @pytest.fixture(params=LoginData.getTestData())
    def getData(self, request):
        return request.param