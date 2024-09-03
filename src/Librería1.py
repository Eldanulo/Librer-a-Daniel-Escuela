import mysql.connector
from mysql.connector import errorcode
from PySide6 import QtCore
from PySide6.QtWidgets import *
from ventana_insertar_usuario import ventana_insertar_usuarios
from ventana_de_muestras import ventana_muestras
from ventana_menu import ventana_de_menu

columna_de_usuario = [
	"ID usuario",
	"Nombre",
	"Apellido",
	"Provincia",
	"Distrito",
	"Telefono",
	"Fecha de nacimiento",
]

def conectar_db():
	mydb = mysql.connector.connect (
		user="root",
		passwd="BDcontraseña1407",
		host="localhost",
		database="Librería",
		ssl_disabled=True
	)
	cursor = mydb.cursor()
	
	return mydb, cursor

def desconectar_db(mydb, cursor):
	cursor.close()
	mydb.close()

def error_bd(e):
	if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		error_message = "Usuario o contraseña incorrecto para la base de datos."
	elif e.errno == errorcode.ER_BAD_DB_ERROR:
		error_message = "Base de datos inexistente."
	else:
		error_message = f"Error al conectarse a la base de datos: {e}"
	
	return error_message

class ventana_sql(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Librería: Proyecto")
		
		self.layout_sql = QStackedLayout()

		self.layout_menu = ventana_de_menu()
		self.layout_muestras = ventana_muestras()
		self.layout_insertar_usuario = ventana_insertar_usuarios()

		lista_de_widget = [
			self.layout_menu,
			self.layout_muestras,
			self.layout_insertar_usuario
		]

		for widgets in lista_de_widget:
			self.layout_sql.addWidget(widgets)

		self.layout_menu.button_mostrar_usuarios.clicked.connect(self.cambiar_ventana_mostrar_usuario)
		self.layout_menu.button_insertar_usuarios.clicked.connect(self.cambiar_ventana_insertar_usuario)
		self.layout_menu.boton_salir.clicked.connect(self.close)
		self.layout_insertar_usuario.layout_inserciones.button_regresar.clicked.connect(self.cambiar_ventana_menu)
		self.layout_muestras.layout_registros.button_return.clicked.connect(self.cambiar_ventana_menu)

		##############################################################################

		self.layout_insertar_usuario.layout_inserciones.button_limpiar.clicked.connect(self.limpiar_insertar_usuario)
		self.layout_insertar_usuario.layout_inserciones.button_insertar.clicked.connect(self.insertar_usuario)

		#############################################################################
		
		self.layout_menu.button_mostrar_usuarios.clicked.connect(self.mostrar_usuarios)

		#############################################################################

		self.widget = QWidget()
		self.widget.setLayout(self.layout_sql)
		self.setCentralWidget(self.widget)
	
	#######################################################################################

	def cambiar_ventana_menu(self):
		self.layout_sql.setCurrentIndex(0)

	def cambiar_ventana_mostrar_usuario(self):
		self.layout_sql.setCurrentIndex(1)

	def cambiar_ventana_insertar_usuario(self):
		self.layout_sql.setCurrentIndex(2)        
		
	#################################################################
	
	def limpiar_insertar_usuario(self):
		self.layout_insertar_usuario.layout_inserciones.line_edit_nombre.setText('')
		self.layout_insertar_usuario.layout_inserciones.line_edit_apellido.setText('')
		self.layout_insertar_usuario.layout_inserciones.line_edit_provincia.setText('')
		self.layout_insertar_usuario.layout_inserciones.line_edit_distrito.setText('')
		self.layout_insertar_usuario.layout_inserciones.line_edit_telefono.setText('')
		self.layout_insertar_usuario.layout_inserciones.label_insertado.setHidden(True)

	def insertar_usuario(self):
		añadir_insercion = '''
			INSERT INTO Usuario (nom_usuario, apell_usuario, prov_usuario, pob_usuario, tel_usuario, nac_usuario)
			VALUES (%s, %s, %s, %s, %s, STR_TO_DATE(%s, '%d-%m-%Y'))
		'''

		nombre = self.layout_insertar_usuario.layout_inserciones.line_edit_nombre.text()
		apellido = self.layout_insertar_usuario.layout_inserciones.line_edit_apellido.text()
		provincia = self.layout_insertar_usuario.layout_inserciones.line_edit_provincia.text()
		distrito = self.layout_insertar_usuario.layout_inserciones.line_edit_distrito.text()
		telefono = self.layout_insertar_usuario.layout_inserciones.line_edit_telefono.text()

		# Obtener la fecha en el formato adecuado desde QDateEdit
		fecha_qdate = self.layout_insertar_usuario.layout_inserciones.date_nacimiento.date()
		fecha = fecha_qdate.toString("dd-MM-yyyy")  # Formato dd-MM-yyyy

		elementos = (
			nombre,
			apellido,
			provincia,
			distrito,
			telefono,
			fecha
		)

		try:
			mydb, cursor = conectar_db()

			cursor.execute(añadir_insercion, elementos)
			mydb.commit()

			desconectar_db(mydb, cursor)
		except mysql.connector.Error as e:
			error_message = error_bd(e)
			print(error_message)
			self.layout_insertar_usuario.layout_inserciones.label_insertado.setText(error_message)

		self.layout_insertar_usuario.layout_inserciones.label_insertado.setText("Usuario Insertado")
		self.layout_insertar_usuario.layout_inserciones.label_insertado.setHidden(False)
	
	############################################################################################################

	def mostrar_usuarios(self):
		self.layout_muestras.layout_registros.table_widget.setRowCount(0)

		try:
			mydb, cursor = conectar_db()

			cursor.execute("SELECT * FROM usuario;")
			usuarios = cursor.fetchall()

			cursor.execute('''
				SELECT CAST(count(COLUMN_NAME) AS char)
				FROM INFORMATION_SCHEMA.COLUMNS
				WHERE table_name = 'usuario' AND
				table_schema = 'librería'; 
			''')
			cantidad_columnas = cursor.fetchall()
			tamaño_columna = int(cantidad_columnas[0][0])

			self.layout_muestras.layout_registros.table_widget.setColumnCount(tamaño_columna)

			desconectar_db(mydb, cursor)
		except mysql.connector.Error as e:
			error_message = error_bd(e)
			print(error_message)

		for numero_fila, fila_con_datos in enumerate(usuarios):
			self.layout_muestras.layout_registros.table_widget.insertRow(numero_fila)
			for numero_columna, data in enumerate(fila_con_datos):
				item = QTableWidgetItem(str(data))
				item.setFlags(QtCore.Qt.ItemIsEnabled)
				self.layout_muestras.layout_registros.table_widget.setItem(numero_fila, numero_columna, item)

		self.layout_muestras.layout_registros.table_widget.setHorizontalHeaderLabels(columna_de_usuario)

app = QApplication()
window = ventana_sql()
window.show()
app.exec()
