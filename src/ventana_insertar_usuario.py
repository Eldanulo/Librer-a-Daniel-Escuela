from PySide6.QtWidgets import *

class inserciones(QFrame):
	def __init__(self):
		super().__init__()
		
		self.layout_inserciones = QGridLayout()

		self.label_nombre = QLabel("Nombre")
		self.line_edit_nombre = QLineEdit()
		self.label_apellido = QLabel("Apellido")
		self.line_edit_apellido = QLineEdit()
		self.label_provincia = QLabel("Provincia")
		self.line_edit_provincia = QLineEdit()
		self.label_distrito = QLabel("Distrito")
		self.line_edit_distrito =QLineEdit()
		self.label_telefono = QLabel("Telefono")
		self.line_edit_telefono = QLineEdit()
		self.label_nacimiento = QLabel("Fecha de nacimiento")
		self.date_nacimiento = QDateEdit()
		self.label_insertado = QLabel("Usuario insertado")
		self.button_insertar = QPushButton("Insertar usuario")
		self.button_limpiar = QPushButton("Limpiar campos")
		self.button_regresar = QPushButton("Regresar")

		lista_de_widgets = [
			self.label_nombre,
			self.line_edit_nombre,
			self.label_apellido,
			self.line_edit_apellido,
			self.label_provincia,
			self.line_edit_provincia,
			self.label_distrito,
			self.line_edit_distrito,
			self.label_nacimiento,
			self.date_nacimiento,
			self.label_telefono,
			self.line_edit_telefono,
			self.label_insertado,
			self.button_insertar,
			self.button_limpiar,
			self.button_regresar
		]
		
		fila = 0
		columna = 0

		for widget in lista_de_widgets:
			if columna == 2:
				columna = 0
				fila += 1
			self.layout_inserciones.addWidget(widget, fila, columna)
			columna += 1

		self.label_insertado.setHidden(True)

		self.setLayout(self.layout_inserciones)

class ventana_insertar_usuarios(QMainWindow):
	def __init__(sefl):
		super().__init__() 

		sefl.layout_insertar_usuarios = QVBoxLayout()
		sefl.layout_inserciones = inserciones()
		sefl.layout_insertar_usuarios.addWidget(sefl.layout_inserciones)

		sefl.widget = QWidget()
		sefl.widget.setLayout(sefl.layout_insertar_usuarios)
		sefl.setCentralWidget(sefl.widget)
		
if __name__ == "__main__":
	app = QApplication()
	window = ventana_insertar_usuarios()
	window.show()
	app.exec()