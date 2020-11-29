from selenium import webdriver
PATH = "./program_files/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://google.com")
print(driver.title)
driver.quit()

# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from time import time
# import os