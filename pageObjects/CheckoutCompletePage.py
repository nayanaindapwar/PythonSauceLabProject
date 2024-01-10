from selenium.webdriver.common.by import By


class CheckoutCompletePage:

    def __init__(self, driver):
        self.driver = driver

    message = (By.XPATH, "//h2[normalize-space()='Thank you for your order!']")

    def successMessage(self):
        textmsg = self.driver.find_element(*CheckoutCompletePage.message).text
        return textmsg