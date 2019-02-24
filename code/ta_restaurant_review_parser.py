import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

sys.path.append(os.path.dirname(__file__))
print(os.path.dirname(__file__))

import ta_restaurant_info_parser as rtp

driver = webdriver.Chrome()
driver.get('https://www.tripadvisor.co.uk/Restaurant_Review-g186338-d5861005-Reviews-Rice_Republic-London_England.html')
rtp.click_more(driver)
#
# review_list = driver.find_element_by_xpath('//div[contains(@id, "location_reviews_list")]')
# review_list
