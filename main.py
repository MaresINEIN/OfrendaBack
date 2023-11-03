from fastapi import FastAPI
from dbconexion import sql_susto

app = FastAPI()

@app.get("/")
async def raiz():
    return {"mensaje": 'https://www.youtube.com/watch?v=pRVV8rkmZEo&pp=ygUVYXF1aSBlc3BhbnRhbiB0YW4gdGFu'}

@app.post("/Nueva_dedicatoria")
async def nueva_dedicatoria():
    return 