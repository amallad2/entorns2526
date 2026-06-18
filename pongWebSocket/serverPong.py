import asyncio
import json
import websockets

PORT = 10040

players = {}  # { websocket: {'y': int, 'number': int} }
ball = {'x': 400, 'y': 300, 'vx': 4, 'vy': 3}

async def game_loop():
    while True:
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']

        # Rebote en bordes verticales
        if ball['y'] <= 0 or ball['y'] >= 600:
            ball['vy'] *= -1

        # Reinicio si sale por los lados
        if ball['x'] <= 0 or ball['x'] >= 800:
            ball['x'], ball['y'] = 400, 300
            ball['vx'] *= -1

        # Enviar estado a todos los jugadores
        state = {
            'players': {str(i): p['y'] for i, p in enumerate(players.values())},
            'ball': ball
        }

        for ws in players.keys():
            try:
                await ws.send(json.dumps(state))
            except:
                continue

        await asyncio.sleep(1/60)

async def handler(websocket):
    # Registrar jugador
    if len(players) >= 2:
        await websocket.send(json.dumps({'error': 'Sala llena'}))
        await websocket.close()
        return

    player_number = len(players)
    players[websocket] = {'y': 250, 'number': player_number}

    try:
        async for message in websocket:
            data = json.loads(message)
            players[websocket]['y'] = data['y']
    finally:
        del players[websocket]

async def main():
    server = await websockets.serve(handler, "0.0.0.0", PORT)
    print(f"Servidor WebSocket en puerto {PORT}")
    await asyncio.gather(server.wait_closed(), game_loop())

asyncio.run(main())
