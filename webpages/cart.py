from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # Locators
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_bikelight = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.remove_backpack = (By.ID, "remove-sauce-labs-backpack")
        self.remove_bikelight = (By.ID, "remove-sauce-labs-bike-light")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.continue_shopping = (By.ID, "continue-shopping")

    # Add items to cart
    def add_items(self):
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.add_bikelight).click()
        print("Items added to cart")
        time.sleep(2)

    # Remove items from dashboard
    def remove_items_dashboard(self):
        self.driver.find_element(*self.remove_backpack).click()
        self.driver.find_element(*self.remove_bikelight).click()
        
        # Verify if items still exist
        backpack_present = len(self.driver.find_elements(*self.add_backpack)) > 0
        bikelight_present = len(self.driver.find_elements(*self.add_bikelight)) > 0
        
        if backpack_present or bikelight_present:
            print("Remove button failed")  
        else:
            print("Items removed successfully")
        
        time.sleep(2)

    # View cart
    def view_cart(self):
        self.driver.find_element(*self.cart_icon).click()
        print("Cart opened")
        time.sleep(2)

    # Continue shopping
    def continue_shopping_action(self):
        self.driver.find_element(*self.continue_shopping).click()
        print("Continued shopping")
        time.sleep(2)
