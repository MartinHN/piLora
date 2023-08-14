import sys
import os
import socket
import rw

client_sock=None
e32_sock=None
csock=None

def close_sock():
    """ close the socket and delete the file """
    global client_sock
    global csock

    print("closing client socket", client_sock)

    csock.close()
    if os.path.exists(client_sock):
        rw.setRW(True)
        os.remove(client_sock)
        rw.setRW(False)

def initSocks( csockpath,esockpath):
    global client_sock
    global csock
    global e32_sock
    client_sock = csockpath
    e32_sock = esockpath
    if os.path.exists(client_sock):
        os.remove(client_sock)

    csock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    print("binding socket", client_sock)
    csock.bind(client_sock)

    print("registering socket", e32_sock)
    csock.sendto(b'', e32_sock)
    (msg, address) = csock.recvfrom(10)

    if msg[0] != 0:
        print("unable to register client")
        sys.exit(1)
    else:
        print("client registered")


def sendToLora(msg):
    global csock
    csock.sendto(msg, e32_sock)
    (msg, address) = csock.recvfrom(512)
    if len(msg) == 1 and msg[0] == 0:
        pass # print("success! received 1 byte from socket", address)
    else:
        print("!!![lora] failed to send data. len:", len(msg))

def sendAck(msg):
    sendToLora(msg)
    print ('sent ack')



def handleLora(msgCb):
    global csock
    # receive from the e32
    try:
        csock.setblocking(False)
        (msg, address) = csock.recvfrom(59)
        csock.setblocking(True)
        msgCb(msg)
    except BlockingIOError as e: 
        pass
    except Exception as e :
        print ("got ex")
        print(e)
    finally:
        csock.setblocking(True)
    
