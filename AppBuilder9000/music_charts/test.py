
import requests
from bs4 import BeautifulSoup

URL = 'https://www.billboard.com/charts/hot-100'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('span', class_='chart-element__information__artist')
for result in results:
    print(result.get_text())

position = soup.find_all('span', class_='chart-element__rank__number')
for spot in position:
    print(position.get_text())

