from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the URL
driver.get('https://www.target.com/')
sleep(4)

# Populate sign-in field
sign_in = driver.find_element(By.ID, 'account-sign-in')
sign_in.click()

# Wait for 4 sec
sleep(4)

# Click the sign-in button
sign_in_button = driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
sign_in_button.click()

# Wait for 4 sec
sleep(4)

# Verify the text 'Sign into your Target account' appears in a span on the page
try:
    sign_in_text = driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
    print("Verification passed: 'Sign into your Target account' is present.")
except:
    print("Verification failed: 'Sign into your Target account' is not present.")
    
    
    
try: 
    sign_in_button_verification = driver.find_element(By.ID, 'login')
    print("Verification passed: 'Sign in' button is present.")
except:
    print("Verification failed: 'Sign in' button is not present.")

driver.quit()
