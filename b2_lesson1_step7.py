"""
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. 
Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("treasure")
    valuex = x_element.get_attribute("valuex")
    x = valuex
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("input:required")
    input1.send_keys(y)   
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click() 
    
    option2 = browser.find_element_by_id("robotsRule")
    option2.click() 
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()   
    
finally:
    time.sleep(5)
    browser.quit()
    
    