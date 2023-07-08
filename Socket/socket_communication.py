import websockets
import asyncio
import random


PORT = 12000
palavra = "teste"
print("Started server and listening on Port" + str(PORT))

connected = set()


async def echo(websocket, path):
    print("A client just connected")
    connected.add(websocket)
    while True:
        try:
            async for message in websocket:
                #print("received message from the client: " + message)            
                for conn in connected:
                    if conn != websocket:
                        await conn.send(message)               
                     
        
                 
        except websocket.exceptions.ConnectionClosed as e:
            print ("A client just disconnceted")
            await websocket.connect()
            continue
        


start_server = websockets.serve(echo, "127.0.0.1" , PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()







