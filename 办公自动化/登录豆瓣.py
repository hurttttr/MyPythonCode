import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.douban.com/'
dirver = webdriver.Chrome()
dirver.get(url)
dirver.implicitly_wait(5)#隐式等待
dirver.maximize_window()

dirver.switch_to_frame(0)
dirver.find_element_by_xpath('//*[@class="account-body-tabs"]/ul/li[2]').click()
dirver.find_element_by_name('username').send_keys('')
elem = dirver.find_element_by_name('password')
elem.send_keys('')
elem.send_keys(Keys.RETURN)

time.sleep(10)
dirver.quit()