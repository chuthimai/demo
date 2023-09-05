from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


GG_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfdu3rDQ18JQWqUCToZMYTR9AR_zIcgZMeNTLQSXrkmbC5Wbw/viewform?usp=sf_link"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-128.25608290625001%2C%22east%22%3A-116.61057509375001%2C%22south%22%3A32.81061121465328%2C%22north%22%3A42.427730472853206%7D%2C%22mapZoom%22%3A6%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def input_data(add, p, l):
    driver = webdriver.Chrome()
    driver.get(GG_LINK)
    time.sleep(3)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(add)
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(p)
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(l)
    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    send_button.click()
    driver.quit()


def write_to_csv(add, p, l):
    csvfile = open('Price of house.csv', 'a', newline='')
    c = csv.writer(csvfile)
    # c.writerow(["Address", "Price", "Link"])
    for i in range(len(add)):
        c.writerow([add[i], p[i].split('+')[0], l[i]])
    csvfile.close()


def get_data():
    time.sleep(20)
    find_grid = driver.find_elements(By.TAG_NAME, "article")

    price = []
    address = []
    link = []
    for grid in find_grid:
        address.append(grid.find_element(By.TAG_NAME, 'address').text)
        price.append(grid.find_element(By.TAG_NAME, 'span').text)
        link.append(grid.find_element(By.TAG_NAME, 'a').get_attribute("href"))

    # for i in range(len(price)):
    #     input_data(address[i], price[i], link[i])
    write_to_csv(address, price, link)
    find_grid[0].find_element(By.TAG_NAME, 'a').click()
    get_data()


driver = webdriver.Chrome()
driver.get(ZILLOW_LINK)
get_data()



