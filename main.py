#IMPORT REQUIRED CLASSES
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

#CREATE FASTAPI APP
app = FastAPI()

#CREATE A LIST TO STORE CONNECTED CLIENT
clients = []

#CREATE WEBSOCKET ENDPOINT
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
   
   #ACCEPT THE CONNECTION
    await ws.accept()

    #ADD CLIENT TO THE LIST
    clients.append(ws)

    try:

        #KEEP LISTENING FOREVER
        while True:
            data = await ws.receive_text()

            #BROADCAST DATA TO ALL CLIENTS
            for client in clients:
                await client.send_text(data)
                
    #HANDLE CLIENT
    except WebSocketDisconnect:
        clients.remove(ws)
