import requests
from bs4 import BeautifulSoup
import time


URL = 'https://www.billboard.com/charts/hot-100'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
song_title = []
song_Artist = []
song_number = []

song_data = soup.find_all('li', attrs={"class": 'chart-list__element display-flex'})

for store in song_data:
    number = store.button.span.span.text
    print(number)