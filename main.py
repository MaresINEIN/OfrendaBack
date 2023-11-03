from fastapi import FastAPI , WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dbconexion import sql_susto,dedicatorias

app = FastAPI()

websockets = []

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados en las solicitudes
)

@app.get("/")
async def raiz():
    return {"mensaje": 'https://www.youtube.com/watch?v=pRVV8rkmZEo&pp=ygUVYXF1aSBlc3BhbnRhbiB0YW4gdGFu'}

@app.post("/Nueva_dedicatoria")
async def nueva_dedicatoria(dedicatoria:dedicatorias):
    if not dedicatoria.mensaje and not dedicatoria.img:
        raise HTTPException(status_code=404, detail="Se debe ingresar al menos un mensaje o una imagen")
    if dedicatoria.img and "data:image" not in dedicatoria.img:
        raise HTTPException(status_code=404,detail="La imagen debe estar en formato data:image")
    if not sql_susto.ingresar_dedicatoria(dedicatoria):
        raise HTTPException(status_code=404, detail="Ocurrio un error al ingresar dedicatoria")
    try:
        for usuario in websockets:
            await usuario.send_text('recargar')
    except Exception as e:
        print(e)
        websockets.remove(usuario)
    return {"message": "Dedicatoria registrada con exito", 'status': 'success'}

@app.get("/Obtener_dedicatorias")
async def obtener_dedicatorias():
    return sql_susto.obtener_dedicatorias()


@app.websocket('/websocket')
async def websocket_manager(websocket:WebSocket):
    await websocket.accept()
    websockets.append(websocket)
    try:
        while True:
            data = await websocket.receive_text() 
    except WebSocketDisconnect:
        websockets.remove(websocket)
        print("se desconecto")
