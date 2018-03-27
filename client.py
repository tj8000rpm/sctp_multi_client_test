#!/usr/bin/env python

import socket
import sctp
import time
import threading
import random

sk=None

client=("127.0.0.1" , 3868)
try:
    sk = sctp.sctpsocket_udp(socket.AF_INET)
    sk.bind(client)
except:
    if sk:
        sk.close()

servers=[("127.0.0.1" , 3869),("127.0.0.1" , 3870)]

def gothread(server):
    time.sleep(random.random()*3)
    print "send to {}".format(server)
    sk.sendto("hi",server)
    msg=sk.recv(1500*3)
    print msg
    time.sleep(random.random()*3)

try:
    ths=[]
    for server in servers:
        th=threading.Thread(target=gothread,args=(server,))
        th.start()
        ths.append(th)
    for th in ths:
        th.join()

finally:
    if sk:
        sk.close()
