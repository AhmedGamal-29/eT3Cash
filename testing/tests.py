from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.alert import Alert

# Setup WebDriver
chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Maximize the window and navigate to the app
driver.get("http://localhost:5173/")
driver.maximize_window()

# Helper function to wait for elements
def wait_for_element(by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# Function to find a button by its text
def find_button_by_text(button_text):
    try:
        return wait_for_element (By.XPATH, f"//button[contains(text(), '{button_text}')] | //a[contains(text(), '{button_text}')] | //button[span[contains(text(), '{button_text}') ]]")
    except Exception as e:
        print(f"Error finding button by text '{button_text}': {e}")
        print("Page Source:")
        print(driver.page_source)  # for debugging
        raise

# Register function if needed
def register(username, email, phone, password):
    try:
        wait_for_element(By.ID, "username").send_keys(username)
        wait_for_element(By.ID, "email").send_keys(email)
        wait_for_element(By.ID, "phone").send_keys(phone)
        wait_for_element(By.ID, "password").send_keys(password)
        find_button_by_text("Register").click() 
        print("Register successful")
    except Exception as e:
        print(f"Register failed: {e}")
def back():
    time.sleep(2)
    driver.back()

# Login function if needed
def login(username, password):
    try:
        wait_for_element(By.ID, "username").send_keys(username)
        wait_for_element(By.ID, "password").send_keys(password)
        find_button_by_text("Login").click() 
        print("Login successful")
    except Exception as e:
        print(f"Login failed: {e}")

# Cash In test case
def test_cash_in(amount):
    try:
        find_button_by_text("Cash In").click() 
        wait_for_element(By.ID, "amount").send_keys(amount)
        time.sleep(2)
        find_button_by_text("Submit").click() 
        print(f"Cash In of {amount} successful")
        back()
    except Exception as e:
        print(f"Cash In failed: {e}")

# Cash Out test case
def test_cash_out(amount):
    try:
        find_button_by_text("Cash Out").click() 
        wait_for_element(By.ID, "amount").send_keys(amount)
        time.sleep(2)
        find_button_by_text("Submit").click() 
        print(f"Cash Out of {amount} successful")
        back()
    except Exception as e:
        print(f"Cash Out failed: {e}")

# Check Balance test case
def test_check_balance():
    try:
        find_button_by_text("Check Balance").click() 
        find_button_by_text("Check Balance").click() 
        balance_element = wait_for_element(By.CLASS_NAME, "balance-display")
        balance = balance_element.text
        print(f"Current balance: {balance}")
        back()
    except Exception as e:
        print(f"Check Balance failed: {e}")

# Donate test case
def test_donate(amount):
    try:
        find_button_by_text("Donate").click() 
        wait_for_element(By.ID, "amount").send_keys(amount)
        time.sleep(2)
        find_button_by_text("Submit Donation").click() 
        print(f"Donation of {amount} successful")
        back()
    except Exception as e:
        print(f"Donation failed: {e}")

# Invest test case
def test_invest(amount):
    try:
        find_button_by_text("Invest").click() 
        wait_for_element(By.ID, "amount").send_keys(amount)
        time.sleep(2)
        find_button_by_text("Submit Investment").click() 
        print(f"Investment of {amount} successful")
        back()
    except Exception as e:
        print(f"Investment failed: {e}")

# Transactions test case
def test_transactions():
    try:
        find_button_by_text("Transaction History").click() 
        time.sleep(5)
        print(f"Transactions successful")
        back()
    except Exception as e:
        print(f"Transactions failed: {e}")


# Test execution
try:

    login("wrong username", "wrong password")
    time.sleep(2)
    Alert(driver).accept()
    driver.refresh()
    time.sleep(2)
    login("ahmed", "ahmed__$$1000")

   # Test cash in with $100
    test_cash_in(-100)
    time.sleep(2)
    test_cash_in(100)

    # Test cash out with $50
    test_cash_out(-50)
    time.sleep(2)
    test_cash_out(50)

    # Check balance
    test_check_balance()

    # Donate $20 to a charity
    test_donate(210)

    # Invest $100 in a stock
    test_invest("hello world")
    time.sleep(2)
    test_invest(80)

    time.sleep(2)
    test_transactions()

finally:
    # Close the browser after the tests
    time.sleep(5)
    driver.quit()