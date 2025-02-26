import time
import json
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    # Read input from Apify via environment variable
    try:
        input_data = json.loads(os.environ.get("APIFY_INPUT", "{}"))
    except Exception as e:
        print("Error reading input:", e)
        input_data = {}

    # Extract inputs from the actor's input JSON
    groups_input = input_data.get("Facebook_Profile_URL", "")
    message = input_data.get("Message", "Your message here")
    delay = input_data.get("Delay", 15)
    username = input_data.get("Username", "")
    password = input_data.get("Password", "")

    # Use provided credentials or fall back to defaults
    account = username if username else "newarchcity.2021@gmail.com"
    password = password if password else "N.A.C_%%"

    # Parse comma-separated group URLs
    groups = [grp.strip() for grp in groups_input.split(",") if grp.strip()]

    # Set up Chrome options with a unique user-data-dir to avoid conflicts
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.facebook.com")

    # Login using email/username and password
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(account)
    pass_elem = driver.find_element(By.XPATH, '//*[@id="pass"]')
    pass_elem.send_keys(password)
    pass_elem.send_keys(Keys.RETURN)
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
            print("Error posting to", group, ":", e)
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
    # Wait until the post box is available
    while True:
        try:
            post_box = driver.find_element(By.XPATH, "//div[@data-block='true']//div")
            break
        except Exception:
            time.sleep(1)
    post_box.send_keys(message)
    # Click the post button; XPath may require adjustments
    driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Post')]").click()
    print("Posting on", group)
    time.sleep(1)

def goingToPostLayout(driver):
    # Attempt to click the "Create a public post" trigger
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
    # Open a new tab if necessary
    if len(handles) < 5:
        driver.execute_script('window.open("https://www.facebook.com")')
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)

if __name__ == '__main__':
    main()
