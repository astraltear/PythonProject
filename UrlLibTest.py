import urllib.request, urllib.error,urllib.parse
print( urllib.request.urlopen("http://www.google.com").read() )