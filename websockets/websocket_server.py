# import asyncio
# import websockets

# async def echo(websocket, path):
#     async for message in websocket:
#         print(f"Received message: {message}")
#         await websocket.send(f"Echo: {message}")

# start_server = websockets.serve(echo, "localhost", 6789)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

import asyncio
import websockets
import json

connected_clients = set()
total_messages = 0


async def echo(websocket, path):
    global total_messages
    if path == "/admin":
        # Handle the admin connection in a separate coroutine
        await admin_handler(websocket, path)
        return

    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")
            total_messages += 1
            # Update the admin clients with the new stats
            await update_admin_clients()
    finally:
        connected_clients.remove(websocket)
        # Update the admin clients with the new stats
        await update_admin_clients()


async def admin_handler(websocket, path):
    # Admin client connection will receive stats updates
    while True:
        try:
            stats = {
                "connected_clients": len(connected_clients),
                "total_messages": total_messages,
            }
            await websocket.send(json.dumps(stats))
            await asyncio.sleep(1)  # Update every second.
        except websockets.exceptions.ConnectionClosed:
            break


async def update_admin_clients():
    # Broadcast updated stats to all connected admin clients
    stats = json.dumps(
        {"connected_clients": len(connected_clients), "total_messages": total_messages}
    )
    for client in connected_clients:
        if client.path == "/admin":
            await client.send(stats)


start_server = websockets.serve(echo, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
