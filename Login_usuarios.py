#!/usr/bin/python3

import sqlite3, logging,cgi,smtplib,ssl

logging.basicConfig(filename="error.log")

try:
	form = cgi.FieldStorage()

	name=form.getvalue("name")
	passw=form.getvalue("password")

except Exception as e:
	logging.error("\n\n Error en EL FORMULARIO \n\n", exc_info=True)


#### BBDD ####
try:
	
	tipo = "cliente"
	conexion = sqlite3.connect("./bbdd/registro.sqlite")
	cursor = conexion.cursor()
	
	cursor.execute("SELECT * FROM USUARIOS WHERE NOMBRE='{}' AND PASSWORD='{}'".format(name,passw))
	lista = cursor.fetchall()
	
	conexion.commit()
	
	if len(lista) < 1:
		print("Location: http://nombrealumnob1.2daw.local/error.html")
		print("")
	else:
		cursor.execute("SELECT * FROM USUARIOS WHERE NOMBRE='{}' AND TIPO='{}'".format(name,tipo))
		lista2 = cursor.fetchall()
		
		conexion.commit()
		
		if len(lista2) <1:
			print("Location: http://nombrealumnob1.2daw.local/empleado.html")
			print("")
		else:
			print("Location: http://nombrealumnob1.2daw.local/pagina_cliente.html")
			print("")
		
	cursor.close()
	conexion.close()
	
except Exception as e:
	logging.error("\n\n Error en la BBDD \n\n", exc_info=True)


