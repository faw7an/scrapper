from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

# Path to the ChromeDriver executable
chrome_driver_path = r'C:\webdrivers\chromedriver.exe'  # Use raw string to avoid escape sequence issues

# URL of the webpage to scrape (replace with the desired URL)
url = 'https://solscan.io/token/7u6WirUYbf3kJdZQoPTCYjgU5rpVg21LuXLKmmCUpump?page=5#holders'  # Replace with the actual URL you want to scrape

# Initialize the Chrome WebDriver with the Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get(url)

# Wait for the content to load (adjust the selector as necessary)
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'td'))
    )
except Exception as e:
    print(f"Error waiting for elements: {e}")

# Scroll down to ensure all dynamic content is loaded
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)  # Wait for additional content to load

# Get the page source (HTML content)
html_content = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all the <td> elements with the specific class
td_elements = soup.find_all('td', class_='h-12 px-2 py-[10px] align-middle text-[14px] leading-[24px] font-normal text-neutral7 [&:has([role=checkbox])]:pr-0 border-t')

# Check if any <td> elements were found
if not td_elements:
    print("No <td> elements found.")

# Define the class to include
include_class = 'text-link'

# Initialize a list to store the extracted <a> tag texts
a_tags_text = []

# Extract the first <a> tag within each <td> element and filter based on class
for td in td_elements:
    a_tag = td.find('a', class_=include_class)
    if a_tag:
        a_tags_text.append(a_tag.get_text())

# Filter the list to include only the links at even indices
filtered_a_tags_text = [text for index, text in enumerate(a_tags_text) if index % 2 == 0]

# Save the filtered <a> tag texts to a CSV file
csv_file_path = 'output.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Link Text'])  # Write the header
    for text in filtered_a_tags_text:
        writer.writerow([text])

print("CSV file has been created successfully.")
