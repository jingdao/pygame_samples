import urllib.request
import re

def web_search(query):
	request = urllib.request.urlopen('https://en.wikipedia.org/wiki/'+query)
	for l in request:
		if l.startswith(b'<p>'):
			l = l.decode("utf-8")
			l = re.sub('<.*?>','',l)
			l = re.sub('&.*?;','',l)
			l = l.replace('\n','')
			print(l)
			break

web_search('Boris_Johnson')
web_search('United_Kingdom')
web_search('Parliament')
