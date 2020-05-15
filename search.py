from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from getpass import getpass


class SearchBot:
  def __init__(self, area=None):
    self.area = area
    self.driver = webdriver.Chrome()
    self.driver.get("https://maps.google.com")
    self.galleries_list = []
    sleep(2)

  def search_google(self, area=None):
    # fill and runin search
    area = area or self.area or input("Please input search area to continue: ")
    login_name = self.driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]"
    )
    login_name.send_keys(f"art gallery, {area}")
    login_name.send_keys(Keys.RETURN)
    sleep(3)

  def retrieve_list(self):
    classname = "section-result-title-container"
    resultslist = self.driver.find_elements_by_css_selector(".section-result-title span")
    for ele in resultslist:
      inner_text = self.driver.execute_script("return arguments[0].innerText;", ele)
      self.galleries_list.append(ele)
      print(f"galleries_list: {len(self.galleries_list)} -- {inner_text}")
    # # fill in password
    # login_pass = self.driver.find_element_by_xpath(
    #     "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input"
    # ).send_keys(self.password)
    # sleep(1)

  #   # delete password from temporary variable
  #   self.password = None

  #   # click log in button
  #   self.driver.find_element_by_xpath(
  #       "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]"
  #   ).click()
  #   sleep(3)

  #   # click not now button to close pop up modal
  #   self.driver.find_element_by_xpath(
  #       "/html/body/div[4]/div/div/div[3]/button[2]"
  #   ).click()
  #   sleep(1)

  # def fetch_followers(self):  # not yet working
  #   # click users profile link
  #   self.driver.find_element_by_xpath(
  #       "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img"
  #   ).click()
  #   sleep(1)

  #   # click followers link
  #   self.driver.find_element_by_xpath(
  #       "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"
  #   ).click()
  #   sleep(1)

  #   # scroll to bottom of followers modal
  #   modal_bottom = self.driver.find_element_by_xpath(
  #       "/html/body/div[4]/div/div[2]/ul/div")
  #   followers_ul = self.driver.find_element_by_xpath(
  #       "/html/body/div[4]/div/div[2]/ul")
  #   followers_ul.click()

    # self.driver.execute_script("arguments[0].scrollIntoView()", modal_bottom)
    # while (True):
    #   self.driver.execute_script("window.scrollTo(0, 1080)")
    #   sleep(1)


testbot = SearchBot("San Francisco, CA")
testbot.search_google()
testbot.retrieve_list()
