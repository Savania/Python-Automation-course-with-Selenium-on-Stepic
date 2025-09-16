
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
import os


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button.click()
    browser.execute_script("window.scrollBy(0, 100);")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    value = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(value)
    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла