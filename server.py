from asyncio.events import get_event_loop
import asyncio
import websockets
import json


  
async def echo(websocket, path):
    async for message in websocket:
        data = message.split('~~')
        print(data)
        with open('messages.json' , 'r') as f:
            msg = json.load(f)
        dnt = data[0].split()
        if f'_{dnt[0]}' not in msg:
            msg[f'_{dnt[0]}']  = {}
        elif f'_{dnt[1]}' not in msg[f'_{dnt[0]}']:
            msg[f'_{dnt[0]}'][f'_{dnt[1]}'] = {}
            print('elif')
        else:
            msg[f'_{dnt[0]}'][f'_{dnt[1]}'] = {
                'message' : data[2],
                'client' : data[1],
                'date'  : dnt[0],
            }
            
            print('f')
        print(msg)
        
        with open("messages.json", "w") as f:
            json.dump(msg, f)
            
        await websocket.send(message)
    
   
        

start_server = websockets.serve(echo, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()