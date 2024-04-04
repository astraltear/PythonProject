import http.client
from urllib.request import urljoin,urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser
import os

class ImageParser2(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result=[]
            print(self.result)
            
        for name,value in attrs:
            if name == 'src':
                self.result.append(value)
                print(self.result)
    
def downloadImage(srcUrl,data):
        if not os.path.exists('DOWNLOAD'):
            os.makedirs('DOWNLOAD')
        
        parser = ImageParser2()
#         print(data)
        parser.feed(data)
        resultSet = set(x for x in parser.result)
         
        for x in sorted(resultSet):
            src = urljoin(srcUrl, x)
            basename = os.path.basename(src)
            targetFile = os.path.join('DOWNLOAD',basename)
             
            print("Downloading...",src)
            urlretrieve(src, targetFile)

def main():
    host="www.google.co.kr"
    
    conn = http.client.HTTPConnection(host)
    conn.request("GET", '')
    resp = conn.getresponse()
    data = resp.read().decode(resp.headers.get_content_charset())
    conn.close()
    
    url = urlunparse(('http',host,'','','',''))
    print(url)
    
    downloadImage(url,data)
    
    
    
if __name__ =='__main__':
    main()