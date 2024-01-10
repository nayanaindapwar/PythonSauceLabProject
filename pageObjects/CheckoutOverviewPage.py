from selenium.webdriver.common.by import By

from pageObjects.CheckoutCompletePage import CheckoutCompletePage


class CheckoutOverviewPage:

    def __init__(self, driver):
        self.driver = driver

    finish_button = (By.ID, "finish")

    def clickFinishButton(self):
        self.driver.find_element(*CheckoutOverviewPage.finish_button).click()
        checkoutCompletePage = CheckoutCompletePage(self.driver)
        return checkoutCompletePage
