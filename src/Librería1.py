
import mysql.connector
from mysql.connector import errorcode
from PySide6.QtWidgets import *
from ventana_insertar_usuario import ventana_insertar_usuarios
from ventana_de_muestras import ventana_registros
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
		user = "ParaTodos",
		passwd = "DBcontraseña1234",
		host = "192.168.0.10",
		# host = "localhost",
		database = "Librería",
	)
	cursor = mydb.cursor()
	
	return mydb, cursor

def desconectar_db(mydb, cursor):
	cursor.close()
	mydb.close()

class ventana_sql(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Librería: Proyecto")
		
		self.layout_sql = QStackedLayout()

		self.layout_menu = ventana_de_menu()
		self.layout_muestras = ventana_registros()
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
		self.layout_insertar_usuario.layout_inserciones.button_regresar.clicked.connect(self.cambiar_ventana_menu)
		self.layout_muestras.button_return.clicked.connect(self.cambiar_ventana_menu)

		##############################################################################

		self.layout_insertar_usuario.layout_inserciones.button_limpiar.clicked.connect(self.limpiar_insertar_usuario)

		#############################################################################

		self.widget = QWidget()
		self.widget.setLayout(self.layout_sql)
		self.setCentralWidget(self.widget)

	def cambiar_ventana_menu (self):
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

	def insertar_usuario(self):
		añandir_insercion = '''
			INSERT INTO Usuario (nom_usuario, apell_usuario, prov_usuario, pob_usuario, tel_usuario, nac_usuario)
			VALUES (%s, %s, %s, %s, %s, %s)
		'''

		nombre = self.layout_insertar_usuario.layout_inserciones.line_edit_nombre.text()
		apellido =self.layout_insertar_usuario.layout_inserciones.line_edit_apellido.text()
		provincia = self.layout_insertar_usuario.layout_inserciones.line_edit_provincia.text()
		distrito = self.layout_insertar_usuario.layout_inserciones.line_edit_distrito.text()
		nacimiento = self.layout_insertar_usuario.layout_inserciones.line_edit_telefono.text()
		fecha = self.layout_insertar_usuario.layout_inserciones.date_nacimiento.textFromDateTime()

		try:
			conectar_db()



			desconectar_db()
		except mysql.connector.Error as e:
			if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				error_message = "Usuario o contraseña incorrecto para la base de datos."
			elif e.errno == errorcode.ER_BAD_DB_ERROR:
				error_message = "Base de datos inexitente."
			else:
				error_message = f"Error al conectarse a la base de datos: {e}"
			self.layout_error_db.label_error_mysql.setText(error_message)

app = QApplication()
window = ventana_sql()
window.show()
app.exec()
