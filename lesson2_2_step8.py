from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Test")
    input_lname = browser.find_element(By.NAME, "lastname")
    input_lname.send_keys("Test")
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("Test@test.test")
    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')  # добавляем к этому пути имя файла
    file.send_keys(file_path)
    print(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла