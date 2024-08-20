# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time

# # Initialize undetected Chrome WebDriver with options
# options = uc.ChromeOptions()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# # You might try avoiding headless mode to reduce detection risk
# # options.add_argument("--headless")  # Try without this

# driver = uc.Chrome(options=options)

# try:
#     # Load the webpage
#     url = 'https://dexscreener.com/solana/9tzygod5xc4tnzqh3pbnkfgv9fv1ngwo5uxfejpcyqj'
#     driver.get(url)

#     # Wait for the page to fully load and display the content
#     time.sleep(10)  # Increase this if necessary

#     # Wait for the div with class 'custom-1pvtqh7' to be present
#     WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'custom-1pvtqh7'))
#     )

#     # Parse the HTML using BeautifulSoup
#     html_content = driver.page_source
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Find the div with class 'custom-1pvtqh7'
#     div = soup.find('div', class_='custom-1pvtqh7')

#     # Iterate through all tr and td tags within this div
#     if div:
#         rows = div.find_all('tr')
#         for row in rows:
#             cells = row.find_all('td')
#             for cell in cells:
#                 # Find all a tags within each cell
#                 links = cell.find_all('a')
#                 for link in links:
#                     # Print the href attribute of each a tag
#                     print(link.get('href'))
#     else:
#         print("Div with class 'custom-1pvtqh7' not found")

# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     # Ensure the WebDriver is properly closed
#     driver.quit()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Initialize undetected Chrome WebDriver
options = uc.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = uc.Chrome(options=options)

try:
    # Load the webpage
    url = 'https://dexscreener.com/solana/9tzygod5xc4tnzqh3pbnkfgv9fv1ngwo5uxfejpcyqj'
    driver.get(url)

    # Wait for the div with class 'custom-1pvtqh7' to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'custom-1pvtqh7'))
    )

    # Parse the HTML using BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the div with class 'custom-1pvtqh7'
    div = soup.find('div', class_='custom-1pvtqh7')

    # Iterate through all tr and td tags within this div
    if div:
        rows = div.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            for cell in cells:
                # Find all a tags within each cell
                links = cell.find_all('a')
                for link in links:
                    # Print the href attribute of each a tag
                    print(link.get('href'))
    else:
        print("Div with class 'custom-1pvtqh7' not found")

except Exception as e:
    print(f"Error: {e}")

finally:
    try:
        # Ensure the WebDriver is properly closed
        driver.quit()
    except Exception as e:
        print(f"Error during driver.quit(): {e}")