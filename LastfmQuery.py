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
		if json_data["albums"].keys().count("album") == 0:
			return rdioqueries
		for album in json_data["albums"]["album"]:
			rdioqueries.append(album["artist"]["name"])
		return rdioqueries

	def getPlaylists(self,user):
		response = urllib2.urlopen(baseURL+"?method=user.getPlaylists"+"&api_key="+api_key+"&user="+user+"&format="+format)
		json_data = json.loads(response.read())
		rdioqueries = {}
		if json_data["playlists"].keys().count("playlist") == 0:
			return rdioqueries
		for playlist in json_data["playlists"]["playlist"]:
			url = playlist["url"]
			page = urllib2.urlopen(url).read()
			found = True
			find_index = 0
			index = 0
			length = len(page)
			rdioqueries[playlist["title"]] = []
			while index < int(playlist["size"]):
				# get artist name
				find_index = page.find("<a href=\"/music/",find_index,length)
				find_index += 1
				artist = page[page.find(">",find_index,length)+1:page.find("<",find_index,length)]

				# get track name
				find_index = page.find("<a href=\"/music/",find_index,length)
				find_index += 1
				track = page[page.find(">",find_index,length)+1:page.find("<",find_index,length)]

				# advance to next track
				find_index = page.find("<a href=\"/music/",find_index,length)
				find_index += 1
				index+=1

				rdioqueries[playlist["title"]].append(artist + " " + track)
		return rdioqueries




