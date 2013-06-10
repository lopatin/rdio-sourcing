import unicodedata

from rdio import Rdio
import LastfmQuery

def main():
	CONSUMER_KEY, CONSUMER_SECRET = get_consumer_credentials()
	rdio = Rdio((CONSUMER_KEY, CONSUMER_SECRET))
	auth_url = rdio.begin_authentication('oob')

	# redirect user to rdio, will give pin back

	verifier = get_pin(auth_url)
	saved_token = rdio.token # a two element tuple
	rdio.complete_authentication(verifier)

	print "fetching last fm artists..."
	lastfm = LastfmQuery.LastfmQuery()
	lastfm_list_of_artists = lastfm.getAlbums("jaisrael")
	
	print "adding artists to collection..." 
	for artist in lastfm_list_of_artists:
		try:
			response = rdio.call('search', {'query':artist, 'types':'Artist'})		
		except UnicodeEncodeError:
			print "unicode issue. skipping this artist"
			continue
	
		artist_key = response['result']['results'][0]['key']
		if artist_key is not None:
			track_objs = rdio.call('getTracksForArtist', {'artist':artist_key})['result']
			track_keys_unicode_list = [ track['key'] for track in track_objs ]
			if track_keys_unicode_list is not None:
				# convert track keys to unicode
				track_keys_ascii_list = [ unicodedata.normalize('NFKD', u).encode('ascii','ignore') for u in track_keys_unicode_list ]
				track_keys_str = ""
				for u in track_keys_ascii_list:
					track_keys_str += u + ","
				if track_keys_str.endswith(','):
					track_keys_str = track_keys_str[:-1]
				atc = rdio.call('addToCollection', {'keys':track_keys_str})

def get_consumer_credentials():
	f = open('config', 'r')
	CONSUMER_KEY = f.readline().strip()
	CONSUMER_SECRET = f.readline().strip()
	return CONSUMER_KEY, CONSUMER_SECRET

def get_pin(auth_url):
	print 'Authorize this application at: %s' % (auth_url)
	oauth_verifier = raw_input('Enter the PIN / OAuth verifier: ').strip()
	return oauth_verifier
if __name__ == "__main__":
	main()
