import urllib2


# Check if you can connect to the video conferencing tool.

class TestCase_1:

	def internet_on(self):
	    try:
	        response=urllib2.urlopen('http://192.168.202.114',timeout=1)
	        return "Pass"
	    except urllib2.URLError as err: pass
	    return "Fail"