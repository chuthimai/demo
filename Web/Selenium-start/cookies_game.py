import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookies = driver.find_element(By.ID, "bigCookie")

loop = 100000
while loop > 0:
    cookies.click()
    loop -= 1

time.sleep(100)
driver.close()





