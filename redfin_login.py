from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
webdriver_path = 'chromedriver.exe'
service = Service(webdriver_path)
# Set the download directory
download_directory = r"C:\Users\shai\Desktop\ftest"
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,  # Set the default download directory
    "download.prompt_for_download": False,  # Disable prompting for download location
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options)



# Set your credentials
USERNAME = "elirazchoen1@gmail.com"
PASSWORD = "shai1234!"


# Set the URL of the Redfin login page
login_url = "https://www.redfin.com/login"

# Create a new instance of the Chrome driver
#driver = webdriver.Chrome()

# Navigate to the Redfin login page
driver.get(login_url)

# Find the username and password fields and input the credentials
username_field = driver.find_element(By.NAME, "emailInput")
password_field = driver.find_element(By.NAME, "passwordInput")

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

# Find and click the login button
login_button = driver.find_element(By.CSS_SELECTOR, ".submitButton")
login_button.click()

# Wait for the login to complete
time.sleep(5)
session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'Accept-Language': 'en-US,en;q=0.9',
 'Accept-Encoding': 'gzip, deflate, br'}
download_page_url = "https://www.redfin.com/stingray/api/gis-csv?al=3&has_att_fiber=false&has_deal=false&has_dishwasher=false&has_laundry_facility=false&has_laundry_hookups=false&has_parking=false&has_pool=false&has_short_term_lease=false&include_pending_homes=false&isRentals=false&is_furnished=false&is_income_restricted=false&is_senior_living=false&market=pittsburgh&num_homes=350&ord=redfin-recommended-asc&page_number=1&poly=-80.37745%2040.29076%2C-79.48618%2040.29076%2C-79.48618%2040.44039%2C-80.37745%2040.44039%2C-80.37745%2040.29076&pool=false&sf=1,2,3,5,6,7&status=9&travel_with_traffic=false&travel_within_region=false&uipt=1&utilities_included=false&v=8"
driver.get(download_page_url)
response = session.get(download_page_url)

#time.sleep(3)
# Find the download link and click it
#download_link = driver.find_element_by_xpath('///*[@id="download-and-save"]')
#download_link.click()

time.sleep(10)
#response = requests.get(url, headers=headers)
#print(response)
# Wait for the redirection to the download page
#WebDriverWait(driver, 10).until(EC.url_contains("download-page"))

# Retrieve the URL of the CSV file from the redirected page
#file_url = driver.current_url

# Use requests to download the file
#response = requests.get(download_link)

# Save the file to disk
#with open("downloaded_file.csv", "wb") as f:
 #   f.write(response.content)

# Close the browser
driver.quit()