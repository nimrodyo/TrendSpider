"""
TrendsSpider is a Python system dediacted to search for trends in Twitter, Google and other web platforms.
Every after extracting trends from every platform the system will search those trends in the socail nets
and look for URLs, PDF, EXE, and Office files with the goal of finding viruses & exploits.
"""

import GoogleTrends
import TwitterTrends


tt = TwitterTrends.TwitterTrends()
tt.PerformTweetSearch()

#tt.Test()