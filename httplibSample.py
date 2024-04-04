import http.client

host ="www.google.com"

conn = http.client.HTTPConnection(host)
conn.request('GET','')
resp = conn.getresponse()
print(resp.read().decode( resp.headers.get_content_charset() ))
