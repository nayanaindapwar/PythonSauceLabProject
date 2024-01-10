from selenium.webdriver.common.by import By

from pageObjects.CheckoutOverviewPage import CheckoutOverviewPage


class CheckoutInfoPage:

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.ID, "first-name")
    lastname = (By.ID, "last-name")
    postalcode = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    def enterFirstname(self):
        return self.driver.find_element(*CheckoutInfoPage.firstname)

    def enterLastname(self):
        return self.driver.find_element(*CheckoutInfoPage.lastname)

    def enterPostalcode(self):
        return self.driver.find_element(*CheckoutInfoPage.postalcode)

    def click_ContinueButton(self):
        self.driver.find_element(*CheckoutInfoPage.continue_button).click()
        checkoutOverviewPage = CheckoutOverviewPage(self.driver)
        return checkoutOverviewPage