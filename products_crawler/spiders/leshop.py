# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  raw_html.encode('ascii','ignore')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext=cleantext.strip()
  cleantext=re.sub('\s+',' ',cleantext)
  return cleantext

class LeShopSpider(CrawlSpider):
    name = 'leshop'
    def __init__(self, product='apple', domain=None, *args, **kwargs):
        super(LeShopSpider, self).__init__(*args, **kwargs)
        self.product_name=product.lower()
        self.product_name=re.sub("[^ a-zA-Z0-9]+", "", self.product_name)
        self.search_url='https://www.leshop.ch/en/search?query='+self.product_name

        self.allowed_domains = ['www.leshop.ch','supermarket.leshop.ch']
        self.start_urls = [self.search_url]

    rules = (
          Rule(LinkExtractor(allow=(), tags=('a'),attrs=('href'),restrict_css=('.pagnNext',)),
               callback="parse_items",
               follow=True),)

    def parse_start_url(self,response):
        request=SplashRequest(self.search_url,
                              callback=self.parse_items,
                              args={
                                  # optional; parameters passed to Splash HTTP API
                                  'wait': 2.5,
                                  # 'url' is prefilled from request url
                                  # 'http_method' is set to 'POST' for POST requests
                                  # 'body' is set to request body for POST requests
                              })
        return request
    
    def parse_items(self, response):
      print("Processing...", response.real_url, response.url)
      name=[]
      description=[]
      quantity=[]
      price=[]
      image=[]
      items = response.xpath('//li[@class="item"]')
      for item in items:
        item_name_select=item.xpath('.//*[contains(@id, "name")]/text()')
        item_name = item_name_select.extract_first()
        #print(item_name)
        item_descr_select=item.xpath('.//*[contains(@id, "description")]//span/text()')
        item_descr = item_descr_select.extract_first()
        #print(item_descr)
        item_quantity_select=item.xpath('.//*[contains(@class, "weight-priceUnit")]//span/span/text()')
        item_quantity = item_quantity_select.extract_first()
        #print(item_quantity)
        item_price_select=item.xpath('.//*[contains(@id, "current-price")]/text()')
        item_price=item_price_select.extract_first()
        #print(cleanhtml(item_price)+' CHF')
        item_image_select=item.xpath('.//img/@src | .//img/@data-src')
        item_image = item_image_select.extract_first()
        #print(item_image)
        
        if((item_name or item_descr) and item_quantity and item_price and item_image ):
          name.append(cleanhtml(item_name))
          description.append(cleanhtml(item_descr))
          quantity.append(cleanhtml(item_quantity))
          price.append(cleanhtml(item_price)+' CHF')
          image.append(cleanhtml(item_image))
      print('Result Counts: ',len(name))
      
      for item in zip(name,description,quantity,price,image):
          scraped_info = {
              'product_name' : item[0],
              'product_descr' : item[1],
              'product_quantity' : item[2],
              'price' : item[3],
              'image_url' : item[4],
              'source': 'leshop.ch' 
              }
          yield scraped_info