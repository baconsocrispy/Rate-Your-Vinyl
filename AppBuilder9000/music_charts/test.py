import requests
from bs4 import BeautifulSoup
import time


def hot_hundred():
    URL = 'https://www.billboard.com/charts/hot-100'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    section = soup.find_all('article', class_='ye-chart-item piano-content-overlay__gated-item')
    for index, piece in enumerate(section):
        artist = section.find_all('div', class_='ye-chart-item__artist')
        song = section.find('div', class_='ye-chart-item__title').div.text
        position = section.find('span', class_='decade-end-chart-item__peak-info-data').span.text
        peak_date = section.find('span', class_='decade-end-chart-item__peak-info-data').span.text
        print(f"""Song: {song}""")
        print(f"""Song: {artist}""")
        print(f"""Song: {position}""")
        print(f"""Song: {peak_date}""")