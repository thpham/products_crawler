# -*- coding: utf-8 -*-

# Scrapy settings for products_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'products_crawler'

SPIDER_MODULES = ['products_crawler.spiders']
NEWSPIDER_MODULE = 'products_crawler.spiders'

SPLASH_URL = 'http://127.0.0.1:8050/'
SPLASH_COOKIES_DEBUG = True
SPLASH_LOG_400 = True
DOWNLOADER_MIDDLEWARES = {
  'scrapy_splash.SplashCookiesMiddleware': 723,
  'scrapy_splash.SplashMiddleware': 725,
  'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
  'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'products_crawler (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# output data format
FEED_FORMAT = "csv"
FEED_URI = "tmp/%(name)s.csv"

# Enable logs to see scrapy logs in command line
LOG_ENABLED=False

# Max deptth to crawl
DEPTH_LIMIT=4
FEED_EXPORT_FIELDS=["product_name", "product_descr", "product_quantity", "price", "image_url", "source"]
