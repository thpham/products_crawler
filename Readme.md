# Products-Crawler

Products-Crawler is a python web crawler developed using scrapy framework. It has 2 spiders for crawling the search results from leshop.ch, coopathome.ch. The crawler extract the product names, description, quantity, price, image urls and source, and then stores them in a csv file named `results.csv`. It can be useful for comparing the price of a particular product between different e-commerce websites.

## Installing Dependencies

- Install pip using `pip install -r requirements.txt`
- Run splash headless browser with `docker run --rm -d -p 8050:8050 scrapinghub/splash`

## Running Crawler
1. Open command line
2. Go to root directory i.e. Products-Crawler
3. Run `python run_crawler.py`
4. Enter the search keyword (a product or brand name) in command line.
5. See the crawling results in `results.csv` file
