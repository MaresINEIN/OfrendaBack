
import os

def crear_directorio()->bool:   
    directorio = os.getcwd()+ "\img"
    try:
        if not os.path.exists(directorio):
            os.mkdir(directorio)
        return True
    except:
        return False

def almacena_imagen(data_ima: str, nombre: str)->str:
    directorio_logo = os.getcwd() + "\img"
    file_logo = nombre+".txt"
    path = os.path.join(directorio_logo, file_logo)
    with open(path, "w") as file_logo:
        file_logo.write(data_ima)
    return directorio_logo

def recupera_imagen(nombre:int)->str|bool:
    txt_filename = os.getcwd()+f"/img/{nombre}.txt"
    try:
        with open(txt_filename, "r") as txt_file:
            data_url = txt_file.read()
        return data_url
    except Exception as e:
        print(e)
        return False
