from bs4 import BeautifulSoup
import requests
import lxml

url = "https://store.steampowered.com/app/291650/Pillars_of_Eternity/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
#print(soup.prettify())

name = soup.select_one(selector=".apphub_AppName").getText()
# print(name)

price = soup.select_one(selector=".game_purchase_action_bg").getText()
price = price.strip()
price = price[1:]
# print(price)

# Function to scrape data from our website
# Will return ('Pillars of Eternity', '29.99\t\t\t\t\t\t\n\n\nAdd to Cart')

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")


    name = soup.select_one(selector=".apphub_AppName").getText()


    price = soup.select_one(selector=".game_purchase_action_bg").getText()
    price = price.strip()
    price = price[1:]

    return name, price
print(get_link_data(url))
