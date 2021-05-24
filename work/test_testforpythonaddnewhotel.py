import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_for_python_add_new_hotel():
  def setup_method(self, method): # Создание класса и инициализация драйвера
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method): # Завершение работы драйвера
    self.driver.quit()
  
  def test_testforpythonaddnewhotel(self):
    self.driver.get("http://10.10.50.171/fins_rus/start.swe?SWECmd=Login&SWECM=S&SRN=&SWEHo=10.10.50.171")
    self.driver.set_window_size(1050, 840)
    self.Login()
    self.Create_new_Hotel()
    self.logout()

  def Create_new_Hotel(self): # Создание нового отеля
    time.sleep(2)
    self.driver.find_element(By.ID, "j_s_sctrl_tabScreen").click() # Клик Расскрывающейся список
    time.sleep(1)
    dropdown = self.driver.find_element(By.ID, "j_s_sctrl_tabScreen")
    dropdown.find_element(By.XPATH, "//option[. = 'Гостиницы']").click() # Выбор из списка пункта "Гостиницы"
    time.sleep(1)
    self.driver.find_element(By.ID, "j_s_sctrl_tabScreen").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "s_2_1_4_0_Ctrl").click() # Клик создать гостиницу +
    time.sleep(1)
    self.driver.find_element(By.XPATH, '//*[@id="1_Name"]').send_keys("Test_python"+(str(random.randint(1, 99)))) # Имя гостиницы
    time.sleep(1)
    self.driver.find_element(By.ID, "1_s_2_l_Tax_Exempt_Number").click()
    self.driver.find_element(By.ID, "1_Tax_Exempt_Number").send_keys(str(random.randint(1, 5))) # Кол звезд
    time.sleep(1)
    self.driver.find_element(By.ID, "1_s_2_l_Hotel_City").click()
    self.driver.find_element(By.ID, "s_2_2_20_0_icon").click()
    self.driver.find_element(By.ID, "ui-id-147").click()
    self.driver.find_element(By.ID, "1_s_2_l_Latitude").click()
    self.driver.find_element(By.ID, "1_Latitude").send_keys("53,",str(random.randint(100, 999))) # Штрота
    time.sleep(1)
    self.driver.find_element(By.ID, "1_s_2_l_Longitude").click()
    self.driver.find_element(By.ID, "1_Longitude").send_keys("41,",str(random.randint(100, 999))) # Долгота
    time.sleep(1)
    self.driver.find_element(By.ID, "1_s_2_l_Hotel_Info").click()
    self.driver.find_element(By.ID, "1_Hotel_Info").send_keys("Рязань") # Комментарий
    time.sleep(1)
    self.driver.find_element(By.ID, "2_s_2_l_Name").click() # Переход на другое поле для слхранения

  def logout(self): # Выход
    self.driver.find_element(By.ID, "tb_0").click()
    self.driver.find_element(By.CSS_SELECTOR, ".siebui-btn-logout").click()

  def Login(self): # Вход
    self.driver.find_element(By.ID, "s_swepi_1").send_keys("KSELYUTIN")
    self.driver.find_element(By.ID, "s_swepi_2").send_keys("KSELYUTIN")
    self.driver.find_element(By.ID, "s_swepi_22").click()
  
