from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser = webdriver.Chrome()
browser.get(link)


inputs = browser.find_element(By.NAME, "firstname")
inputs.send_keys('обязательное поле')
inputs = browser.find_element(By.NAME, "lastname")
inputs.send_keys('обязательное поле')
inputs = browser.find_element(By.NAME, "email")
inputs.send_keys('обязательное поле')
element = browser.find_element(By.NAME, "file")
element.send_keys(file_path)

    # Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


time.sleep(10)
browser.quit()