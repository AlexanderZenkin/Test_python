from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//*[@id="treasure"]') # Нашли элемент
    checked = x_element.get_attribute("valuex")
    x = checked
    y = calc(x)

    input3 = browser.find_element_by_xpath('//*[@id="answer"]')
    input3.send_keys(y)
    input3 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    input3.click()
    input3 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    input3.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()