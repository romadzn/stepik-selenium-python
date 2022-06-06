from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    res = (int(num1) + int(num2))
    stres = str(res)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(stres).click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:    
    time.sleep(5)
    browser.quit()
    