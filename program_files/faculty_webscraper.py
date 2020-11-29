from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import time
import re

class Bot:
  def __init__(self):
    print(chr(27) + "[2J")
    print("Initiating new Bot... 🐬\n")
    self.path = "./chromedriver"
    self.input = 'schools.txt'
    self.searches = []
    self.driver = None
    self.stack = []
    self.list = []
    self.max = 10
    self.arts = [] # useless but beautiful...

  def cycle(self):
    self.set()
    self.txt()
    self.google()
    self.quit()

  def sleep(self):
    max = self.max
    min = 3
    random = (max - min)*np.random.random() + min
    time.sleep(random)
    
  def emails(self):
    print("running self.emails()...")
    source = self.driver.page_source
    print("charactor length of source is", len(source))
    source = re.split('>|<|. |\)|\(|[|]|\"|\'|\`|\\n|/', source)
    # source = re.split('>|<|. ', source) # original glory...
    # print(source) # open the universe...
    self.arts.append(source)
    p = re.compile(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")
    temps = [s for s in source if p.match(s)]
    for email in temps:
      if email not in self.list:
        self.list.append(email)
    print(self.list)
    print("closing self.emails ✓\n")

  def empty(self):
    print("running self.empty()...")
    print(len(self.list), " in self.list")
    file = open("output.txt", "a")
    while len(self.list) > 0:
      email = self.list.pop()
      print("adding", email, "to output.txt")
      file.write(email)
      file.write("\n")
    print(len(self.list), " in self.list")
    print("closing self.empty ✓\n")

  def set(self):
    print("running self.set()...")
    self.driver = webdriver.Chrome(self.path)
    print("closing self.set ✓\n")

  def check(self):
    print("\nrunning self.check()... 🌀")
    self.empty()
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
    self.sleep()
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
      self.driver.get(url)
      self.sleep()
      self.emails()
    print('\ncurrent stack empty 📂')
    self.check()
    print("\nclosing self.unstack ✓\n")

  def txt(self):
    print("running txt()...")
    with open(self.input) as file:
      text = file.readline()
      while text:
          line = text.strip()
          self.searches.append(line)
          text = file.readline()
    self.sleep()
    print("closing self.txt ✓\n")

  def quit(self):
    print("running quit()... all done! 👍")
    self.driver.quit()

test = Bot()
test.cycle()