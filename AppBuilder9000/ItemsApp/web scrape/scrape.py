import requests
from bs4 import BeautifulSoup
import pandas as pd


# Webpage request to grab the skeleton of the web page.
page = requests.get('http://books.toscrape.com/')

# Grabs the page source and stores it into the variable 'soup'.
soup = BeautifulSoup(page.content, 'html.parser')

# Book list inside of the section tag.
books = soup.find('section')


# All Books Info
"""Prices"""
book_price = books.select(".product_pod .price_color")
prices = [bp.get_text() for bp in book_price]

"""Titles"""
book_titles = books.select(".product_pod h3")
titles = [t.get_text() for t in book_titles]

"""Covers"""
book_img = books.select('img')
book_covers = [bc["src"] for bc in book_img]


"""Pandas data frame"""
book_list = pd.DataFrame({
    "Titles": titles,
    "Covers": book_covers,
    "Prices": prices
})


