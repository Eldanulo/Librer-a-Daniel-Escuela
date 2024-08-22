from PySide6.QtWidgets import (
	QMainWindow,
	QVBoxLayout,
	QTableWidget,
	QPushButton,
	QWidget,
	QFrame,
	QLineEdit,
	QStackedLayout,
	QApplication,
	QLabel
)

class ventana_registros (QFrame):
	def __init__(self):
		super().__init__()

		self.layout_registros = QVBoxLayout()

		self.table_widget = QTableWidget()
		self.button_return = QPushButton("Regresar")

		self.layout_registros.addWidget(self.table_widget)
		self.layout_registros.addWidget(self.button_return)

		self.setLayout(self.layout_registros)

class ventana_muestras (QMainWindow):
	def __init__(self):
		super().__init__()
		self.layout_muestras = QStackedLayout()

		self.layout_registros = ventana_registros()

		self.layout_muestras.addWidget(self.layout_registros)

		self.setLayout(self.layout_muestras)

		self.widget = QWidget()
		self.widget.setLayout(self.layout_muestras)
		self.setCentralWidget(self.widget)

	def change_window_main_log(self):
		self.layout_muestras.setCurrentIndex(0)
	
if __name__ == "__main__":
	app = QApplication()
	window = ventana_registros()
	window.show()
	app.exec()