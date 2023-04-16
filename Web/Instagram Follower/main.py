from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

USERNAME = os.environ.get("USERNAME")
PASS = os.environ.get("PASS")


class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.all_button = None

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_box.send_keys(USERNAME)
        pass_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_box.send_keys(PASS)
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        log_in_button.click()
        time.sleep(30)

    def follow(self):
        follower = self.driver.find_element(By.CSS_SELECTOR, "._aano")
        self.all_button = follower.find_elements(By.CSS_SELECTOR, "button")
        print(self.all_button)
        for button in self.all_button:
            print("LOL ---> 0")
            try:
                print("LOL ---> 1")
                button.click()
            except:
                print("LOL ---> 2")
                time.sleep(5)
                self.follow()


instaFollow = InstaFollower()
instaFollow.login()
instaFollow.follow()
time.sleep(60)
