from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lxml import etree

url = 'http://www.dangdang.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximsize_window()