from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Locators
        
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")


    # Enter username
    
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        # print for debug
        print(f"Entered username: {username}")

    
    # Enter password
    
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        print(f"Entered password: {password}")

    
    # Click login button
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        print("Clicked login button")
        time.sleep(3)

    
    # Check if error message is displayed
    
    def is_error_displayed(self):
        try:
            error = self.driver.find_element(*self.error_message).is_displayed()
            return error
        except:
            return False
