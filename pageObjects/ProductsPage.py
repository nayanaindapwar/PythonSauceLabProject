from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver


    addtocartbackpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    addtocartbikelight = (By.ID, "add-to-cart-sauce-labs-bike-light")
    shoppingcartbadge = (By.CSS_SELECTOR, ".shopping_cart_link")

    def click_addtocartbackpack(self):
        return self.driver.find_element(*ProductsPage.addtocartbackpack)

    def click_addtocartbikelight(self):
        return self.driver.find_element(*ProductsPage.addtocartbikelight)

    def click_shoppingcartbadge(self):
        self.driver.find_element(*ProductsPage.shoppingcartbadge).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage