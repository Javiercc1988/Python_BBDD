#!/usr/bin/python3

import sqlite3, logging,csv

logging.basicConfig(filename="error.log")

print("Content-Type: text/html\r\n\r\n")

try:
	conexion = sqlite3.connect("./bbdd/registro.sqlite")
	cursor = conexion.cursor()
	
	cursor.execute("SELECT * FROM PRODUCTOS")
	lista = cursor.fetchall()
	for i in lista:
		print("Producto:",i)
		
	conexion.commit()	
	cursor.close()
	conexion.close()
		
except Exception as e:
	logging.error("\n\n Error en la BBDD \n\n", exc_info=True)
