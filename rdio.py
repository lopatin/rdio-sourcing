#!/usr/bin/env python
import oauth2 as oauth
import urllib, cgi

class RdioAPI(object):
    
    def __init__(self):
        self.consumer = self.create_consumer()
        self.client = self.create_client()
        self.request_token, self.parsed_content = get_request_token()
        self.authorization_url = create_authorization_url()
        # wait for user to give me pin to create access_token
       	self.access_token = None
   
	def create_consumer(self):
		""" create the OAuth consumer credentials """ 
		CONSUMER_KEY, CONSUMER_SECRET = self.get_consumer_credentials()
		oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
		return consumer

	def get_consumer_credentials(self):
		f = open('config', 'r')
		CONSUMER_KEY = f.readline().strip()
		CONSUMER_SECRET = f.readline().strip()
		return CONSUMER_KEY, CONSUMER_SECRET
	
	def create_client(self):
		return oauth.Client(self.consumer)

	def get_request_token(self):
		response, content = self.client.request('http://api.rdio.com/oauth/request_token', 'POST', urllib.urlencode({'oauth_callback':'oob'}))
		parsed_content = dict(cgi.parse_qsl(content))
		request_token = oauth.Token(parsed_content['oauth_token'], parsed_content['oauth_token_secret'])
		return request_token, parsed_content

	def create_authorization_url(self):
		return '%s?oauth_token=%s' % (self.parsed_content['login_url'], self.parsed_content['oauth_token'])
	
	def authorize_user(self, pin):
		self.authorize_user_with_pin(pin)
		self.exchange_request_token_for_access_token()
		self.create_client_token

	def authorize_user_with_pin(self, oauth_verifier): 
		self.request_token.set_verifier(oauth_verifier)

	def exchange_request_token_for_access_token(self):
		""" upgrade the request token to an access token """
		self.client = self.upgrade_client_to_use_request_token()
		response, content = self.client.request('http://api.rdio.com/oauth/access_token', 'POST')
		parsed_content = dict(cgi.parse_qsl(content))
		self.access_token = oauth.Token(parsed_content['oauth_token'], parsed_content['oauth_token_secret'])
		self.client = self.upgrade_client_to_use_access_token()

	def upgrade_client_to_use_request_token(self):
		return oauth.Client(self.consumer, self.request_token)

	def upgrade_client_to_use_access_token(self):
		return oauth.Client(self.consumer, self.access_token)

	def add_to_collection(self, obj_list, type):
		pass
		# for obj in obj_list:
			# search rdio
			# get top result and add to collection

		# example authorized request
		#response = client.request('http://api.rdio.com/1/', 'POST', urllib.urlencode({'method': 'currentUser'}))
		#print response[1]



