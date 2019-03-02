import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# sys.path.append(os.path.dirname(__file__))
# print(os.path.dirname(__file__))
#
# import ta_restaurant_info_parser as rtp

def get_review_selector(driver):
    review_selector = driver.find_elements_by_xpath('//div[@class = "reviewSelector"]')
    return review_selector

def get_ind_bubble_rating(ind_review_selector):
    ind_bubble_rating = ind_review_selector.find_element_by_xpath('.//span[contains(@class, "ui_bubble_rating")]')
    return ind_bubble_rating.get_attribute('class')

def get_ind_review_date(ind_review_selector):
    ind_review_date = ind_review_selector.find_element_by_xpath('.//span[contains(@class, "ratingDate")]')
    return ind_review_date.get_attribute('title')

def get_ind_review_content(ind_review_selector):
    ind_review_content= rs.find_element_by_xpath('.//p[contains(@class, "partial_entry")]')
    return ind_review_content.text

def get_ind_review_stay_date(ind_review_selector):
    ind_review_stay_date= rs.find_element_by_xpath('.//div[contains(@class, "reviews_stay_date")]')
    return ind_review_stay_date.text

def click_more(driver):
    try:
        elem_more = driver.find_element_by_xpath('//span[@class="taLnk ulBlueLinks"]').click()
        print('Clicked')
    except:
        print('Already Clicked')

def click_next(driver):
    elem_next = driver.find_element_by_xpath('//a[@class="nav next taLnk ui_button primary"]').click()
    # elem_next = driver.find_element_by_tag_name("Next").click()


options = Options()
# options.add_argument('--start-maximized')
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument("--window-size=800x600")
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=options)

driver.get('https://www.tripadvisor.co.uk/Restaurant_Review-`g186338-d5861005-Reviews-Rice_Republic-London_England.html')


# click_more(driver)
# print(len(get_review_selector(driver)))
# for rs in get_review_selector(driver):
#     print('scrap comment')
#     ind_rating = get_ind_bubble_rating(rs)
#     ind_review_date = get_ind_review_date(rs)
#     # ind_review_content = get_ind_review_content(rs)
#     ind_stay_date = get_ind_review_stay_date(rs)
#     print(ind_rating)
#     print(ind_review_date)
#     print(ind_stay_date)

count = 0
while True:
    if count > 50:
        break
    else:
        # try:
        #     print('check next button')
        #     driver.find_elements_by_xpath('//a[@class, "nav next ui_button primary disabled"]')
        #     break
        # except:
        click_more(driver)
        print(len(get_review_selector(driver)))
        for rs in get_review_selector(driver):
            print('scrap comment')
            ind_rating = get_ind_bubble_rating(rs)
            ind_review_date = get_ind_review_date(rs)
            ind_review_content = get_ind_review_content(rs)
            ind_stay_date = get_ind_review_stay_date(rs)
            # print(ind_rating)
            print(ind_review_date)
            # print(ind_stay_date)
        click_next(driver)
        time.sleep(0.5)

driver.close()
