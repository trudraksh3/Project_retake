import scrapy
import pandas as pd
page_limit = True

if page_limit:
    pages = 3
else:
    pages = 100

class EloSpider(scrapy.Spider):
    name = "elo"
    allowed_domains = ['https://www.exportleftovers.com/']
    start_urls = [f'https://www.exportleftovers.com/collections/men?page={i}' for i in range(1, pages + 1)]
    

    def parse(self, response):
        p_link = response.css('a.full-unstyled-link::attr(href)').extract()
        p_name=[text.strip() for text in response.css('a.full-unstyled-link::text').extract()]
        p_price=[text.strip() for text in response.css('span.price-item.price-item--regular::text').extract()]
        del p_name[1::2]
        del p_link[1::2]
        li2=[]
        for item in p_link:
            li2.append('https://www.exportleftovers.com'+item)
        Data_Scraped = pd.DataFrame(
            {'Product Name': p_name,
            'Product Price': p_price,
            'Product Link': li2
            })
        Data_Scraped.to_csv('C:/Users/rudra/OneDrive/Desktop/university/Semester 2/Webscrapping/retake/Project/Scrapy.csv',index=False,mode='a')
