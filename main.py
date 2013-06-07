import rdio

def main():
	rdio_api = rdio.RdioAPI()
	authorization_url = rdio_api.authorization_url  # use this url for rdio button
	# user will click rdio button, get pin from rdio, and give us pin
	# pin = get pin from user
	rdio_api.authorize_user_with_pin(pin)
	rdio_api.exchange_request_token_for_access_token()
    # ready to make authrorized calls, example call:
    # rdio_api.add_to_collection(list_of_artists, type="Album")

if __name__ == "__main__":
    main()