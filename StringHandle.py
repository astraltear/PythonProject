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

str = "�ƺ��°��������̾�_01ȸ.wma"
str=str.replace("mp3", "MP3").replace("wma", "WMA").replace("mp4", "MP4")
print str

str2="datafiles/201303/mp3/�����_����_01ȸ.mp3"
str2=str2[str2.rfind("/")+1:]
str2=str2[:str2.rfind(".")+1]+"mp4"
print str2

eachLine="I tell you, theres no such thing as a flying circus."
print eachLine.find(":") 