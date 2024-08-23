import mysql.connector
from mysql.connector import errorcode
from PySide6.QtWidgets import *

def conectar_db():
	mydb = mysql.connector.connect (
		user = "ParaTodos",
		passwd = "contraseña1234",
		host = "192.168.0.9",
		#host = "localhost",
		database = "Librería",
	)
	cursor = mydb.cursor()
	
	return mydb, cursor

def desconectar_db(mydb, cursor):
	cursor.close()
	mydb.close()

def mostrar_error (e):
	if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		mensaje_error = "Error: Usuario o Contrseña incorrecto"
	elif e.errno == errorcode.ER_BAD_DB_ERROR:
		mensaje_error = "Base de Datos no existe"
	else:
		mensaje_error = f"Error al conectarse a la DB: {e}"
	print(f"{mensaje_error}") 

def imprimir_resultados (r):
	for fila in r:
		print(fila)

def mostrar_libros():
	try:
		mydb, cursor = conectar_db()

		cursor.execute("select * from Libros")
		resultados = cursor.fetchall()

		imprimir_resultados(resultados)

		desconectar_db(mydb, cursor)
	except mysql.connector.Error as e:
		mostrar_error(e)
		

def mostrar_autores():
	try:
		mydb, cursor = conectar_db()

		cursor.execute("select * from Autores")
		resultados = cursor.fetchall()

		imprimir_resultados(resultados)

		desconectar_db(mydb, cursor)
	except mysql.connector.Error as e:
		mostrar_error(e)


def mostrar_prestamos():
	try:
		mydb, cursor = conectar_db()

		cursor.execute("select * from Prestamos")
		resultados = cursor.fetchall()

		imprimir_resultados(resultados)

		desconectar_db(mydb, cursor)
	except mysql.connector.Error as e:
		mostrar_error(e)


def mostrar_usuarios():
	try:
		mydb, cursor = conectar_db()

		cursor.execute("select * from Usuario")
		resultados = cursor.fetchall()

		imprimir_resultados(resultados)

		desconectar_db(mydb, cursor)
	except mysql.connector.Error as e:
		mostrar_error(e)

if __name__ == "__main__":
	while True:
		print("\nBienvenido ¿Qué desea hacer?")
		print("\n1. Mostrar Préstamos")
		print("2. Mostrar Usuarios")
		print("3. Mostrar Libros")
		print("4. Mostrar Autores")
		print("5. Insertar Préstamos")
		print("6. Insertar Usuarios")
		print("7. Insertar Libros")
		print("8. Insertar Autores")
		print("0. Salir")

		menu = int(input("\nIntrodusca una opción: "))
		print()

		match menu:
			case 1: mostrar_prestamos()
			case 2: mostrar_usuarios()
			case 3: mostrar_libros()
			case 4: mostrar_autores()
			case 5: pass
			case 6: pass
			case 7: pass
			case 8: pass
			case 0: break
			case _: print("Opción inválida. Ingrese una de las opciones presentadas.")