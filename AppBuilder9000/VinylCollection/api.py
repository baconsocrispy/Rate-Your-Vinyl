# import requests
#
# # this is my user-generated developer token
# TOKEN = "DBiUmQgyHHBGmXsybviPrgmVVSJmMDdhpxBAGwle"
#
# # catalog number taken from spine of vinyl record
# catalog_number = "aotnlp016"
#
# # url structure to query database
# URL = "https://api.discogs.com/database/search?q=" + catalog_number + "&token=" + TOKEN
#
# # sends api request to discogs
# response = requests.get(URL)
#
# # converts request to json
# json = response.json()
#
# # gathers first release from query results
# release = json['results'][0]
#
# # access to key pieces of data
# print(release['title']) #string
# print(release['year']) #string
# print(release['label'][0]) #string
# print(release['genre']) #list
# print(release['style']) #list
# print(release['id']) #string
# print(release['country']) #string
#
# # accessing discogs client (application name + token required)
# d = discogs_client.Client('VinylApplication', user_token=TOKEN)
#
# # retrieves python release object from id gathered above
# release_object = d.release(int(release['id']))
#
# print(release_object.title)
#
# album = "Greg Foat - The Mage")
# print(album)
#
# # v = '-'.join(filter(str.isalnum, album))
# # print(v)
#
#
#
#
#
#
#
#
#
