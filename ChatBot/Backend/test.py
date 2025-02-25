import asyncio
import websockets
import os



async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        await websocket.send('[END]')
    
async def main():
    async with websockets.serve(
        echo , 
        "localhost",
        int(os.environ.get('PORT', 8090))
    ):
        await asyncio.Future()



if __name__ == '__main__':
    asyncio.run(main())