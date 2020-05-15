from selenium import webdriver
from time import sleep
from getpass import getpass


class LikeBot:
  def __init__(self, username, password):
    self.username = username or input("Please input your username: ")
    self.password = password or getpass(
        "Please input your password (private / not saved): ")
    self.driver = webdriver.Chrome()
    self.driver.get("https://instagram.com")
    sleep(2)

  def login(self):
    # fill in username
    login_name = self.driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"
    ).send_keys(self.username)

    # fill in password
    login_pass = self.driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input"
    ).send_keys(self.password)
    sleep(1)

    # delete password from temporary variable
    self.password = None

    # click log in button
    self.driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]"
    ).click()
    sleep(3)

    # click not now button to close pop up modal
    self.driver.find_element_by_xpath(
        "/html/body/div[4]/div/div/div[3]/button[2]"
    ).click()
    sleep(1)

  def fetch_followers(self):  # not yet working
    # click users profile link
    self.driver.find_element_by_xpath(
        "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img"
    ).click()
    sleep(1)

    # click followers link
    self.driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"
    ).click()
    sleep(1)

    # scroll to bottom of followers modal
    modal_bottom = self.driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/ul/div")
    followers_ul = self.driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/ul")
    followers_ul.click()

    # self.driver.execute_script("arguments[0].scrollIntoView()", modal_bottom)
    # while (True):
    #   self.driver.execute_script("window.scrollTo(0, 1080)")
    #   sleep(1)


testbot = LikeBot("tombetthauser", "Ch1pD00d3?")
testbot.login()
testbot.fetch_followers()
