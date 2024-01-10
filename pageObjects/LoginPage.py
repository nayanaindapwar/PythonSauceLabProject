from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pageObjects.ProductsPage import ProductsPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    loginbutton = (By.ID, "login-button")

    def enterUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def enterPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickLoginButton(self):
        login_button = self.driver.find_element(*LoginPage.loginbutton)
        # Use JavaScript to click the button
        self.driver.execute_script("arguments[0].click();", login_button)
        productsPage = ProductsPage(self.driver)
        return productsPage




