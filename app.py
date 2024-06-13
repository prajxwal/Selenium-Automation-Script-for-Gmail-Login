import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

# Read the CSV file
df = pd.read_csv('example.csv')

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def login(email, password):
    try:
        # Open a new tab and switch to it
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])

        driver.get('https://accounts.google.com/signin/v2/identifier')

        # Enter email and proceed
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'identifierId'))
        )
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)

        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'Passwd'))
        )
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, 'Passwd'))
        )
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 20).until(
            EC.url_contains("mail.google.com")
        )
        print(f"Logged in successfully with {email}")
    except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print(f"Failed to log in with {email}. Password might be incorrect or element not interactable.")

for index, row in df.iterrows():
    login(row['Email'], row['Password'])

driver.quit()