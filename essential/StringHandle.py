# -*- coding: euc-kr -*-
x="37"
y="43"
z=x+y
print "str", z

z= int(x)+int(y)
print "int", z

s = str(z)
print "convert str function|", s
s = repr(z)
print "convert repr function|", s
s = format(z,"4d")
print "convert format function|", s

z= float(x)+float(y)
print "float", z

str = "아빠는거짓말쟁이야_01회.wma"
str=str.replace("mp3", "MP3").replace("wma", "WMA").replace("mp4", "MP4")
print str

str2="datafiles/201303/mp3/비행운_서른_01회.mp3"
str2=str2[str2.rfind("/")+1:]
str2=str2[:str2.rfind(".")+1]+"mp4"
print str2

eachLine="I tell you, theres no such thing as a flying circus."
print eachLine.find(":") 

str3 = 'python is powerful'
print (str3.endswith('ful'))
print (str3.endswith('M'))
print (str3.endswith('ful',10,-1))
print ( str3.find('sub') )  
#print ( str3.index('sub') ) # exception invoke
print ( str3.find('l') )
print ( str3.find('l',5,-1) )
print ( str3.isalnum() )

print ( ".".join("iterable") )
print ( "iterable".upper() )



