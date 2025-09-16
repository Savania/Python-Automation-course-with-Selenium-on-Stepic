from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    value = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(value)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла