from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2951907624&distance=5&f_AL=true&f_JT=F&geoId=105790653&keywords=python%20developer&location=Hanoi%2C%20Hanoi%2C%20Vietnam&refresh=true")

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()

email = os.environ.get("EMAIL")
email_box = driver.find_element(By.CSS_SELECTOR,"#username")
email_box.send_keys(email)
email_box.send_keys(Keys.ENTER)

password = os.environ.get("PASS")
pass_word_box = driver.find_element(By.CSS_SELECTOR, "#password")
pass_word_box.send_keys(password)
pass_word_box.send_keys(Keys.ENTER)


time.sleep(20)
job = driver.find_elements(
    By.CSS_SELECTOR,
    ".relative"
    ".job-card-list"
    ".job-card-container--clickable"
    )
job[0].click()

time.sleep(5)
easy_apply_box = driver.find_elements(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
easy_apply_box[0].click()

time.sleep(3)
phone_number = os.environ.get("PHONE")
phone_number_box = driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--container input")
phone_number_box.send_keys(phone_number)

next_button = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end button")
next_button.click()


time.sleep(120)








