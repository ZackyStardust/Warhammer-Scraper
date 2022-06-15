import os
os.environ['GH_TOKEN'] = "<fill with your token here>"
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
import requests

print("What is the name of the mini/box you are looking for? Be specific and clear in order not to find incorrent products.\n")
prodname = input()

browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

browser.get("https://versusgamecenter.pt/")
versus = []
versus.append("++ Versus Gamecenter ++")
browser.find_element(by=By.ID, value='lupa-search').click()
browser.find_element(by=By.ID, value='search').send_keys(prodname, Keys.RETURN)
time.sleep(10)
try:
    browser.find_element(by=By.XPATH, value='//div[@class="product-list-content"]/h3/a').click()
    time.sleep(10)
    versus.append(browser.find_element(by=By.XPATH, value='//div[@class="product-details-des"]/h3').text)
    versus.append(browser.find_element(by=By.XPATH, value='//div[@class="pricebox"]/span').text)
    versus.append("Disponibilidade:", browser.find_element(by=By.XPATH, value='//div[@class="availability mb-20"]/span').text)
except NoSuchElementException:
    versus.append("Product not found in store.")

browser.get("https://arenaporto.com/")

searchbar = browser.find_element(by=By.XPATH, value='//input[@class="ui-autocomplete-input"]')
searchbar.send_keys(prodname, Keys.RETURN)
time.sleep(10)

arenaporto = []
arenaporto.append("++ Arena Porto ++")
try:
    arenaporto.append(browser.find_element(by=By.XPATH, value='//div[@class="product-description"]/h2/a').text)
    arenaporto.append(browser.find_element(by=By.XPATH, value='//span[@class="price"]').text)
    browser.find_element(by=By.XPATH, value='//div[@class="product-description"]/h2/a').click()
    if browser.find_element(by=By.XPATH, value='//span[@id="product-availability"]'):
        arenaporto.append(browser.find_element(by=By.XPATH, value='//span[@id="product-availability"]').text)
except NoSuchElementException:
    arenaporto.append("Product not found in store.")

print("\n")
print(*versus, sep = "\n")
print("\n")
print(*arenaporto, sep = "\n")

browser.quit()
