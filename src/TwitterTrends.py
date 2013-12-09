import urllib2
import JSONFormatter
import OAuthManager
import time

class TwitterTrends:
	"""Responsible Find Twitter Trends, search for tweets corresponding to those trends"""
	jsonFormat = JSONFormatter.JSONFormatter()	
	
	# Twitter Authentication Credetials
	Key = "RrE4H0xX9VhV0AmGiPXU8w"
	SecretKey = "qhlBUprDscYW6UDdeGWHb42KrpM42lvBR3ILpl3do"	
	Token = "2210480120-0hoewXx61WVw3Q5Cnm1GsmXbGl8j3NdJQBOVZ35"
	TokenSecret = "WBd0E5I78hOK6IJ6o4I2vF6yurHMVQRxHG4OVu2PdXP5S"
	
	# Data Objects
	locationsDict = dict()
	locationsFile = 'locFile.txt'
	trendsList = list()
	trendsFile = 'twitterTrendsFile.txt'
	twitterClient = None
	
	def __init__(self):
		self.Authenticate()
		try:
			with open(self.locationsFile, 'r') as f:				
				self.LoadLocations(f)
				print "Locations Loaded from file"
		except IOError:
			print "Locations will be downloaded from internet"
			self.GetLocations()

		try:
			with open(self.trendsFile, 'r') as f:				
				self.LoadTrends(f)
				print "Trends Loaded from file"
		except IOError:
			print "Trends will be downloaded from internet"
			self.GetTrends()

	def Authenticate(self):
		self.twitterClient = OAuthManager.OAuthManager().TwitterClient(self.Key, self.SecretKey, self.Token, self.TokenSecret)

	def LoadLocations(self, f):
		for line in f:
			code = line.split(',')[0]
			loc = line.split(',')[1]
			self.locationsDict[code] = loc				
		
	def GetLocations(self):
		locationsURL = ('https://api.twitter.com/1.1/trends/available.json')
		print "Query for: " + locationsURL
		resp, content = self.twitterClient.request(locationsURL)		
		if ('errors' in content):
			print "Sleep 60 Seconds..."
			time.sleep(60)
		self.locationsDict = JSONFormatter.JSONFormatter().GetLocationsAndCodes(content)
		
		# Write locations to file
		with open(self.locationsFile, 'w') as f:
			for code, state in self.locationsDict.iteritems():
				f.write(str(code) + ',' + state + '\n')			
			f.close()
	
	def LoadTrends(self, f):	
		for line in f:
			self.trendsList.append(line)

	def GetTrends(self):
		if (self.locationsDict is not None):
			for code, state in self.locationsDict.iteritems():
				#print code + state
				trendsURL = "https://api.twitter.com/1.1/trends/place.json?id={0}".format(code)
				print "Query for URL: " + trendsURL
				resp, content = self.twitterClient.request(trendsURL)
				if ('errors' in content):
					print "....Sleep 600 Seconds...."
					time.sleep(600)
				else:
					self.trendsList.extend(JSONFormatter.JSONFormatter().ExtractTrends(content))
						
			with open(self.trendsFile, 'w') as f:
				for item in self.trendsList:
					f.write(item+"\n")
				f.close()
		else:
			print "Error: No location were found..."		
	
		
	def PerformTweetSearch(self):
		tweets = list()
		for hashtag in self.trendsList[0:10]:
			tweetsSearch = "https://api.twitter.com/1.1/search/tweets.json?q={0}".format(hashtag)
			print "Query for URL: " + tweetsSearch
			resp, content = self.twitterClient.request(tweetsSearch)
			print resp
			print content
			if ('errors' in content):
				print content + "....Sleep 60 Seconds..."
				#time.sleep(60)
			else:
				tweets.extend(JSONFormatter.JSONFormatter().ExtractURLsFromTweets(content))
				print tweets
		
		with open('tweets.txt', 'w') as f:
			for tweet in tweets:
				f.write(tweet)
		
		
	def Test(self):
		trendsURL = "https://api.twitter.com/1.1/trends/place.json?id=1"
		print "Query for URL: " + trendsURL		
		resp, content = self.twitterClient.request(trendsURL)
		self.trendsList = JSONFormatter.JSONFormatter().ExtractTrends(content)		
		f = open('C:\\myfile.txt','w')			
		for hashtag in self.trendsList:
			tweetsSearch = "https://api.twitter.com/1.1/search/tweets.json?q={0}".format(hashtag)
			print "Query for URL: " + tweetsSearch
			resp, content = self.twitterClient.request(tweetsSearch)
			f.write(content) 
		f.close()
		
