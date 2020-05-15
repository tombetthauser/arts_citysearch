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
    self.galleries_queue = []
    self.galleries_dict = {}
    self.driver.get("https://maps.google.com")
    self.continue_search = True
    os.system('clear')
    print(f"\nNew SearchBot instantiated 🌱\nGoogle maps opened and ready to begin...")
    sleep(2)

  def search(self, area=None):
    area = area or self.area or input(
        "\nPlease input search area to continue: ")
    self.search_google("San Francisco, CA")
    while (self.continue_search == True):
      self.retrieve_list()
      self.empty_queue()
      self.click_next()
    print("\nEnd of search loop reached, search complete 👍\n")

  def empty_queue(self):
    print('\nInitiating empty_queue function...')
    for gallery_name in self.galleries_queue:
      xpath = f'//span[text()="{gallery_name}"]'
      element = self.driver.find_element_by_xpath(xpath)
      element.click()
      sleep(2)

      info = self.driver.find_elements_by_class_name("widget-pane-link")
      print(f"\nScraping info for {gallery_name}...")
      print(len(info))
      self.galleries_dict[gallery_name] = []
      for ele in list(info):
        inner_text = self.driver.execute_script("return arguments[0].innerText;", ele)
        if inner_text != '':
          self.galleries_dict[gallery_name].append(inner_text)
        print(f"'{inner_text}' fetched from gallery")
      try:
        description_ele = self.driver.find_element_by_css_selector(".section-editorial-quote span")
        description = self.driver.execute_script("return arguments[0].innerText;", description_ele)
      except:
        description = 'no description'
      self.galleries_dict[gallery_name].append(description)
      print("\nGallery info collected:")
      for ele in self.galleries_dict[gallery_name]:
        print(f"– {ele}")
      print(f"\nall info added for {gallery_name} ✓")

      back_link = self.driver.find_element_by_xpath("//span[text()='Back to results']")
      back_link.click()
      sleep(2)
    self.galleries_queue = []
    print(f"Function empty_queue successfully completed ✓")

  def click_next(self):
    print(f"\nInitiating click_next function...")
    try:
      nextbutton_class = "n7lv7yjyC35__button-next-icon"
      next_button = self.driver.find_element_by_class_name(nextbutton_class)
      next_button.click()
      sleep(3)
    except:
      self.continue_search = False
      print(f"Function click_next successfully completed –– no next found ☓")

  def search_google(self, area=None):
    area = area or self.area or input(
        "\nPlease input search area to continue: ")
    print(
        f"\nInitiating search_google function with '{area}' for search area...")
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
    resultslist = self.driver.find_elements_by_css_selector(
        ".section-result-title span")
    for ele in resultslist:
      # append with xcode rather than element object
      inner_text = self.driver.execute_script(
          "return arguments[0].innerText;", ele)
      self.galleries_queue.append(inner_text)
      self.galleries_list.append(ele)
      print(f"galleries_list: {len(self.galleries_list)} -- {inner_text}")
    print(f"Function retrieve_list successfully completed ✓")

testbot = SearchBot()
testbot.search("San Francisco, CA")
