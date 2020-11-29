from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "./program_files/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://google.com")
print(driver.title)

search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search.send_keys("test")
search.send_keys(Keys.RETURN)

# driver.quit()

# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from time import time
# import os