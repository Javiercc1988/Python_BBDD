#!/usr/bin/python3

import sqlite3, logging,cgi,smtplib,ssl,csv

logging.basicConfig(filename="error.log")

try:
	form = cgi.FieldStorage()

	name=form.getvalue("name")
	email=form.getvalue("email")
	sexo=form.getvalue("radio")
	passw=form.getvalue("password")

except Exception as e:
	logging.error("\n\n Error en EL FORMULARIO \n\n", exc_info=True)


#### BBDD ####
try:
	users=[(name,email,sexo,passw,"cliente")]
	conexion = sqlite3.connect("./bbdd/registro.sqlite")
	cursor = conexion.cursor()
	
	cursor.executemany("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)",users)
	
	conexion.commit()
	cursor.close()
	conexion.close()
	
except Exception as e:
	logging.error("\n\n Error en la BBDD \n\n", exc_info=True)


#### CSV ####
try:
	with open("./archivos/usuarios.csv","a",newline="") as f:
		writer = csv.writer(f,delimiter=",")
		writer.writerow(users)
		
except Exception as e:
	logging.error("\n\n Error en CSV  \n\n", exc_info=True)

#### EMAIL ####

try:
	sender="example@example.com"
	pass_mail="example_password"
	context=ssl.create_default_context()
	msg="""Subject: Bienvenido!

	HOLA {} BIENVENIDO A MI FORMULARIO""".format(name)

	with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as s:
		s.login(sender,pass_mail)
		s.sendmail(sender,email,msg)
	
except Exception as e:
	logging.error("\n\n Error en EMAIL \n\n", exc_info=True)

finally:
	print("Location: http://http://nombrealumnob1.2daw.local/cliente.html")
	print("")
