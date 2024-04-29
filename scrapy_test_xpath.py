import scrapy
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
url = 'https://www.redfin.com/PA/Pittsburgh/1539-Park-Blvd-15216/home/74699966'
# Configure Selenium options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems


webdriver_path = 'chromedriver.exe'
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)



class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.redfin.com/PA/Pittsburgh/937-Roland-Rd-15221/home/74605887'
    ]
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        

    def parse(self, response):
        self.driver.get(response.url)
        # Extracting statsValue using XPath
        stats_value = response.xpath('//div[@class="statsValue"]/text()').get()

        yield {
            'stats_value': stats_value.strip() if stats_value else None
        }
            