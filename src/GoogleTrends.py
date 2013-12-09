import urllib2
import JSONFormatter

class GoogleTrends:
	"""Responsible for bringing Google Trends results"""
	urlConst = ('http://www.google.com/trends/fetchComponent?q={0}&cid={1}&export={2}')
	
	#urlConst.format(q, cid, exType)
	
