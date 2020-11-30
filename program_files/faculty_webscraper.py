from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import numpy as np
import time
import re

class Bot:
  def __init__(self):
    print(chr(27) + "[2J")
    print("Initiating new Bot... 🐬\n")
    self.start = self.printtime()
    self.path = "./chromedriver"
    self.input = 'schools.txt'
    self.visitedurls = {"cat", "dog"}
    self.googlinksmax = 3
    self.searches = []
    self.driver = None
    self.stack = []
    self.stack2 = []
    self.stack3 = []
    self.list = []
    self.max = 10
    self.arts = [] # useless but beautiful...

  def cycle(self):
    self.writestart()
    self.set()
    self.txt()
    self.google()
    self.writestop()
    self.quit()

  def writestart(self):
    file = open("output.txt", "a")
    file.write("starting at ----> ")
    file.write(self.start.strftime("%H:%M:%S"))
    file.write("\n")

  def writestop(self):
    now = datetime.now()
    file = open("output.txt", "a")
    file.write("stopping at ----> ")
    file.write(now.strftime("%H:%M:%S"))
    file.write("\n")

  def sleep(self):
    max = self.max
    min = 5
    random = (max - min)*np.random.random() + min
    print("pausing for", random, "sec...")
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
    print("removing school from input txt file...\n")
    self.popschool()
    print("closing self.empty ✓\n")

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
      self.empty()
      return self.google()
    self.quit()

  def google(self):
    print("running google()...")
    self.driver.get("http://google.com")
    self.sleep()
    try:
      search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
      term = self.searches.pop() + " art department faculty directory"
      print('searching for', term, '...')
      search.send_keys(term)
      search.send_keys(Keys.RETURN)
    except:
      print("failed to load page")
    self.sleep()
    self.getlinks()
    self.check()
    print("closing self.google ✓\n")

  def getlinks(self, stacknum = 1):
    print("running getlinks()...")
    searchdiv = self.driver.find_element_by_id("search")
    self.links = searchdiv.find_elements_by_tag_name("a") # delete later
    links = searchdiv.find_elements_by_tag_name("a")
    count = 0
    for link in links:
      url = link.get_attribute('href')
      if url != None:
        if "google" not in url:
          if ".edu" in url:
            if "@" not in url:
              if url not in self.visitedurls:
                if count < self.googlinksmax:
                  self.visitedurls.add(url)
                  count = count + 1
                  if url not in self.stack:
                    if stacknum == 2:
                      self.stack2.append(url)
                    elif stacknum == 3:
                      self.stack3.append(url)
                    else:
                      self.stack.append(url)
    print("closing self.getlinks ✓\n")

  def getlinks2(self, stacknum = 1):
    print("running getlinks2()...")
    links = self.driver.find_elements_by_tag_name("a")
    for link in links:
      url = link.get_attribute('href')
      if url not in self.stack:
        if "google" not in url:
          if ".edu" in url:
            if "@" not in url:
              if "faculty" in url or "directory" in url or "staff" in url or "contact" in url:
                if url not in self.visitedurls:
                  self.visitedurls.add(url)
                  if stacknum == 2:
                    self.stack2.append(url)
                    print("adding url to self.stack2 ----->", url)
                  elif stacknum == 3:
                    self.stack3.append(url)
                    print("adding url to self.stack3 ----->", url)
                  else:
                    self.stack.append(url)
                    print("adding url to self.stack ----->", url)
    print("closing self.getlinks2 ✓\n")

  def popschool(self):
    string = []
    with open(self.input, "r") as file:
      content = file.readlines()
      print("\n".join(content[:-1]))
      string = "".join(content[:-1])
    with open(self.input, "w") as file:
      file.write(string)

  def unstack(self):
    print("running unstack()...")
    while len(self.stack) > 0:
      url = self.stack.pop()
      print('\npopping new url off self.stack')
      print(len(self.stack), 'items in self.stack')
      print('redirecting to\n', url)
      try:
        self.driver.get(url)
        self.sleep()
        self.emails()
        self.getlinks2(2)
      except:
        print("url / href is None")
    print('self.stack empty')
    if len(self.list) > 20:
      self.stack2 = []
    while len(self.stack2) > 0:
      self.stack2 = self.stack2[0:30]
      if len(self.list) > 50:
        self.stack2 = []
      try:
        url = self.stack2.pop()
      except:
        print("error bypassed ----> attempted stack2.pop on empty stack")
      print('\npopping new url off self.stack2')
      print(len(self.stack2), 'items in self.stack2')
      print('redirecting to\n', url)
      try:
        self.driver.get(url)
        self.sleep()
        self.emails()
        self.getlinks2(3)
      except:
        print("url / href is None")
    print('self.stack2 empty')
    if len(self.list) > 20:
      self.stack3 = []
    while len(self.stack3) > 0:
      self.stack3 = self.stack2[0:30]
      if len(self.list) > 50:
        self.stack3 = []
      url = self.stack3.pop()
      print('\npopping new url off self.stack3')
      print(len(self.stack3), 'items in self.stack3')
      print('redirecting to\n', url)
      try:
        self.driver.get(url)
        self.sleep()
        self.emails()
      except:
        print("url / href is None")
    print('self.stack3 empty')
    print('\nall stacks empty 📂')
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
    if len(self.list) > 0:
      self.empty()
    self.printtime()
    print("started at ----> ", self.start.strftime("%H:%M:%S"))
    print("running quit()... all done! 👍")
    self.driver.quit()

  def printtime(self):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("current time ---->", current_time)
    return now

test = Bot()
test.cycle()
