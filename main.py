from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

driver = webdriver.Chrome()
try:
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    wait = WebDriverWait(driver, 12)
    price_element = wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_button = driver.find_element(By.ID, "book")
    book_button.click()

    x_element = driver.find_element(By.ID, "input_value")
    x = float(x_element.text)
    result = math.log(abs(12 * math.sin(x)))

    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(str(result))

    submit_button = driver.find_element(By.ID, "solve")
    submit_button.click()

    alert = driver.switch_to.alert
    answer_text = alert.text
    print("Ответ:", answer_text)
    alert.accept()

finally:
    driver.quit()