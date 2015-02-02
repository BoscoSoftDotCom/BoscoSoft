'''
Created on Jan 21, 2015

@author: gstumpf
'''
import socket
import smtplib
import time
import os
import sys
import traceback
import tempfile
import logging
from email.mime.text import MIMEText

def main (toEmailAddress):
    oldIPAddress = 'None'
    sleepSeconds = 60 #*15
    
    logging.debug('The Temp Dir Is ' +tempDir)
    
    cwd = os.curdir
    openFile = open(tempDir  + "/IPAddress.txt", "w+")
    writeFile = openFile.write('x')
    openFile.close()
    
    forever = 10
    now = 9
    while (now < forever):
        #only do this when the IP Address Has Changed
        hostName = socket.gethostbyname(socket.gethostname());
        if (hostName == 'localhost' or hostName == '127.0.0.1') :
                logging.debug('The Host Name Is ' +hostName)
                time.sleep(sleepSeconds)
                continue

        try:
            openFile = open(tempDir + "/IPAddress.txt", "r+")
            readFile = openFile.read()
            ipAddress = readFile
            #print('IP Address In File: ' + ipAddress)
            openFile.close()
            
            if (ipAddress == oldIPAddress) :
                time.sleep(sleepSeconds)
                continue
            
            msg = MIMEText(hostName)
            msg['Subject'] = 'IP Address'
            msg['From'] = toEmailAddress
            msg['To'] = toEmailAddress
            
            smtpserver = smtplib.SMTP('', 25)
            smtpserver.ehlo()
            #smtpserver.starttls()
            smtpserver.ehlo
            #smtpserver.login(gmail_user, gmail_password)
            
            smtpserver.sendmail(toEmailAddress, [toEmailAddress], msg.as_string())
            smtpserver.quit()
            logging.debug('Emailed Host ' + hostName)
            
            #print('IP Address Derived: ' + hostName)
            oldIPAddress = hostName
            
            openFile = open(tempDir + "/IPAddress.txt", "w+")
            writeFile = openFile.write(hostName)
            openFile.close()
    
            time.sleep(sleepSeconds)
    
        except:
            traceback.print_exc()
            logging.debug(traceback.print_exc())
            time.sleep(sleepSeconds)
        
if __name__ == "__main__":
    tempDir = tempfile.gettempdir()
    logging.basicConfig(filename= tempDir +'\\IPAddressNotifier.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',)
    logging.debug('Restarting ' + sys.argv[0])
    firstArg = sys.argv[1]
    main(firstArg)
    
        