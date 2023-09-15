from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math


link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

element = browser.find_element(By.ID, "input_value")
x = int(element.text)
inputs = browser.find_element(By.ID, "answer")
inputs.send_keys(str(math.log(abs(12*math.sin(x)))))

option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()

option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
option2.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
browser.quit()
