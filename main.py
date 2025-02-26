import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
# Note: Removed win32clipboard since cookies functionality and Windows-only features are not used.
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import os

def main():
    # Read input from Apify (actor’s input will be provided as JSON via STDIN)
    try:
        input_data = json.loads(os.environ.get('APIFY_INPUT', '{}'))
    except Exception as e:
        print("Error reading input:", e)
        input_data = {}

    # Extract inputs (ignoring cookies functionality)
    groups_input = input_data.get("Facebook_Profile_URL", "")
    message = input_data.get("Message", "Your message here")
    delay = input_data.get("Delay", 15)
    username = input_data.get("Username", "")
    password = input_data.get("Password", "")

    # If username/password are provided in input, use them. Otherwise, fall back to hardcoded defaults.
    account = username if username else "newarchcity.2021@gmail.com"
    password = password if password else "N.A.C_%%"

    # Parse group URLs (comma-separated list)
    groups = [grp.strip() for grp in groups_input.split(",") if grp.strip()]

    # Initialize Selenium Chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    # Disable notifications
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # Use the Linux-friendly options
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.facebook.com')

    # Login using provided credentials
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(account)
    passelement = driver.find_element(By.XPATH, '//*[@id="pass"]')
    passelement.send_keys(password)
    passelement.send_keys(Keys.RETURN)
    time.sleep(2)

    counter = 0
    for group in groups:
        if group == "":
            continue

        whichTab(driver)
        counter += 1
        try:
            postingProcess(group, driver, message, counter)
        except Exception as e:
            print("Error posting to", group, e)
            time.sleep(delay)
            postingProcess(group, driver, message, counter)
        time.sleep(delay)

    driver.close()

def postingProcess(group, driver, message, counter):
    driver.get(group)
    time.sleep(1.5)
    try:
        page_name = driver.find_element(By.CSS_SELECTOR, ".oajrlxb2").text
        print(f"{counter}: Now trying on page: {page_name}")
    except Exception:
        time.sleep(3)
        page_name = driver.find_element(By.CSS_SELECTOR, ".oajrlxb2").text
        print(f"{counter}: Now trying on page: {page_name}")

    goingToPostLayout(driver)
    time.sleep(0.5)
    # Wait for the post box to become available
    while True:
        try:
            post_box = driver.find_element(By.XPATH, "//div[@data-block='true']//div")
            break
        except Exception:
            time.sleep(1)
    post_box.send_keys(message)
    # Click post button (XPath may need to be updated)
    driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Post')]").click()
    print("Posting on", group)
    time.sleep(1)

def goingToPostLayout(driver):
    # Simplified version: click on "Create a public post" if available
    try:
        post_trigger = driver.find_element(By.XPATH, "//span[contains(text(),'Create a public post')]")
        post_trigger.click()
    except Exception as e:
        print("Could not locate public post trigger:", e)
    time.sleep(2)

def whichTab(driver):
    handles = driver.window_handles
    for handle in handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
            if driver.current_url != "https://www.facebook.com":
                return
    # Open a new tab if needed
    if len(handles) < 5:
        driver.execute_script('window.open("https://www.facebook.com")')
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)

if __name__ == '__main__':
    main()
