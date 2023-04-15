from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")
driver = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div')

upcoming_event = {}
list = driver.find_elements(by=By.TAG_NAME, value="li")

count = 0
for i in list:
    date = i.find_element(by=By.TAG_NAME, value="time")
    event = i.find_element(by=By.TAG_NAME, value="a")
    upcoming_event[count] = {"date": date.text, "event": event.text}
    count += 1

print(upcoming_event)


