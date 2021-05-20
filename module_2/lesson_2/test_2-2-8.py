from selenium import webdriver
import time
import os


with open("test.txt", "w") as file:
    content = file.write("automationbypython")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

# Инициализируем драйвер, переходим по ссылке
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Заполняем поля
    browser.find_element_by_css_selector('input[placeholder="Enter first name"]').send_keys("Ivan")
    browser.find_element_by_css_selector('input[placeholder="Enter last name"]').send_keys("Petrov")
    browser.find_element_by_css_selector('input[placeholder="Enter email"]').send_keys("IvanPetrov@mail.ru")
    # Добавляем файл

    browser.find_element_by_xpath('//*[@id="file"]').send_keys(file_path)
    print(file_path)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()