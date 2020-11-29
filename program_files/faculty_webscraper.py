from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Bot:
  def __init__(self):
    self.path = "./program_files/chromedriver"
    self.input = 'schools.txt'
    self.searches = []
    self.driver = None
    self.links = [] # delete later
    self.stack = []

  def cycle(self):
    # self.set()
    # self.google()
    # self.getlinks()
    # self.unstack()
    # self.quit()
    self.txt()
    print(self.searches)

  def set(self):
    self.driver = webdriver.Chrome(self.path)

  def google(self):
    self.driver.get("http://google.com")
    search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    search.send_keys("test")
    search.send_keys(Keys.RETURN)
    time.sleep(3)

  def getlinks(self):
    searchdiv = self.driver.find_element_by_id("search")
    self.links = searchdiv.find_elements_by_tag_name("a") # delete later
    links = searchdiv.find_elements_by_tag_name("a")
    for link in links:
      url = link.get_attribute('href')
      if url not in self.stack:
        self.stack.append(url)

  def unstack(self):
    while len(self.stack) > 0:
      url = self.stack.pop()
      self.driver.get(url)
      time.sleep(3)

  def txt(self):
    with open(self.input) as file:
      text = file.readline()
      while text:
          line = text.strip()
          self.searches.append(line)
          text = file.readline()

    
  def clicklink(self, idx): # delete later
    self.links[idx].click()
    time.sleep(3)

  def quit(self):
    self.driver.quit()


test = Bot()
test.cycle()
