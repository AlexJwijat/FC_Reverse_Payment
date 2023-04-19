# Import required libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define the URL to be accessed
url = "https://firmcentral.westlaw.com/"

# Initialize the webdriver for Chrome and open the URLss
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

# Get user input for username and password
username = input("Enter your username: ")
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Username")))
password = input("Enter your password: ")
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Password")))

#Input username and password in browser
username_input.send_keys(username)
password_input.send_keys(password)


#Sign In
next_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "SignIn"))
)
next_button.click()

print("Logged in")

# List of invoice links to be reversed
lst = []

while True:
    for link in lst:
        driver.get(link)
        # Define selectors for dropdown, reverse, and save buttons
        dropdown_css = ".icon_greyArrowDown"
        dropdown_class = "showActionsMenu dropDownArrow btn_secondary hasIcon"
        dropdown_xpath = "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[6]/div/div/div/table/tbody/tr/td[7]/ul/li[2]/a/span"

        reverse_css = ".reversePayment"
        reverse_class = "reversePayment dropDownButton"
        reverse_xpath = "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[6]/div/div/div/table/tbody/tr/td[7]/ul/li[2]/div/div/ul/li/a"

        save_class = "btn_primary savePaymentAction"
        save_css = ".btn_primary"
        save_xpath = "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[5]/ul/li[5]/button"

        # Locate the dropdown and click it
        dropdown = WebDriverWait(driver, 10).until(EC.
        presence_of_element_located((By.CSS_SELECTOR, dropdown_css)))
        dropdown.click()

        # Locate the reverse button and click it
        reverse = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, reverse_css)))
        reverse.click()
        
         # Locate the save button and click it
        save = WebDriverWait(driver, 10).until(EC.
        presence_of_element_located((By.CSS_SELECTOR, save_css)))
        save.click()
        
        # Print a message indicating the reversal process is complete for the current invoice
        print(f"Reversal complete for invoice: {link}")

    # Close the webdriver when the reversal process is complete for all invoices
    driver.quit()
        
