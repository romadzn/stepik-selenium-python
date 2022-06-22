"""
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
Ваша задача — реализовать автотест со следующим сценарием действий: 

открыть страницу 
ввести правильный ответ 
нажать кнопку "Отправить" 
дождаться фидбека о том, что ответ правильный 
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
Опциональный фидбек — это текст в черном поле, как показано на скриншоте: 
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.mark.parametrize("linknums", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestPagesTask:
    def test_links_parametrize(self, browser, linknums):
        link = f"https://stepik.org/lesson/{linknums}/step/1"
        browser.get(link)
        browser.implicitly_wait(5)
        
        input1 = browser.find_element(By.TAG_NAME, "textarea")
        input1.send_keys(str(math.log(int(time.time()))))
        browser.implicitly_wait(5)
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        
        checkval = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        assert "Correct!" == checkval.text

if __name__ == '__main__':
    pytest.main()        