import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import os

EMAIL = os.environ.get("EMAIL")
OTHER_EMAIL = os.environ.get("OTHER EMAIL")
PASS = os.environ.get("PASS")
URL = "https://tiki.vn/to-mau-nguoi-lon-mai-lan-cuc-truc-p195133818.html?itm_campaign=tiki-reco_UNK_DT_UNK_UNK_tiki-listing_UNK_p-category-mpid-listing-v1_202304020600_MD_batched_PID.195133819&itm_medium=CPC&itm_source=tiki-reco&spid=195133819"

header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
    }

response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
name_items = soup.find(name="h1", class_="title").text
price = soup.find(name="div", class_="product-price__current-price").text

price_without_currency = int(float(price.split(' ')[0])*1000)

reasonable_price = 60000
should_buy = (price_without_currency <= reasonable_price)

if should_buy:
    message = f"Subject:Giá '{name_items}' trên Tiki\n\nGiá của sản phẩm '{name_items}' trên Tiki hiện tại là {price_without_currency} đ." \
              f"\n{URL}"
    print(message)
    connection = SMTP(host="smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL, password=PASS)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=OTHER_EMAIL,
        msg=message.encode('utf-8')
    )
    connection.close()










