from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Bot:
  def __init__(self):
    print(chr(27) + "[2J")
    print("Initiating new Bot... 🐬\n")
    self.path = "./chromedriver"
    self.input = 'schools.txt'
    self.searches = []
    self.driver = None
    self.links = [] # delete later
    self.stack = []

  def cycle(self):
    self.set()
    self.txt()
    self.google()
    # self.getlinks()
    # self.unstack()
    self.quit()

  def set(self):
    print("running self.set()...")
    self.driver = webdriver.Chrome(self.path)
    print("closing self.set ✓\n")

  def check(self):
    print("\nrunning self.check()... 🌀")
    print(len(self.stack), 'items left in self.stack')
    print(len(self.searches), 'items left in self.searches')
    if len(self.stack) > 0:
      return self.unstack()
    if len(self.searches) > 0:
      return self.google()
    self.quit()

  def google(self):
    print("running google()...")
    self.driver.get("http://google.com")
    search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    term = self.searches.pop()
    print('searching for', term, '...')
    search.send_keys(term)
    search.send_keys(Keys.RETURN)
    time.sleep(3)
    self.getlinks()
    self.check()
    print("closing self.google ✓\n")

  def getlinks(self):
    print("running getlinks()...")
    searchdiv = self.driver.find_element_by_id("search")
    self.links = searchdiv.find_elements_by_tag_name("a") # delete later
    links = searchdiv.find_elements_by_tag_name("a")
    for link in links:
      url = link.get_attribute('href')
      if url not in self.stack:
        self.stack.append(url)
    print("closing self.getlinks ✓\n")

  def unstack(self):
    print("running unstack()...")
    while len(self.stack) > 0:
      url = self.stack.pop()
      print('\npopping new url off self.stack')
      print(len(self.stack), 'items in self.stack')
      print('redirecting to\n', url)
      # self.driver.get(url)
      # time.sleep(3)
    print('current stack empty 📂')
    self.check()
    print("/nclosing self.unstack ✓\n")

  def txt(self):
    print("running txt()...")
    with open(self.input) as file:
      text = file.readline()
      while text:
          line = text.strip()
          self.searches.append(line)
          text = file.readline()
    time.sleep(3)
    print("closing self.txt ✓\n")

    
  def clicklink(self, idx): # delete later
    print("running clicklink()...")
    self.links[idx].click()
    time.sleep(3)
    print("closing self.clicklink ✓\n")

  def quit(self):
    print("running quit()... all done! 👍")
    self.driver.quit()


test = Bot()
test.cycle()
