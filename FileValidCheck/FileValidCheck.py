# -*- coding: utf-8 -*-
import DBUtil
from ftplib import FTP
import smtplib

MAIL_SERVER = "111.222.333.444"

HOST="yourdomain.co.kr"
PORT=20021
USERID="user"
PASSWORD="pwd"

M_HOST="yourdomain.co.kr"
M_PORT=9921
M_USERID="userid"
M_PASSWORD="pwd"

STREAM_HEADER="/AOD/"
DOWN_AUDIEN_HEADER="/DN/down/"
DOWN_ASP_HEADER="/DN/down2/"
DOWN_MOBILE_HEADER="/DN/down3/"

senderMail=["abc@yourdomain.com","def@yourdomain.com","ghi@yourdomain.com"]

def dirSearch(header,file,void,ftp,isMobile,logFile):

    if isMobile=="W":
        prefix = header+file[:file.rfind("/")]
        dbFileName = file[file.rfind("/")+1:]
    elif isMobile=="S":
        prefix = header+void
        dbFileName = file[file.rfind("/")+1:]
        dbFileName = dbFileName[:dbFileName.rfind(".")+1]+"mp4"
    else:
        prefix = header+void    
        dbFileName = file[file.rfind("/")+1:]
    
    try:
        ftp.cwd(prefix)
        currentFtpList = ftp.nlst()
        if dbFileName not in currentFtpList :
            dbFileName = dbFileName.replace("mp3","MP3")
            if dbFileName not in currentFtpList :
                #print void,dbFileName,prefix    # ������ �������� �ʴ´�. 
                logFile.write("["+void+"]["+prefix+"]["+dbFileName+"]\n")
            
    except Exception, e:
        #print e,prefix    # ��ΰ� �������� �ʴ´�. 
        logFile.write(e)

ftp_down = FTP()
ftp_down.connect(HOST, PORT)
ftp_down.login(USERID, PASSWORD, "")

ftp_msteam = FTP()
ftp_msteam.connect(M_HOST, M_PORT)
ftp_msteam.login(M_USERID, M_PASSWORD, "")

liveVolumeTuple = DBUtil.getLiveVolume()

logFile = open("filecheck.log",'w')

if liveVolumeTuple.__len__() ==0 :
    logFile.write("DATA NOT FOUND")
else:
    for row in liveVolumeTuple:
        void,mp3,wma = row
        
        # streaming
        dirSearch(STREAM_HEADER,wma,void,ftp_down,"W",logFile)
        
        # asp down mp3, wma    
        dirSearch(DOWN_ASP_HEADER,mp3,void,ftp_down,"W",logFile)
        dirSearch(DOWN_ASP_HEADER,wma,void,ftp_down,"W",logFile)
        
        # mobile down
        dirSearch(DOWN_MOBILE_HEADER,mp3,void,ftp_down,"M",logFile)
        # mobile stream
        dirSearch("/",mp3,void,ftp_msteam,"S",logFile)
        
        # audien down mp3, wma    
        dirSearch(DOWN_AUDIEN_HEADER,mp3,void,ftp_down,"W",logFile)
        dirSearch(DOWN_AUDIEN_HEADER,wma,void,ftp_down,"W",logFile)

logFile.flush()
logFile.close()

logFile = open("filecheck.log",'r')
lines = logFile.readlines()
isError =False
mSg=" "
for line in lines: 
    if line=="DATA NOT FOUND" :
        break
    else :
        isError=True
        mSg +=line
        
if isError:
    s = smtplib.SMTP(MAIL_SERVER)
    message = 'Subject: %s\n\n%s' % ("���ϴ���", mSg)
    for sender in senderMail:
        s.sendmail("zert@yourdomain.com",sender,message)
    

ftp_down.quit()
ftp_down.close()

ftp_msteam.quit()
ftp_msteam.close()
