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

time.sleep(3)

searchdiv = driver.find_element_by_id("search")
links = searchdiv.find_elements_by_tag_name("a")
links[0].click()

time.sleep(3)

driver.quit()