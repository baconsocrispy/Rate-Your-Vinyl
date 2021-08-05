from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.officialcharts.com/charts/albums-chart/').text
soup = BeautifulSoup(source, features='html.parser')
chart = soup.find('table', class_='chart-positions')

for track in chart.find_all('div', class_='track', limit=10):
    cover_src = track.find('img')['src']
    title = track.find('div', class_='title').a.text
    artist = track.find('div', class_='artist').a.text

    print(cover_src)
    print(title)
    print(artist)
    print()
