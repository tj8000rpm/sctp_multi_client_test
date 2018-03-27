#!/usr/bin/env python

import socket
import sctp
import datetime
import sys
from time import *

server=("" , int(sys.argv[1]))

sk = sctp.sctpsocket_tcp(socket.AF_INET)
#sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sk = sctp.sctpsocket_udp(socket.AF_INET)
sk.bind(server)

while True:
    print('listening')
    sk.listen(5)
    c, addr = sk.accept()
    print('receiving')
    print(c.recv(4096))
    print('sending')
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    try:
        c.send(now)
    except :
        pass
    finally:
        c.close()
s.close()
