import urllib2
import json

api_key = "3b1f753492cceb041b6e48c3e8c54f6f"
secret = "03bb12fa64001d7a0be3e10ee7b0b8be"

format = "json"

baseURL = "http://ws.audioscrobbler.com/2.0/"

# get top Albums in library
class LastfmQuery:
	def getAlbums(self,user):
		response = urllib2.urlopen(baseURL+"?method=library.getAlbums"+"&api_key="+api_key+"&user="+user+"&format="+format)
		json_data = json.loads(response.read())
		rdioqueries = []
		for album in json_data["albums"]["album"]:
			rdioqueries.append(album["name"] + " " + album["artist"]["name"])
		print rdioqueries
		return rdioqueries


querier = LastfmQuery()
querier.getAlbums('jaisrael')



