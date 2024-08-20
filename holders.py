# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time
# import csv
# import os

# # Prompt the user to input the first page URL
# first_page_url = input("Please enter the URL of the first page to scrape: ")

# # Prompt the user to input the constant part of the URL for subsequent pages
# constant_url_part = input("Please enter the constant part of the URL for subsequent pages (e.g., 'https://solscan.io/token/7u6WirUYbf3kJdZQoPTCYjgU5rpVg21LuXLKmmCUpump?page='): ")

# # Prompt the user to input the starting and ending page numbers
# start_page = int(input("Please enter the starting page number: "))
# end_page = int(input("Please enter the ending page number: "))

# # Path to the ChromeDriver executable
# chrome_driver_path = r'C:\webdrivers\chromedriver.exe'  # Use raw string to avoid escape sequence issues

# # Initialize the Chrome WebDriver with the Service object
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# # Iterate over the range of page numbers
# for page_number in range(start_page, end_page + 1):
#     # Construct the URL for the current page
#     if page_number == start_page:
#         url = first_page_url
#     else:
#         url = f"{constant_url_part}{page_number}#holders"
    
#     # Open the webpage
#     driver.get(url)
    
#     # Wait for the content to load (adjust the selector as necessary)
#     try:
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'td'))
#         )
#     except Exception as e:
#         print(f"Error waiting for elements on page {page_number}: {e}")
#         continue
    
#     # Scroll down to ensure all dynamic content is loaded
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)  # Wait for additional content to load
    
#     # Get the page source (HTML content)
#     html_content = driver.page_source
    
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')
    
#     # Extract all the <td> elements with the specific class
#     td_elements = soup.find_all('td', class_='h-12 px-2 py-[10px] align-middle text-[14px] leading-[24px] font-normal text-neutral7 [&:has([role=checkbox])]:pr-0 border-t')
    
#     # Check if any <td> elements were found
#     if not td_elements:
#         print(f"No <td> elements found on page {page_number}.")
#         continue
    
#     # Define the class to include
#     include_class = 'text-link'
    
#     # Initialize a list to store the extracted <a> tag texts
#     a_tags_text = []
    
#     # Extract the first <a> tag within each <td> element and filter based on class
#     for td in td_elements:
#         a_tag = td.find('a', class_=include_class)
#         if a_tag:
#             a_tags_text.append(a_tag.get_text())
    
#     # Filter the list to include only the links at even indices
#     filtered_a_tags_text = [text for index, text in enumerate(a_tags_text) if index % 2 == 0]
    
#     # Append the filtered <a> tag texts to the existing CSV file
#     with open('output.csv', 'a', newline='') as csv_file:  # Open in append mode
#         writer = csv.writer(csv_file)
#         for text in filtered_a_tags_text:
#             writer.writerow([text])

# # Close the WebDriver
# driver.quit()

# print("CSV file has been updated successfully.")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv
import os

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
def scrape_page(url):
    # Open the webpage
    driver.get(url)
    
    # Wait for the content to load (adjust the selector as necessary)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'td'))
        )
    except Exception as e:
        print(f"Error waiting for elements on page {url}: {e}")
        return
    
    # Scroll down to ensure all dynamic content is loaded
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Wait for additional content to load
    
    # Get the page source (HTML content)
    html_content = driver.page_source
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract all the <td> elements with the specific class
    td_elements = soup.find_all('td', class_='h-12 px-2 py-[10px] align-middle text-[14px] leading-[24px] font-normal text-neutral7 [&:has([role=checkbox])]:pr-0 border-t')
    
    # Check if any <td> elements were found
    if not td_elements:
        print(f"No <td> elements found on page {url}.")
        return
    
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
    
    # Append the filtered <a> tag texts to the specified CSV file
    with open(csv_file_name, 'a', newline='', encoding='utf-8') as csv_file:  # Open in append mode with utf-8 encoding
        writer = csv.writer(csv_file)
        for text in filtered_a_tags_text:
            writer.writerow([text])

# Initialize a list to store all the filtered data
filtered_data = []

# Check if the constant URL part is empty
if not constant_url_part:
    # Scrape only the first page
    scrape_page(first_page_url)
else:
    # Iterate over the range of page numbers
    for page_number in range(start_page, end_page + 1):
        # Construct the URL for the current page
        if page_number == start_page:
            url = first_page_url
        else:
            url = f"{constant_url_part}{page_number}#holders"
        
        # Scrape the current page
        # scrape_page(url)
        filtered_data.extend(scrape_page(url, page_number))

# Close the WebDriver
driver.quit()

print(f"CSV file '{csv_file_name}' has been updated successfully.")