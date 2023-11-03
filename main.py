from fastapi import FastAPI , WebSocket, WebSocketDisconnect
from dbconexion import sql_susto

app = FastAPI()

websockets = []

@app.get("/")
async def raiz():
    return {"mensaje": 'https://www.youtube.com/watch?v=pRVV8rkmZEo&pp=ygUVYXF1aSBlc3BhbnRhbiB0YW4gdGFu'}

@app.post("/Nueva_dedicatoria")
async def nueva_dedicatoria():
    try:
        for usuario in websockets:
            usuario.send_text('recargar')
    except:
        websockets.remove(websockets)
    return 

@app.websocket('/websocket')
async def websocket_manager(websocket:WebSocket):
    await websocket.accept()
    websockets.append(websocket)
    try:
        while True:
            pass
    except WebSocketDisconnect:
        print("se desconecto")
