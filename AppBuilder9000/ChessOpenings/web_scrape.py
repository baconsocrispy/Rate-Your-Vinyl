from bs4 import BeautifulSoup
import re

from urllib.request import urlopen

Chessbase_url = "https://shop.chessbase.com/en/openings/spanish_open"


def web_scrape(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    parsed_html = BeautifulSoup(html, "html.parser")
    soup = html.BeautifulSoup.find_all(_class="col-xs-12 col-sm-4 cbdiagram")
    print(soup)


web_scrape(Chessbase_url)
