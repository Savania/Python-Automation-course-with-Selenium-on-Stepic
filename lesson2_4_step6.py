from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os


link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element(By.ID, "button")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
