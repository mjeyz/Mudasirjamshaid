from bs4 import BeautifulSoup
import requests
import smtplib


practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
PASSWORD = "apul vxon fmai kxgx"
MY_EMAIL = "thisismjeyz@gmail.com"
TO_ADDRESS= "mudasirjamshaid0@gmail.com"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.8",
}

response = requests.get(practice_url)

soup = BeautifulSoup(response.content, "html.parser")
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)

if price_as_float < 100:
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs= TO_ADDRESS,
                                msg=f"subject:Amazon Price Alert \n\n Today price of your product is  {price_as_float}."
                                    f" Go and buy now.")
    except smtplib.SMTPException as e:
        print(f"An smtp error is happening and error is {e}")
    else:
        print(f"Message sent to {TO_ADDRESS} successfully.")
