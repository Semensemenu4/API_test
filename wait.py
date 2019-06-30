from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

chromedriver = '/home/sergey/python/chromedriver'
browser = webdriver.Chrome(chromedriver)
#browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/registration1.html")
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR')
    )
browser.find_element_by_id('book').click()

x = browser.find_element_by_xpath("//span[@id='input_value']")
inp = calc(x.text)

browser.find_element_by_xpath("//input[@id='answer']").send_keys(inp)
browser.find_element_by_xpath("//button[@id='solve']").click()

alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
