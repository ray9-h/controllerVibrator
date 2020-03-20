from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#programmed with love by @ray9_h
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://html5gamepad.com/")

time.sleep(10)

vib = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/ul[4]/li[6]')

while True:
    time.sleep(1)
    vib.click()
