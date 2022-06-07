"""
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, 
который дизайнер всё никак не успевает переделать.
Вам потребуется написать код, чтобы:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), 
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 150);")
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("input:required")
    input1.send_keys(y)   
    
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click() 
    
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click() 
    
    
    button = browser.find_element_by_tag_name("button")
    button.click() 
    
finally:
    time.sleep(5)
    browser.quit()    
    