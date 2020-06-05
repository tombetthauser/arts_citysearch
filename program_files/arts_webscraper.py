from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import time
import os

class SearchBot:
  def __init__(self, area="paris, texas"):
    self.area = area
    # self.driver = webdriver.Chrome()
    self.driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
    self.galleries_list = []
    self.galleries_queue = []
    self.galleries_dict = {}
    self.driver.get("https://maps.google.com")
    self.continue_search = True
    os.system('clear')
    print(f"\nNew SearchBot instantiated 🌱\nGoogle maps opened and ready to begin...")

  def search(self, area=None):
    area = area or self.area or input("\nPlease input search area to continue: ")
    self.search_google(area)
    # sleep(3)
    while (self.continue_search == True):
      self.retrieve_list()
      self.empty_queue()
      self.click_next()
    self.csv_export()
    print("\nEnd of search loop reached, search complete 👍\n")

  def sanitize_string(self, string):
    string_copy = string
    for char in ('(', ')', '"', "'"):
      string_copy = string_copy.replace(char, '')
    return string_copy
    
  def csv_export(self):
    print("\nInitiating csv_export function...")
    unix_time = int(time())
    file_name = f"data_{unix_time}.csv"
    os.system(f"touch {file_name}")
    for gallery_name in self.galleries_list:
      csv_string = f'"{self.sanitize_string(gallery_name)}",'
      for info_item in self.galleries_dict[gallery_name]:
        csv_string += f'"{self.sanitize_string(info_item)}",'
      csv_string += str(self.area)
      os.system(f"echo '{csv_string}' >> {file_name}")
    print(f"Function csv_export successfully completed ✓")

  def empty_queue(self):
    print('\nInitiating empty_queue function...')
    for gallery_name in self.galleries_queue:
      
      next_gallery_loaded = False
      while (next_gallery_loaded == False):
        try:
          xpath = f'//span[text()="{gallery_name}"]'
          element = self.driver.find_element_by_xpath(xpath)
          next_gallery_loaded = True
        except:
          pass
      element.click()
      # sleep(2)

      info = self.driver.find_elements_by_class_name("widget-pane-link")
      while (len(info) < 1):
        try:
          info = self.driver.find_elements_by_class_name("widget-pane-link")
        except:
          pass

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

      back_link_present = False
      while (back_link_present == False):
        try:
          back_link = self.driver.find_element_by_xpath("//span[text()='Back to results']")
          back_link_present = True
        except:
          pass
      back_link.click()

    self.galleries_queue = []
    print(f"Function empty_queue successfully completed ✓")

  def click_next(self):
    print(f"\nInitiating click_next function...")
    try:
      nextbutton_class = "n7lv7yjyC35__button-next-icon"
      next_button = self.driver.find_element_by_class_name(nextbutton_class)
      next_button.click()
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

  def retrieve_list(self):
    print(f"\nInitiating retrieve_list function call...")
    print(f"Current gallery_list count: {len(self.galleries_list)}\n")
    resultslist = self.driver.find_elements_by_css_selector(".section-result-title span")

    while (len(resultslist) < 1):
      try:
        resultslist = self.driver.find_elements_by_css_selector(".section-result-title span")
      except:
        pass
      
    for ele in resultslist:
      inner_text = self.driver.execute_script(
          "return arguments[0].innerText;", ele)
      self.galleries_queue.append(inner_text)
      self.galleries_list.append(inner_text)
      print(f"galleries_list: {len(self.galleries_list)} -- {inner_text}")

    print(f"Function retrieve_list successfully completed ✓")

SearchBot().search()
