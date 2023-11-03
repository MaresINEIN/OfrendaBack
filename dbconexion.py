import mysql.connector
from pydantic import BaseModel,validator
from funciones import crear_directorio,almacena_imagen,recupera_imagen
import random

def no_esta_vacio(valor):
    if not isinstance(valor, bool) and not valor.strip():
        raise ValueError("El campo no debe estar vacío")
    return valor 

class dedicatorias(BaseModel):
    autor:str|bool =False
    img:str|bool=False
    mensaje:str|bool=False

    verifica =validator('mensaje','img')(no_esta_vacio)

class EspantanTan:
    def __init__(self,):
      self.conexion = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password='',
      )
      self.cursor = self.conexion.cursor()
      self.cursor.execute('CREATE DATABASE IF NOT EXISTS dedicatorias')
      self.cursor.execute('USE dedicatorias')
      crear_directorio()

      self.cursor.execute( '''
        CREATE TABLE IF NOT EXISTS dedicatorias (
        id VARCHAR(200) PRIMARY KEY, 
        autor VARCHAR(60) NOT NULL DEFAULT 'Anonimo',
        texto VARCHAR(700) NOT NULL,
        imagen VARCHAR(100) NOT NULL DEFAULT False
            ) ENGINE = InnoDB;
        ''')
      self.conexion.commit()

    def ingresar_dedicatoria(self,dedicatoria:dedicatorias):
      id = str(random.randint(1,900))
      if not dedicatoria.autor:
        dedicatoria.autor = "anonimo"
      aux_img = dedicatoria.img
      if not aux_img:
          dedicatoria.img="/"
      else:
        dedicatoria.img = f"/img/{dedicatoria.autor}_{id}.txt"
      sql = f"INSERT INTO dedicatorias (id,autor,texto,imagen) VALUES ('{id}','{dedicatoria.autor}','{dedicatoria.mensaje}','{dedicatoria.img}')"
      try:
          self.cursor.execute(sql)
          if dedicatoria.img !="/":
            if not almacena_imagen(aux_img,f"{dedicatoria.autor}_{id}"):
              return Exception("No se logro almacenar la imagen")
          self.conexion.commit()
          return True
      except Exception as e:
          print(e)
          return False
      
    def obtener_dedicatorias(self):
      dedicatoria_sql = []
      sql="SELECT * FROM  dedicatorias"
      try:
          self.cursor.execute(sql)
          result = self.cursor.fetchall()
          for i in result:
            dedicatorias_data = dict(zip(self.cursor.column_names, i))
            if dedicatorias_data["imagen"] != "/":
              dedicatorias_data["imagen"] = recupera_imagen(f"{dedicatorias_data['autor']}_{dedicatorias_data['id']}")
            else:
              pass
            dedicatoria_sql.append(dedicatorias_data)
          return dedicatoria_sql
      except:
          return False




sql_susto = EspantanTan()