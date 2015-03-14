import re, urllib

html = urllib.urlopen("http://www.yes24.com/").read(20000)
linklist = re.findall('<a href="(.*?)">.*?</a>',html)
for link in linklist :
    print link.split(" ")[0]
    #print link