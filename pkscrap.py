

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time
# import csv

# # Prompt the user to input the URL to scrape
# url = input("Please enter the URL to scrape: ")

# # Prompt the user to input the name of the CSV file to be created
# csv_file_name = input("Please enter the name of the CSV file to be created (e.g., 'output.csv'): ")

# # Path to the ChromeDriver executable
# chrome_driver_path = r'C:\webdrivers\chromedriver.exe'  # Use raw string to avoid escape sequence issues

# # Initialize the Chrome WebDriver with the Service object
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# # Function to scrape the page
# def scrape_page(url):
#     # Open the webpage
#     driver.get(url)
    
#     # Wait for the content to load (adjust the selector as necessary)
#     try:
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'tr.css-15iar3s'))
#         )
#     except Exception as e:
#         print(f"Error waiting for elements on page {url}: {e}")
#         return []
    
#     # Scroll down to ensure all dynamic content is loaded
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)  # Wait for additional content to load
    
#     # Get the page source (HTML content)
#     html_content = driver.page_source
    
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')
    
#     # Extract all the <tr> elements with the specific class
#     tr_elements = soup.find_all('tr', class_='css-15iar3s')
    
#     # Check if any <tr> elements were found
#     if not tr_elements:
#         print(f"No <tr> elements found on page {url}.")
#         return []
    
#     # Initialize a list to store the extracted <a> tag texts
#     a_tags_text = []
    
#     # Extract the <a> tags within each <tr> element and filter based on class
#     for tr in tr_elements:
#         a_tag = tr.find('a', class_='css-19toqs6')
#         if a_tag:
#             a_tags_text.append(a_tag.get_text())
    
#     return a_tags_text

# # Scrape the provided URL
# filtered_data = scrape_page(url)

# # Append the filtered <a> tag texts to the specified CSV file
# with open(csv_file_name, 'a', newline='', encoding='utf-8') as csv_file:  # Open in append mode with utf-8 encoding
#     writer = csv.writer(csv_file)
#     for text in filtered_data:
#         writer.writerow([text])

# # Close the WebDriver
# driver.quit()

# print(f"CSV file '{csv_file_name}' has been updated successfully.")


# # above code works but gives all a tags
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time
# import csv

# # Prompt the user to input the URL to scrape
# url = input("Please enter the URL to scrape: ")

# # Prompt the user to input the name of the CSV file to be created
# csv_file_name = input("Please enter the name of the CSV file to be created (e.g., 'output.csv'): ")

# # Path to the ChromeDriver executable
# chrome_driver_path = r'C:\webdrivers\chromedriver.exe'  # Use raw string to avoid escape sequence issues

# # Initialize the Chrome WebDriver with the Service object
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# # Function to scrape the page
# def scrape_page(url):
#     # Open the webpage
#     driver.get(url)
    
#     # Wait for the content to load (adjust the selector as necessary)
#     try:
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'tr.css-15iar3s'))
#         )
#     except Exception as e:
#         print(f"Error waiting for elements on page {url}: {e}")
#         return []
    
#     # Scroll down to ensure all dynamic content is loaded
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)  # Wait for additional content to load
    
#     # Get the page source (HTML content)
#     html_content = driver.page_source
    
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')
    
#     # Extract all the <tr> elements with the specific class
#     tr_elements = soup.find_all('tr', class_='css-15iar3s')
    
#     # Check if any <tr> elements were found
#     if not tr_elements:
#         print(f"No <tr> elements found on page {url}.")
#         return []
    
#     # Initialize a list to store the extracted <a> tag texts
#     a_tags_text = []
    
#     # Extract the <a> tags within each <tr> element and filter based on class
#     for tr in tr_elements:
#         a_tag = tr.find('a', class_='css-19toqs6')
#         if a_tag:
#             a_tags_text.append(a_tag.get_text())
    
#     return a_tags_text

# # Function to remove duplicates from the list
# def remove_duplicates(data_list):
#     return list(set(data_list))

# # Initialize a set to store all the unique data
# unique_data = set()

# # Run the scraping loop for 5 minutes (300 seconds)
# start_time = time.time()
# while (time.time() - start_time) < 300:
#     # Scrape the provided URL
#     new_data = scrape_page(url)
    
#     # Remove duplicates from the new data
#     new_data = remove_duplicates(new_data)
    
#     # Add the new data to the unique data set
#     unique_data.update(new_data)
    
#     # Wait for 1 second before the next iteration
#     time.sleep(1)

# # Append the unique data to the specified CSV file
# with open(csv_file_name, 'a', newline='', encoding='utf-8') as csv_file:  # Open in append mode with utf-8 encoding
#     writer = csv.writer(csv_file)
#     for text in unique_data:
#         writer.writerow([text])

# # Close the WebDriver
# driver.quit()

# print(f"CSV file '{csv_file_name}' has been updated successfully.")

# # above code works but gives all a tags waits 5min

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time
# import csv

# # Prompt the user to input the URL to scrape
# url = input("Please enter the URL to scrape: ")

# # Prompt the user to input the name of the CSV file to be created
# csv_file_name = input("Please enter the name of the CSV file to be created (e.g., 'output.csv'): ")

# # Path to the ChromeDriver executable
# chrome_driver_path = r'C:\webdrivers\chromedriver.exe'  # Use raw string to avoid escape sequence issues

# # Initialize the Chrome WebDriver with the Service object
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# # Function to scrape the page
# def scrape_page(url):
#     # Open the webpage
#     driver.get(url)
    
#     # Wait for the content to load (adjust the selector as necessary)
#     try:
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'tr.css-15iar3s'))
#         )
#     except Exception as e:
#         print(f"Error waiting for elements on page {url}: {e}")
#         return []
    
#     # Scroll down to ensure all dynamic content is loaded
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)  # Wait for additional content to load
    
#     # Get the page source (HTML content)
#     html_content = driver.page_source
    
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')
    
#     # Extract all the <tr> elements with the specific class
#     tr_elements = soup.find_all('tr', class_='css-15iar3s')
    
#     # Check if any <tr> elements were found
#     if not tr_elements:
#         print(f"No <tr> elements found on page {url}.")
#         return []
    
#     # Initialize a list to store the extracted <a> tag texts
#     a_tags_text = []
    
#     # Extract the <a> tags within each <tr> element and filter based on class
#     for tr in tr_elements:
#         a_tag = tr.find('a', class_='css-19toqs6')
#         if a_tag:
#             a_tags_text.append(a_tag.get_text())
    
#     return a_tags_text

# # Function to remove duplicates from the list
# def remove_duplicates(data_list):
#     return list(set(data_list))

# # Initialize a set to store all the unique data
# unique_data = set()

# # Run the scraping loop for 1 minute (60 seconds)
# start_time = time.time()
# while (time.time() - start_time) < 60:
#     # Scrape the provided URL
#     new_data = scrape_page(url)
    
#     # Remove duplicates from the new data
#     new_data = remove_duplicates(new_data)
    
#     # Add the new data to the unique data set
#     unique_data.update(new_data)
    
#     # Wait for 1 second before the next iteration
#     time.sleep(1)

# # Append the unique data to the specified CSV file
# with open(csv_file_name, 'a', newline='', encoding='utf-8') as csv_file:  # Open in append mode with utf-8 encoding
#     writer = csv.writer(csv_file)
#     for text in unique_data:
#         writer.writerow([text])

# # Close the WebDriver
# driver.quit()

# print(f"CSV file '{csv_file_name}' has been updated successfully.")

# above for 1min

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

# Prompt the user to input the URL to scrape
url = input("Please enter the URL to scrape: ")

# Prompt the user to input the name of the CSV file to be created
csv_file_name = input("Please enter the name of the CSV file to be created (e.g., 'output.csv'): ")

# Path to the ChromeDriver executable
chrome_driver_path = r'C:\webdrivers\chromedriver.exe'  # Use raw string to avoid escape sequence issues

# Initialize the Chrome WebDriver with the Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Function to scrape the page
def scrape_page(url):
    # Refresh the webpage to get the latest data
    driver.get(url)
    
    # Wait for the content to load (adjust the selector as necessary)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'tr.css-15iar3s'))
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
    
    # Extract all the <tr> elements with the specific class
    tr_elements = soup.find_all('tr', class_='css-15iar3s')
    
    # Check if any <tr> elements were found
    if not tr_elements:
        print(f"No <tr> elements found on page {url}.")
        return []
    
    # Initialize a list to store the extracted <a> tag texts
    a_tags_text = []
    
    # Extract the <a> tags within each <tr> element and filter based on class
    for tr in tr_elements:
        a_tag = tr.find('a', class_='css-19toqs6')
        if a_tag:
            a_tags_text.append(a_tag.get_text())
    
    return a_tags_text

# Initialize a set to store all the unique data
unique_data = set()

# Run the scraping loop for 1 minute (60 seconds)
start_time = time.time()
while (time.time() - start_time) < 30:
    # Scrape the provided URL
    new_data = scrape_page(url)
    
    # Filter out duplicates by checking against the unique_data set
    new_unique_data = [data for data in new_data if data not in unique_data]
    
    # Add the new unique data to the unique data set
    unique_data.update(new_unique_data)
    
    # Append the new unique data to the specified CSV file
    with open(csv_file_name, 'a', newline='', encoding='utf-8') as csv_file:  # Open in append mode with utf-8 encoding
        writer = csv.writer(csv_file)
        for text in new_unique_data:
            writer.writerow([text])
    
    # Wait for 1 second before the next iteration
    time.sleep(1)

# Close the WebDriver
driver.quit()

print(f"CSV file '{csv_file_name}' has been updated successfully.")
