from fastapi import FastAPI, HTTPException
from dbconexion import dedicatorias, sql_susto

app = FastAPI()



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
    return {"message": "Dedicatoria registrada con exito", 'status': 'success'}

@app.get("/Obtener_dedicatorias")
async def obtener_dedicatorias():
    return sql_susto.obtener_dedicatorias()