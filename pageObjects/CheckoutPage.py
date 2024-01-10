from selenium.webdriver.common.by import By

from pageObjects.CheckoutInfo import CheckoutInfoPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver


    checkout_button = (By.ID, "checkout")

    def click_CheckoutButton(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        checkoutInfoPage = CheckoutInfoPage(self.driver)
        return checkoutInfoPage
