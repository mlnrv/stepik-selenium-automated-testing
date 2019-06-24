from selenium import webdriver
from time import sleep
from utils import calc, text_to_buffer


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_css_selector("button.btn").click()

    browser.switch_to.alert.accept()

    x_value = browser.find_element_by_id("input_value").text
    answer = calc(int(x_value))

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(answer)

    browser.find_element_by_css_selector("button.btn").click()

    text_alert = browser.switch_to.alert.text
    text_to_buffer(text_alert)

finally:
    sleep(1)
    browser.quit()
