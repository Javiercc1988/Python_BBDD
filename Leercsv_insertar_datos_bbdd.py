#!/usr/bin/python3

import sqlite3, logging,csv

logging.basicConfig(filename="error.log")

try:
	conexion = sqlite3.connect("./bbdd/registro.sqlite")
	cursor = conexion.cursor()
	
	listavacia=[]
	
	with open("productos.csv",newline="") as f:
		reader = csv.reader(f,delimiter=",")
		next(reader)
		for row in reader:
			listavacia.append(tuple(row))
	
	cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?,?)",listavacia)
	
	conexion.commit()	
	cursor.close()
	conexion.close()
		
except Exception as e:
	logging.error("\n\n Error en la BBDD \n\n", exc_info=True)
