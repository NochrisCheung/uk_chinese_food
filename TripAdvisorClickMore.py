# import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

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
# elem = driver.find_elements_by_class_name('taLnk ulBlueLinks')
# driver.implicitly_wait(5)
# elem = driver.find_element_by_xpath("//span[@class='taLnk ulBlueLinks']").click()


elem = driver.find_element_by_xpath("//span[@class='taLnk ulBlueLinks']")
# driver.find_element_by_xpath("//*[contains(text(), 'More')]").click()
# driver.switch_to_frame(elem)
# print(elem)
# elem.move_to_element()
# elem.send_keys(Keys.RETURN)
action = webdriver.common.action_chains.ActionChains(driver)
#
# for i in range(-15, 0):

print(elem.location['x'], elem.location['y'])
print(elem.size['width'],elem.size['height'])
print(elem.text)
# action.move_to_element_with_offset(elem, 0 , -elem.size['height']/2 + 1).click().perform()
try:
    for j in range(-100, 0):
        print(0, j)
        action.move_to_element_with_offset(elem, 0, j).click().perform()

except Exception:
        element = driver.find_elements_by_xpath("//p[@class='partial_entry']")
        i = 1
        for e in element:
                print (str(i) + '\n')
                i = i+1
                print(e.text.encode("utf8"))


# elem.click()


# action.click()
# action.perform()

# elem = driver.find_element_by_xpath("//span[text()='More']")


# elem = driver.find_element_by_xpath("//span[text()='More']").click()
# driver.execute_script('argument[0].click()', elem)
# except Exception:
#     driver.save_screenshot('screenshot.png')

# driver.close()
