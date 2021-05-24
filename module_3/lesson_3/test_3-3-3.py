import pytest
import unittest
from selenium import webdriver
import time

class test_pageregistration(unittest.TestCase):
    def test_positive(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(link)
        self.browser.find_element_by_css_selector('div.first_block [class="form-control first"]').send_keys("Ivan")
        self.browser.find_element_by_css_selector('div.first_block [class="form-control second"]').send_keys("Petrov")
        self.browser.find_element_by_css_selector('div.first_block [class="form-control third"]').send_keys("IvanPetrov@mail.ru")
        self.browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert ("Congratulations! You have successfully registered!") == (welcome_text)

    def test_negative(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(link)
        self.browser.find_element_by_css_selector('div.first_block [class="form-control first"]').send_keys("Ivan")
        self.browser.find_element_by_css_selector('div.first_block [class="form-control second"]').send_keys("Petrov")
        self.browser.find_element_by_css_selector('div.first_block [class="form-control third"]').send_keys("IvanPetrov@mail.ru")
        self.browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert ("Congratulations! You have successfully registered!") == (welcome_text)

