from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

class ventana_de_menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout_menu = QVBoxLayout()

        self.label_titulo = QLabel("Librería")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.button_mostrar_prestamos = QPushButton("Mostrar prestamos")
        self.button_insertar_prestamos = QPushButton("Insertar prestamos")
        self.button_mostrar_usuarios = QPushButton("Mostrar usuarios")
        self.button_insertar_usuarios = QPushButton("Insertar usuarios")
        self.button_mostrar_libros = QPushButton("Mostrar libros")
        self.button_insertar_libros = QPushButton("Insertar libros")
        self.button_mostrar_autores = QPushButton("Mostrar autores")
        self.button_insertar_autores = QPushButton("Insertar autor")
        
        lista_de_widgets = [
            QLabel(),
            self.label_titulo,
            QLabel(),
            self.button_mostrar_prestamos,
            QLabel(),
            self.button_insertar_prestamos,
            QLabel(),
            self.button_mostrar_usuarios,
            QLabel(),
            self.button_insertar_usuarios,
            QLabel(),
            self.button_mostrar_libros,
            QLabel(),
            self.button_insertar_libros,
            QLabel(),
            self.button_mostrar_autores,
            QLabel(),
            self.button_insertar_autores,
            QLabel(),
        ]

        for widget in lista_de_widgets:
            self.layout_menu.addWidget(widget)

        self.widget = QWidget()
        self.widget.setLayout(self.layout_menu)
        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    app = QApplication()
    window = ventana_de_menu()
    window.show()
    app.exec()

          