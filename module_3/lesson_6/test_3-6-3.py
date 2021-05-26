from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
import time
import math

url = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1','https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1', 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1',]

textprov = ''

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    print('Послание:' + textprov)
    browser.quit()

@pytest.mark.parametrize('address', url)
def test_guest_should_see_login_link(browser, address):
    link = f"{address}"
    browser.get(link)

    browser.implicitly_wait(5)
    browser.find_element_by_css_selector("[class='ember-text-area ember-view textarea string-quiz__textarea']").click()
    browser.find_element_by_css_selector("[class='ember-text-area ember-view textarea string-quiz__textarea']").send_keys(str(math.log(int(time.time())))) # "[id='ember184']"
    WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="submit-submission"]')))
    browser.find_element_by_css_selector('[class="submit-submission"]').click()
    prov = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='smart-hints__hint']"))).text

    global textprov
    if prov != "Correct!":
        textprov = textprov + str(prov)
        print('В переменную добавленно выражение отличное от образца:' + textprov)

