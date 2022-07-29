import requests
from bs4 import BeautifulSoup
# import discogs_client


# this is my user-generated developer token
TOKEN = "DBiUmQgyHHBGmXsybviPrgmVVSJmMDdhpxBAGwle"

# catalog number taken from spine of vinyl record
# warplp324
# barn080ab
# 6750577
# b0029607-01
# xllp318
catalog_number = "b0029607-01"

# url structure to query database
URL = "https://api.discogs.com/database/search?q=" + catalog_number + "&token=" + TOKEN

# sends api request to discogs
response = requests.get(URL)

# converts request to json
json = response.json()

# gathers first release from query results
release = json['results'][0]

# access to key pieces of data
print(release['title']) #string
print(release['year']) #string
print(release['label'][0]) #string
print(release['genre']) #list
print(release['style']) #list
print(release['id']) #string
print(release['country']) #string


# Commenting out code that utilizes discogs_client module
# accessing discogs client (application name + token required)
# d = discogs_client.Client('VinylApplication', user_token=TOKEN)

# # retrieves python release object from id gathered above
# release_object = d.release(int(release['id']))
# print(release_object.title)

# testing Pitchfork score data-scraping
album = release['title']

def get_score(release):
    release_text = clean_string(release['title'])
    url = "https://pitchfork.com/reviews/albums/" + release_text
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    p = soup.find('p')
    span = soup.find('span', {'class': 'score'})
    if span:
        try:
            print(span.text)
            return float(span.text)
        except:
            print('span is not a valid score')
    try:
        print(float(p.text))
        return float(p.text)
    except:
        'p is not a valid score'

def clean_string(string):
    word_list = string.split()
    new_list = []
    for word in word_list:
        clean_word = "".join(filter(str.isalnum, word))
        if clean_word:
            new_list += [clean_word]
    clean_str = "-".join(new_list)
    return clean_str.lower()

get_score(release)









