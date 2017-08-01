#coding: UTF-8

from selenium import webdriver
import re

browser = webdriver.Chrome()
url = "https://www.google.com"
browser.get(url)

inputs = browser.find_element_by_name('q')
inputs.send_keys('iphone8')
button = browser.find_element_by_name('btnK')
button.click()