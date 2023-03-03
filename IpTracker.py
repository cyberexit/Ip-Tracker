import os
from urllib.request import urlopen
import json
import time
import sys
def Bannar4 ():
	print ("\033[31m#############################################################")
	print ("\033[31m# \033[33m\033[1mIp Tracker		                         	    \033[31m#")
	print ("\033[31m# \033[33m\033[1mAccurate IP tracking Tool	                 	    \033[31m#")
	print ("\033[31m# \033[33m\033[1mAuthor: Are you ready soldiers 		            \033[31m#")
	print ("\033[31m# \033[33m\033[1mGitHub: https://github.com/cyberexit/Ip-Tracker           \033[31m#")
	print ("\033[31m# \033[33m\033[1mVersion: 1.0.1			            	    \033[31m#")
	print ("\033[31m#############################################################")
def Ip1 ():
    print ("   \033[31m\033[1mQuery      : \033[33m" + values['query'])
    print ("   \033[31m\033[1mStatus     : \033[33m" + values['status'])
    print ("   \033[31m\033[1mCountry    : \033[33m" + values['country'])
    print ("   \033[31m\033[1mRegionName : \033[33m" + values['regionName'])
    print ("   \033[31m\033[1mCity       : \033[33m" + values['city'])
def Link1 ():
	os.system('xdg-open https://facebook.com/groups/658498695902684/')
def Link2 ():
	os.system('xdg-open https://facebook.com/groups/658498695902684/')
def Tap ():
	print ("Tap Enter Auto Track Your IP Address")
	print ()
def Ip2 ():
    print ("   \033[31m\033[1mZipCode    : \033[33m" + values['zip'])
    print ("   \033[31m\033[1mIsp        : \033[33m" + values['isp'])
    print ("   \033[31m\033[1mOrg        : \033[33m" + values['org'])
    print ("   \033[31m\033[1mAs         : \033[33m" + values['as'])
    print ("   \033[31m\033[1mRegion     : \033[33m" + values['region'])
def Bannar1 ():
	print ('\033[36m')
	os.system('figlet -f slant S O L D I E R')
def Bannar2 ():
	os.system('figlet  IP T R A C K E D')
	print ("\033[34m   {\033[31m\033[1m========================================\033[34m}")
def Bannar3 ():
	print ("\033[33m")
	os.system('figlet -f slant IP ADDRESS')
	print ()
def Thanks ():
	os.system('figlet -f slant T H A N K S')

def Clear ():
	os.system('clear')
def With ():
	print ('\033[33mwait....')
Clear ()
Bannar1 ()
Bannar4 ()
while True:
    a = input('\n\n\n \033[35m Enter username:')
    b = 'Go to hell'
    x = input('\n\n\n  \033[35mEnter password:')
    z = 'soldier'
    if x == z:
        time.sleep(0.1)
        break 
    else:
        wr = '\n\033[31m  Wrong password entered'
        for i in wr:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.07)
        os.system('clear')
        Bannar1 ()
        Bannar4 ()
Link2 ()
Clear()
Bannar3 ()
Tap ()
def Ip3 ():
	print ("   \033[31m\033[1mOrg        : \033[33m" + values['geo'])
while True:
    ip=input("\033[31mTargeted ip:\033[32m")
    With ()
    Link2 ()
    url = "http://ip-api.com/json/"
    response = urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    Clear()
    Bannar2 ()
    Ip1 ()
    Ip2 () 
    break
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome To Hackers World            |
|             Joine Our Facebook Group            |
|             Are you ready soldiers              |
| Watch Ours Tutorials For Learn Ethical Hacking  |''')
print("+-------------------------------------------------+")

os.system("xdg-open https://facebook.com/groups/658498695902684/")
