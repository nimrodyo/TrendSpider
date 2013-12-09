import json
import urllib2 

class JSONFormatter:
	"""Uses simplejson class to format JSON responses"""
	def GetLocationsAndCodes(self, locationsJson):
		if (locationsJson is not None):
			locationsDict = dict()
			locations = json.loads(locationsJson)
			if ('errors' in locations):
				print "Error: "
				print locations['errors']
			else:			
				for item in locations:			
					state = item['name'].encode("utf-8")
					code = item['woeid']
					locationsDict[code] = state				
				return locationsDict			
		else:
			print "Locations JSON in None"
			return None
	
	def ExtractTrends(self, trendsJson):
		trendsList = list()
		if (trendsJson is not None): 
			trends = json.loads(trendsJson)
			if ('errors' in trends):
				print "Error: "
				print trends['errors']
			else:
				for item in trends[0]['trends']:
					trend = urllib2.unquote(item['query'].encode("utf-8"))			
					trendsList.append(trend)
					#print trend
				return trendsList		
		return trendsList
	
	def ExtractURLsFromTweets(self, tweetsJson):
		return tweetsJson
