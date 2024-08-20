from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Path to the ChromeDriver executable
chrome_driver_path = r'C:\webdrivers\chromedriver.exe'  # Use raw string to avoid escape sequence issues

# URL of the webpage to scrape
url = 'file:///C:/Users/FAWZAN/Downloads/Crocs In Sport Mode (CROCS) _ Solscan 3.html'

# Initialize the Chrome WebDriver with the Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get(url)

# Wait for the content to load (adjust the selector as necessary)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'text-link'))
    )
except Exception as e:
    print(f"Error waiting for elements: {e}")

# Get the page source (HTML content)
html_content = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all the <td> elements with the specific class
td_elements = soup.find_all('td', class_='h-12 px-2 py-[10px] align-middle text-[14px] leading-[24px] font-normal text-neutral7 [&:has([role=checkbox])]:pr-0 border-t')

# Extract the <a> tags within the <td> elements and print their text
for td in td_elements:
    a_tag = td.find('a', class_='text-link')
    if a_tag:
        print(a_tag.get_text())

