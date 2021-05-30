import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from group import Group

class TestFirsttestpython():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()
  def test_add_new_group(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.create_new_group(Group(namegroup="First_group", header="First_group", footer="First_group"))
    self.logout()
  def logout(self):
    self.driver.find_element(By.LINK_TEXT, "group page").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  def create_new_group(self, group):
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    self.driver.find_element(By.LINK_TEXT, "groups").click()
    self.driver.find_element(By.NAME, "new").click()
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys(group.namegroup)
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
    self.driver.find_element(By.NAME, "submit").click()
  def login(self, username, password):
    self.driver.find_element(By.NAME, "user").send_keys(username)
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys(password)
  def open_home_page(self):
    self.driver.get("http://192.168.1.106/addressbook/index.php")
    self.driver.set_window_size(949, 692)

  def test_new_group_empty(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.create_new_group(Group(namegroup="", header="", footer=""))
    self.logout()