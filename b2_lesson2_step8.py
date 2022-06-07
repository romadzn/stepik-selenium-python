"""
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    firstName = browser.find_element_by_name("firstname")
    firstName.send_keys("Roman")
    
    lastName = browser.find_element_by_name("lastname")
    lastName.send_keys("Selenium")
    
    email = browser.find_element_by_name("email")
    email.send_keys("qweasdmail.ru")
    
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "file.txt")
    browser.find_element_by_name("file").send_keys(file_path)
    
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
    
finally:    
    time.sleep(5)
    browser.quit()
    