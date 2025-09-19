from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from webpages.loginpage import LoginPage
from webpages.dashboardpage import DashboardPage
from webpages.cart import CartPage
from webpages.checkout import CheckoutPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")
time.sleep(2)

login = LoginPage(driver)
dashboard = DashboardPage(driver)
cart = CartPage(driver)
checkout = CheckoutPage(driver)

# Invalid login
login.enter_username("problem_user")
login.enter_password("wrongpass")
login.click_login()
print("TC_01: Error displayed for invalid login")
time.sleep(2)

driver.find_element(By.ID, "user-name").clear()
driver.find_element(By.ID, "password").clear()

# Valid login
login.enter_username("problem_user")
login.enter_password("secret_sauce")
login.click_login()
print("TC_02: Logged in with valid credentials")
time.sleep(2)

# Dashboard tests
dashboard.check_product_images()
dashboard.open_burger_menu()
dashboard.click_all_items()
dashboard.click_about()

driver.back()
time.sleep(2)

# Cart tests - add items first
cart.add_items()

# Open burger menu to reset app state (removes cart items)
dashboard.open_burger_menu()
dashboard.reset_app_state()
time.sleep(1)

# Sorting
dashboard.select_sort_option("Name (A to Z)")
time.sleep(2)

# Cart tests after reset
cart.view_cart()
cart.continue_shopping_action()

# Navigate to cart and checkout
cart.view_cart()
driver.find_element(By.ID, "checkout").click()  # open checkout page
time.sleep(2)

# Checkout tests
checkout.fill_details("Anshu", "Ghimire", "12345")
checkout.click_continue()
checkout.first_name_empty("12345")
checkout.last_name_non_editable("Anshu", "Ghimire", "12345")
checkout.click_cancel()

# Final logout
dashboard.open_burger_menu()
dashboard.logout()
print("Logged out successfully")

driver.quit()


