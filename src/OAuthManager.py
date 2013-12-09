import oauth2 as oa
import JSONFormatter

class OAuthManager:	
	def TwitterClient(self, Key, SecretKey, oauthToken, oauthTokenSecret):
		# Create Consumer Object
		Consumer = oa.Consumer(key=Key, secret=SecretKey)	
		Token = oa.Token(key = oauthToken, secret = oauthTokenSecret)		
		client = oa.Client(Consumer, Token)
				
		return client
	
	def GoogleAuth(self):
		print "Stub"