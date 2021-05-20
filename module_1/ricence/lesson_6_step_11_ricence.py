from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input_last_name.send_keys("Petrov")
    input_email = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input_email.send_keys("Ivan_Petrov@yandex.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
