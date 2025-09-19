from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DashboardPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.product_images = (By.CLASS_NAME, "inventory_item_img")
        self.burger_menu = (By.ID, "react-burger-menu-btn")
        self.all_items_link = (By.ID, "inventory_sidebar_link")
        self.about_link = (By.ID, "about_sidebar_link")
        self.reset_app_state_link = (By.ID, "reset_sidebar_link")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    def check_product_images(self):
        images = self.driver.find_elements(*self.product_images)
        if len(images) == 6:
            print("Images displayed")
        else:
            print("Images missing")
        time.sleep(2)

    def open_burger_menu(self):
        wait = WebDriverWait(self.driver, 5)
        # Wait until the burger menu is clickable
        burger_btn = wait.until(EC.element_to_be_clickable(self.burger_menu))
        burger_btn.click()
        print("Burger menu opened")
        time.sleep(2)

    def click_all_items(self):
        self.driver.find_element(*self.all_items_link).click()
        print("All Items clicked")
        time.sleep(2)

    def click_about(self):
        self.driver.find_element(*self.about_link).click()
        print("About clicked")
        time.sleep(2)

    def reset_app_state(self):
        self.driver.find_element(*self.reset_app_state_link).click()
        print("Cart cleared")
        time.sleep(2)

    def logout(self):
        self.driver.find_element(*self.logout_link).click()
        print("Logged out")
        time.sleep(2)

    def select_sort_option(self, option_text):
        wait = WebDriverWait(self.driver, 5)
        dropdown_elem = wait.until(EC.visibility_of_element_located(self.sort_dropdown))
        dropdown = Select(dropdown_elem)
        dropdown.select_by_visible_text(option_text)
        print(f"Sorting applied: {option_text}")
        time.sleep(2)
