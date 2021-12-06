#!/usr/bin/python3

import sqlite3, logging

logging.basicConfig(filename="error.log")

try:
	conexion = sqlite3.connect("./bbdd/registro.sqlite")
	cursor = conexion.cursor()
	
	cursor.execute("""CREATE TABLE USUARIOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE VARCHAR(50),
	EMAIL VARCHAR(100),
	SEXO VARCHAR(15),
	PASSWORD VARCHAR(100),
	TIPO VARCHAR(50))""")
	
	conexion.commit()
	cursor.close()
	conexion.close()
	
except Exception as e:
	logging.error("\n\n Error en la BBDD \n\n", exc_info=True)
