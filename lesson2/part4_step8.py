from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils import calc, text_to_buffer


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )
    browser.find_element_by_id("book").click()

    x_value = browser.find_element_by_id("input_value").text
    answer = calc(int(x_value))

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(answer)

    browser.find_element_by_id("solve").click()

    text_alert = browser.switch_to.alert.text
    text_to_buffer(text_alert)

finally:
    time.sleep(1)
    browser.quit()
