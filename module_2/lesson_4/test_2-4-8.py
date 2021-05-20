from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[id="price"]'), "$100"))
    browser.find_element_by_css_selector("button.btn").click()

    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    input3 = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(y)
    browser.find_element_by_css_selector("[id='solve']").click()
finally:
    time.sleep(10)
    browser.quit()