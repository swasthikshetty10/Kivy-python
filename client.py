import asyncio
import websockets
uri = "ws://localhost:8000"
name = 'clientname'
async def sendmsg():
    message = input()
    async with websockets.connect(uri) as websocket:
        await websocket.send(f'{name}~~{message}')
        x = await websocket.recv()
        print(x)
asyncio.get_event_loop().run_until_complete(sendmsg())
