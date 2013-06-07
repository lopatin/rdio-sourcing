import rdio
import LastfmQuery

def main():
	rdio_api = rdio.RdioAPI()
	# use this url for rdio button
	authorization_url = rdio_api.authorization_url  
	
	# at this point, user will click rdio button, get pin from rdio, and give us pin
	
	pin = rdio_api.get_pin()   # prompts in terminal for now until we link with buttons
	rdio_api.authorize_user_with_pin(pin)
	rdio_api.exchange_request_token_for_access_token()
	# ready to make authrorized calls, example call:
	rdio_api.make_authenticated_call()
	# rdio_api.add_to_collection(list_of_artists, type="Album")
	
	lastfm = LastfmQuery.LastfmQuery()
	lastfm_list_of_artists = lastfm.getAlbums("jaisrael")
	rdio_api.add_to_collection(lastfm_list_of_artists, type="Album")

	# for playlists
	lastfm_list_of_playlists = lastfm.getPlaylists("jaisrael")
	# rdio api create playlists

if __name__ == "__main__":
	main()
