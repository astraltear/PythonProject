from urllib.request import urlopen
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result=[]
            
        for name,value in attrs:
            if name == 'src':
                self.result.append(value)
    
def parseImage(data):
        parser = ImageParser()
        parser.feed(data)
        dataSet = set(x for x in parser.result)
        
        

def main():
    url="http://www.google.com"
    f = urlopen(url)
    print(type(f))
    
    #data = f.read()
    data = f.read().decode(f.headers.get_content_charset())
    print(data)
    parseImage(data)
    
    #print(f.read())
    #print(f.headers.get_content_charset())
    
    #charset = f.info() .getparam('charset')
    #data = f.read().decode(charset)
    #print(data)
    
    
if __name__ =='__main__':
    main()