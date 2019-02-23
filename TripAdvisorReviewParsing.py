from bs4 import BeautifulSoup
import requests
import os

url = requests.get("https://www.tripadvisor.co.uk/Restaurant_Review-g186338-d5861005-Reviews-or20-Rice_Republic-London_England.html")
page_code = BeautifulSoup(url.content,"html.parser")
