"""
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла 
Просмотрите отчёт о запуске и найдите последнюю строчку 
Отправьте эту строчку в качестве ответа на это задание 
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. 
Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. 

Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке. 
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestClassOne(unittest.TestCase):
    def test_registration1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.XPATH, "//label[contains(text(),'First name*')]//following-sibling::input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH, "//label[contains(text(),'Last name*')]//following-sibling::input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "//label[contains(text(),'Email*')]//following-sibling::input")
            input3.send_keys("qwe@gmail.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Shoud be equal")

        finally:
            time.sleep(5)
            browser.quit()

        

    def test_registration2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

        # Kод, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH, "//label[contains(text(),'First name*')]//following-sibling::input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH, "//label[contains(text(),'Last name*')]//following-sibling::input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "//label[contains(text(),'Email*')]//following-sibling::input")
            input3.send_keys("sth@gmail.com")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Shoud be equal")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

        
if __name__ == "__main__":
    unittest.main()