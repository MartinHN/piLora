from websocket import create_connection, WebSocketTimeoutException


ws =create_connection("ws://localhost:3003")
ws.timeout = 1

def sendToWs(args):
    try:
        msg=json.dumps({'addr':'server','args':args},separators=(',', ':'))
        print("[ws] sending : ",msg)
        ws.send(msg)
    except Exception as error:
        print('!!!![ws] send error : ',error)

def handleWs(msgCb):
    try :
        data = ws.recv()
        if data :
            msgCb(data)
    except WebSocketTimeoutException as _:
        pass
    except Exception as error:
        print('!!!![ws] send error : ',error)
