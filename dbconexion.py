import mysql.connector 

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

      self.cursor.execute( '''
        CREATE TABLE IF NOT EXISTS dedicatorias (
        id VARCHAR(200) PRIMARY KEY, 
        autor VARCHAR(60) NOT NULL DEFAULT False,
        texto VARCHAR(700) NOT NULL,
        imagen VARCHAR(100) NOT NULL DEFAULT False
            ) ENGINE = InnoDB;
        ''')
      self.conexion.commit()

    def ingresar_dedicatoria(self, ):
      sql = "INSERT INTO dedicatorias (autor) "


sql_susto = EspantanTan()