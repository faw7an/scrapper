from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

# Prompt the user to input the first page URL
first_page_url = input("Please enter the URL of the first page to scrape: ")

# Prompt the user to input the constant part of the URL for subsequent pages
constant_url_part = input("Please enter the constant part of the URL for subsequent pages (e.g., 'https://solscan.io/token/7u6WirUYbf3kJdZQoPTCYjgU5rpVg21LuXLKmmCUpump?page='): ")

# Prompt the user to input the starting and ending page numbers
start_page = int(input("Please enter the starting page number: "))
end_page = int(input("Please enter the ending page number: "))

# Prompt the user to input the name of the CSV file to be created
csv_file_name = input("Please enter the name of the CSV file to be created (e.g., 'output.csv'): ")

# Path to the ChromeDriver executable
chrome_driver_path = r'C:\webdrivers\chromedriver.exe'  # Use raw string to avoid escape sequence issues

# Initialize the Chrome WebDriver with the Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Function to scrape a single page
def scrape_page(url, page_number):
    print(f"Scraping page {page_number}: {url}")
    
    # Open the webpage
    driver.get(url)
    
    # Wait for the content to load (adjust the selector as necessary)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'td'))
        )
    except Exception as e:
        print(f"Error waiting for elements on page {url}: {e}")
        return []
    
    # Scroll down to ensure all dynamic content is loaded
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Wait for additional content to load
    
    # Get the page source (HTML content)
    html_content = driver.page_source
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract all rows from the table
    rows = soup.find_all('tr')
    
    # Initialize a list to store the extracted 'by' column texts
    by_column_texts = []
    
    # Loop through each row and extract the text from the 6th column
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 6:
            by_column = columns[5]  # 6th column (index 5)
            a_tag = by_column.find('a', class_='text-link')
            if a_tag:
                by_column_texts.append(a_tag.get_text())
    
    return by_column_texts

# Initialize a list to store all the filtered data
filtered_data = []

# Iterate over the range of page numbers
for page_number in range(start_page, end_page + 1):
    # Construct the URL for the current page
    if page_number == start_page:
        url = first_page_url
    else:
        url = f"{constant_url_part}{page_number}#transactions"
    
    # Debugging: Print the constructed URL
    print(f"Constructed URL for page {page_number}: {url}")
    
    # Scrape the current page and extend the filtered data list
    try:
        filtered_data.extend(scrape_page(url, page_number))
    except Exception as e:
        print(f"Error scraping page {page_number}: {e}")

# Write the filtered data to the CSV file
with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:  # Open in write mode with utf-8 encoding
    writer = csv.writer(csv_file)
    for row in filtered_data:
        writer.writerow([row])

# Close the WebDriver
driver.quit()

print(f"CSV file '{csv_file_name}' has been updated successfully.")