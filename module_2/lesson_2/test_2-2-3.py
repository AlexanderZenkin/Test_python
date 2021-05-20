from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element_by_xpath('//*[@id="num1"]') # Нашли элемент 1
    x = x_element1.text
    x_element2 = browser.find_element_by_xpath('//*[@id="num2"]')  # Нашли элемент 2
    y = x_element2.text
    summa = int(x) + int(y)
    sum = str(summa)

    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_visible_text(sum)


    button = browser.find_element_by_css_selector("button.btn").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()