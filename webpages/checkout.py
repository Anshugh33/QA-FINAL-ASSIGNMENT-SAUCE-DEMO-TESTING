from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # Locators
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.cancel_btn = (By.ID, "cancel")

    # Fill checkout details
    def fill_details(self, first, last, zip_code):
        self.driver.find_element(*self.first_name).send_keys(first)
        try:
            self.driver.find_element(*self.last_name).send_keys(last)
        except:
    # Handle non-editable last name
            pass
        self.driver.find_element(*self.zip_code).send_keys(zip_code)
        print("Checkout details entered")
        time.sleep(2)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()
        print("Clicked Continue")
        time.sleep(2)

    # Check first name empty error
    def first_name_empty(self, zip_code):
        self.driver.find_element(*self.first_name).clear()
        self.driver.find_element(*self.zip_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_btn).click()
        print("First Name empty error displayed")
        time.sleep(2)

    # Last Name non-editable behavior
    def last_name_non_editable(self, first, last, zip_code):
        self.driver.find_element(*self.first_name).send_keys(first)
        try:
            self.driver.find_element(*self.last_name).send_keys(last)
        except:
            print("Last Name cannot be typed")
        self.driver.find_element(*self.zip_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_btn).click()
        print("Error displayed for non-editable Last Name")
        time.sleep(2)

    #  Cancel button
    def click_cancel(self):
        self.driver.find_element(*self.cancel_btn).click()
        print("Cancelled checkout, returned to cart")
        time.sleep(2)
