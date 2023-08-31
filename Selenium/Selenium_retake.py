from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import re
import time
import pandas as pd

p_name = []
p_price = []
p_link = []

#setting chrome driver path
# Init:
driver=webdriver.Chrome("C:/chromedriver.exe")

url = 'https://www.exportleftovers.com/collections/men?page=1'

#calling the website url
driver.get(url)

page_limit = False

if page_limit == True:
    max_pages = 3
else: max_pages = 100

for i in range(2,max_pages+1):
    
    time.sleep(1)
    price_elements = driver.find_elements(By.CSS_SELECTOR, "span.price-item.price-item--regular")
    price_texts = [element.text.strip() for element in price_elements]
    name_elements =driver.find_elements(By.CSS_SELECTOR, "a.full-unstyled-link")
    name_texts = [element.text.strip() for element in name_elements]
    name_texts=name_texts[1::2]
    link_elements = driver.find_elements(By.CSS_SELECTOR, "a.full-unstyled-link")
    link_texts = [element.get_attribute('href')for element in link_elements]
    link_texts=link_texts[1::2]


    # using time.sleep for a slight delay in code to interact and find all the elements
    time.sleep(1)
    driver.get('https://www.exportleftovers.com/collections/men?page='+str(i))
    for item in price_texts:
        p_price.append(item)
    for item in name_texts:
        p_name.append(item)
    for item in link_texts:
        p_link.append(item)

Data_Scraped = pd.DataFrame(
    {'Product Name': p_name,
    'Product Price': p_price,
    'Product Link': p_link
    })
Data_Scraped.to_csv('C:/Users/rudra/OneDrive/Desktop/university/Semester 2/Webscrapping/retake/Project/Selenium .csv',index=False)
driver.close()