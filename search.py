from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from getpass import getpass
import os

class SearchBot:
  def __init__(self, area=None):
    self.area = area
    self.driver = webdriver.Chrome()
    self.galleries_list = []
    self.driver.get("https://maps.google.com")
    self.continue_search = True
    os.system('clear')
    print(f"\nNew SearchBot instantiated 🌱\nGoogle maps opened and ready to begin...")
    sleep(2)

  def check_next(self):
    print("\nChecking for existance of next button...")
    try:
      self.driver.find_element_by_class_name("n7lv7yjyC35__button-next-icon")
      self.continue_search = True
      print(f"Status of self.continue_search: {self.continue_search}")
      print(f"Function check_next successfully completed ✓")
      return True
    except:
      self.continue_search = False
      print(f"Status of self.continue_search: {self.continue_search}")
      print(f"Function check_next successfully completed ✓")
      return False

  def click_next(self):
    print(f"\nInitiating click_next function...")
    try:
      nextbutton_class = "n7lv7yjyC35__button-next-icon"
      next_button = self.driver.find_element_by_class_name(nextbutton_class)
      next_button.click()
    except:
      self.continue_search = False
      print(f"Function click_next successfully completed –– no next found ☓")
    sleep(3)

  def search_google(self, area=None):
    area = area or self.area or input("\nPlease input search area to continue: ")
    print(f"\nInitiating search_google function with '{area}' for search area...")
    login_name = self.driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]"
    )
    login_name.send_keys(f"art gallery, {area}")
    login_name.send_keys(Keys.RETURN)
    print(f"Function search_google successfully completed ✓")
    sleep(3)

  def retrieve_list(self):
    print(f"\nInitiating retrieve_list function call...")
    print(f"Current gallery_list count: {len(self.galleries_list)}\n")
    classname = "section-result-title-container"
    resultslist = self.driver.find_elements_by_css_selector(".section-result-title span")
    for ele in resultslist:
      inner_text = self.driver.execute_script("return arguments[0].innerText;", ele)
      self.galleries_list.append(ele)
      print(f"galleries_list: {len(self.galleries_list)} -- {inner_text}")
    print(f"Function retrieve_list successfully completed ✓")

testbot = SearchBot()
testbot.search_google("San Francisco, CA")

while (testbot.continue_search == True):
  # print(testbot.continue_search)
  testbot.retrieve_list()
  testbot.click_next()

print("\nWhile loop exited, search complete 👍\n")