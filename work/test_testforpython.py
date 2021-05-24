import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

class TestTestforpython():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}


  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testforpython(self):
    self.driver.get("http://10.10.50.171/fins_rus/start.swe?SWECmd=Login&SWECM=S&SRN=&SWEHo=10.10.50.171")
    self.driver.set_window_size(1600, 1024)
    self.driver.find_element(By.ID, "s_swepi_1").send_keys("KSELYUTIN")
    self.driver.find_element(By.ID, "s_swepi_2").send_keys("KSELYUTIN")
    self.driver.find_element(By.ID, "s_swepi_22").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'Гостиницы поиск\')]").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, '[name="s_1_1_1_0"]').send_keys("Рязань")
    time.sleep(0.5)
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/span["+str(random.randint(1, 5))+"]/i").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, "#s_1_1_0_0_Ctrl > span").click()
    time.sleep(0.5)
    self.driver.find_element(By.ID, "tb_0").click()
    self.driver.find_element(By.CSS_SELECTOR, ".siebui-btn-logout").click()