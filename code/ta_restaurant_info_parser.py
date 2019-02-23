# import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def click_more(driver):
    try:
        elem_more = driver.find_element_by_xpath('//span[@class="taLnk ulBlueLinks"]').click()
    except:
        print('Already Clicked')
    
def click_next(driver):
    elem_next = driver.find_element_by_xpath('//a[@class="nav next taLnk ui_button primary"]').click()

def get_current_page_numer(driver):
    current_page_num = driver.find_element_by_xpath('//a[contains(@class,"current") and contains(@class,"page")]')
    return current_page_num.get_attribute('data-page-number')

def get_restaurant_name(driver):
    restaurant_name = driver.find_element_by_xpath('//h1[@class = "ui_header h1"]')
    return restaurant_name.get_attribute('innerHTML')

def get_total_grade_bubbles(driver):
    total_rating_bubbles = driver.find_element_by_xpath('//span[contains(@class,"bubble_rating")]')
    return total_rating_bubbles.get_attribute('alt')

def get_review_count(driver):
    review_count = driver.find_element_by_xpath('//span[contains(@class,"reviewCount")]')
    return review_count.get_attribute('innerHTML')

def get_restaurant_ranking(driver):
    elem_popularity = driver.find_element_by_xpath('//span[contains(@class,"header_popularity popIndexValidation")]')
    return(elem_popularity.text)

def get_price_and_tags(driver):
    restaurant_tags = driver.find_element_by_xpath('//div[contains(@class, "restaurants") and contains(@class, "tagsContainer")]')
    detail_tags = restaurant_tags.find_elements_by_tag_name('a')

    price = []
    tags = []
    for t in detail_tags:
        if '£'.decode('utf8') in t.text:
            price = t.text
        else:
            tags = tags + [t.text]
    return price, tags

def get_opening_hours(driver):
    elem_opening_hours = driver.find_elements_by_xpath('//span[contains(@class, "LocationHours")]')
    opening_hours = []
    for op in elem_opening_hours:
        if any(char.isdigit() for  char in op.text):
                opening_hours = op.text
                break

    return opening_hours

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


# chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'
# PATH = '/path/to/chromedriver'

driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome(chrome_options=chrome_options)
#
# js = JavaScriptExecutor()

# PATH = '/path/to/chromedriver'
#
# driver = webdriver.PhantomJS()
# driver.set_window_size(1920,1080)
# try:
driver.get('https://www.tripadvisor.co.uk/Restaurant_Review-g186338-d5861005-Reviews-Rice_Republic-London_England.html')

def get_restaurant_ranking(driver):
    elem_popularity = driver.find_element_by_xpath('//span[contains(@class,"header_popularity popIndexValidation")]')
    return(elem_popularity.text)
# driver.close()