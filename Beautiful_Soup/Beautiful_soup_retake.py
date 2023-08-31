from urllib import request as req
from bs4 import BeautifulSoup as BS
import pandas as pd
import re
import time

limit=100
p_name=[]
p_link=[]
p_price=[]
for p in range(1,limit+1):
    time.sleep(1)
    print(p)
    url='https://www.exportleftovers.com/collections/men?page='+str(p)
    html = req.urlopen(url)
    bs = BS(html.read(), 'html.parser')
    t1=bs.find_all('a' ,attrs={'class':'full-unstyled-link'})
    t2=bs.find_all('span' ,attrs={'class':'price-item price-item--regular'})
    t3=bs.find_all('a' ,attrs={'class':'full-unstyled-link'},href=True)
    for item in t1:
        p_name.append(item.get_text(strip=True))
    for item in t2:
        p_price.append(item.get_text(strip=True))
    for item in t3:
        p_link.append('https://www.exportleftovers.com'+item['href'])
del p_name[1::2]
del p_link[1::2]

Data_Scraped = pd.DataFrame(
    {'Product Name': p_name,
     'Product Price': p_price,
     'Product Link': p_link
    })
Data_Scraped.to_csv('C:/Users/rudra/OneDrive/Desktop/university/Semester 2/Webscrapping/retake/Project/bsoup.csv',index=False)
