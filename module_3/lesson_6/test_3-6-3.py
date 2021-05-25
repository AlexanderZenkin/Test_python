import pytest
from selenium import webdriver
import time
import math

#answer = math.log(int(time.time()))

a = 'https://stepik.org/lesson/236895/step/1'
b = 'https://stepik.org/lesson/236896/step/1'
c = 'https://stepik.org/lesson/236897/step/1'
d = 'https://stepik.org/lesson/236898/step/1'
e = 'https://stepik.org/lesson/236899/step/1'
f = 'https://stepik.org/lesson/236903/step/1'
g = 'https://stepik.org/lesson/236904/step/1'
h = 'https://stepik.org/lesson/236905/step/1'

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('address', [a, b, c, d, e, f, g, h])
def test_guest_should_see_login_link(browser, address):
    link = f"{address}"
    browser.get(link)
    time.sleep(15)
    answer = math.log(int(time.time()))
    browser.find_element_by_xpath("//*[@id='ember85']").click()
    browser.find_element_by_xpath("//*[@id='ember85']").send_keys(str(answer)) # "[id='ember184']"
    time.sleep(1)
    browser.find_element_by_css_selector('[class="submit-submission"]').click()
    time.sleep(20)
    welcome_text_elt = browser.find_element_by_css_selector("[class='smart-hints__hint']") #//*[@id="ember116"]/pre
    welcome_text = welcome_text_elt.text
    assert ("Correct!") == (welcome_text)

