
import sys
import os
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence,QFont,QPixmap,QMovie

from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5.QtWidgets import*


import qrc_resources

from Lexer import BasicLexer
from Parser import BasicParser
from BasicExecute import BasicExecute

sys.path.append("BasicExecute")
import BasicExecute as ResultadoF
import Parser as Error

from PyQt5.QtCore import pyqtSlot
dirPath = os.chdir(os.getcwd())

class Acercade(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Aserca de")
        self.label = QLabel(self) 
        self.pixmap = QPixmap('Logo.jpg').scaled(800, 600, Qt.KeepAspectRatio, Qt.FastTransformation) 
        self.label.setPixmap(self.pixmap) 
        self.label.resize(self.pixmap.width(), 
                          self.pixmap.height()) 
        self.label.move(50, 20)

        self.titulo= QLabel(self)
        self.titulo.setText("\tLenguaje Atón")
        self.titulo.setFont(QFont('Arial', 30))
        self.titulo.move(100, 200)

        self.subtitulo= QLabel(self)
        self.subtitulo.setText("Proyecto de:")
        self.subtitulo.setFont(QFont('Arial', 15))
        self.subtitulo.move(100, 300)

        self.subtitulo2= QLabel(self)
        self.subtitulo2.setText("\tParadigmas de programción")
        self.subtitulo2.setFont(QFont('Arial', 15))
        self.subtitulo2.move(100, 350)

        self.subtitulo3= QLabel(self)
        self.subtitulo3.setText("Elaborado por:")
        self.subtitulo3.setFont(QFont('Arial', 15))
        self.subtitulo3.move(100, 400)

        self.subtitulo4= QLabel(self)
        self.subtitulo4.setText("\tJoshua Granados Loria")
        self.subtitulo4.setFont(QFont('Arial', 15))
        self.subtitulo4.move(100, 450)

        self.subtitulo5= QLabel(self)
        self.subtitulo5.setText("\tKevin Mora Valverde")
        self.subtitulo5.setFont(QFont('Arial', 15))
        self.subtitulo5.move(100, 500)

        self.subtitulo6= QLabel(self)
        self.subtitulo6.setText("Profesor:")
        self.subtitulo6.setFont(QFont('Arial', 15))
        self.subtitulo6.move(100, 600)

        self.subtitulo6= QLabel(self)
        self.subtitulo6.setText("\tJosías Chavez Murillo")
        self.subtitulo6.setFont(QFont('Arial', 15))
        self.subtitulo6.move(100, 650)

        self.Anno= QLabel(self)
        self.Anno.setText("\t         2022")
        self.Anno.setFont(QFont('Arial', 30))
        self.Anno.move(100, 710)

        self.resize(900,800)

class Ayuda2(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.title = 'Ayuda'
        self.setWindowTitle(self.title)
        self.titulo= QLabel(self)
        self.titulo.setText("Manual de ayuda")
        self.titulo.setFont(QFont('Arial', 30))
        self.titulo.move(250, 20)
        self.subtitulo= QLabel(self)
        self.subtitulo.setText("En este manual se brindara información relevante a cómo utilizar la herramienta\n(guardar, cargar, abrir, copilar y ejecutar un archivo), además de la sintaxis\ndel código, sus palabras reservadas y sus estructuras.")
        self.subtitulo.setFont(QFont('Arial', 12))
        self.subtitulo.move(100, 100)
        self.resize(900,800)
        self.table_widget = MyTableWidget(self)
        self.table_widget.resize(900,580)
        self.table_widget.move(0, 200)
    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout2 = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(900,800)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Manual de uso")
        self.tabs.addTab(self.tab2,"Sintaxis")
        
        # Create first tab-----------------------------------------------------------------------------------------------------

        scroll= QtWidgets.QScrollArea()
        scroll.resize(900,800)
        self.tab1.layout = QVBoxLayout(self)

        self.subtitulo= QLabel(self)
        self.subtitulo.setText("\t\t\tManual de uso\n")
        self.subtitulo.setFont(QFont('Arial', 20))
        self.subtitulo.move(100, 10)
        #Abrir
        self.subtitulo1= QLabel(self)
        self.subtitulo1.setText("Abrir un archivo.")
        self.subtitulo1.setFont(QFont('Arial', 15))

        self.subtitulo2= QLabel(self)
        self.subtitulo2.setText("      Para abrir un archivo (proyecto) se puede hacer de tres formas.")
        self.subtitulo2.setFont(QFont('Arial', 12))

        self.subtitulo3= QLabel(self)
        self.subtitulo3.setText("\t1- Presionando la combinación de teclas 'Ctrl+o'.")
        self.subtitulo3.setFont(QFont('Arial', 12))

        self.subtitulo4= QLabel(self)
        self.subtitulo4.setText("\t2- Presionando el icono de Abrir (Carpeta) de la ventana principal.")
        self.subtitulo4.setFont(QFont('Arial', 12))

        self.subtitulo5= QLabel(self)
        self.subtitulo5.setText("\t3- Buscar la opción de guardar en el menú (Archivo->Abrir).")
        self.subtitulo5.setFont(QFont('Arial', 12))

        #Guardar
        self.subtitulo6= QLabel(self)
        self.subtitulo6.setText("Guardar un archivo.")
        self.subtitulo6.setFont(QFont('Arial', 15))

        self.subtitulo7= QLabel(self)
        self.subtitulo7.setText("      Para esta acción al igual que la anterior se puede hacer de varias formas. ")
        self.subtitulo7.setFont(QFont('Arial', 12))

        self.subtitulo8= QLabel(self)
        self.subtitulo8.setText("\t1- Presionando la combinación de teclas 'Ctrl+s'.")
        self.subtitulo8.setFont(QFont('Arial', 12))

        self.subtitulo9= QLabel(self)
        self.subtitulo9.setText("\t2- Presionando el icono de guardar de la ventana principal.")
        self.subtitulo9.setFont(QFont('Arial', 12))

        self.subtitulo10= QLabel(self)
        self.subtitulo10.setText("\t3- Buscar la opción de guardar en el menú (Archivo->Guardar).")
        self.subtitulo10.setFont(QFont('Arial', 12))


        #Crear
        self.subtitulo11= QLabel(self)
        self.subtitulo11.setText("Crear(Nuevo) un archivo.")
        self.subtitulo11.setFont(QFont('Arial', 15))

        self.subtitulo12= QLabel(self)
        self.subtitulo12.setText("      Esta acción se puede hacer de varias formas.")
        self.subtitulo12.setFont(QFont('Arial', 12))

        self.subtitulo13= QLabel(self)
        self.subtitulo13.setText("\t1- Presionando la combinación de teclas 'Ctrl+n'.")
        self.subtitulo13.setFont(QFont('Arial', 12))

        self.subtitulo14= QLabel(self)
        self.subtitulo14.setText("\t2- Presionando el icono de Nuevo (Mas) de la ventana principal.")
        self.subtitulo14.setFont(QFont('Arial', 12))

        self.subtitulo15= QLabel(self)
        self.subtitulo15.setText("\t3- Buscar la opción de nuevo en el menú (Archivo->Nuevo).")
        self.subtitulo15.setFont(QFont('Arial', 12))

        #Ejecutar
        self.subtitulo16= QLabel(self)
        self.subtitulo16.setText("Ejecutar un archivo.")
        self.subtitulo16.setFont(QFont('Arial', 15))

        self.subtitulo17= QLabel(self)
        self.subtitulo17.setText("      Esta acción se puede hacer pulsando el botón de ejecutar, como se muestra\nen la imagen.")
        self.subtitulo17.setFont(QFont('Arial', 12))


        content_widget = QtWidgets.QWidget()
        scroll.setWidget(content_widget)
        scroll.setWidgetResizable(True)
        lay = QtWidgets.QVBoxLayout(content_widget)

        #Gif1
        self.label = QLabel(self) 
        self.movi = QMovie("IMAGENES/ezgif.com-gif-maker2.gif")
        self.label.resize(150,150)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMovie(self.movi)
        self.movi.start()

        self.label2 = QLabel(self) 
        self.movi2 = QMovie("IMAGENES/ezgif.com-gif-maker1.gif")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setMovie(self.movi2)
        self.movi2.start()

        self.label3 = QLabel(self) 
        self.movi3 = QMovie("IMAGENES/ezgif.com-gif-maker3.gif")
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setMovie(self.movi3)
        self.movi3.start()

        self.label17 = QLabel(self) 
        self.pixmap17 = QPixmap('IMAGENES/ejecucion.png')
        self.label17.setAlignment(Qt.AlignCenter) 
        self.label17.setPixmap(self.pixmap17) 
        self.label17.resize(self.pixmap17.width(), 
                          self.pixmap17.height())

        #Abrir
        lay.addWidget(self.subtitulo)
        lay.addWidget(self.subtitulo1)
        lay.addWidget(self.subtitulo2)
        lay.addWidget(self.subtitulo3)
        lay.addWidget(self.subtitulo4)
        lay.addWidget(self.subtitulo5)
        #Imagen
        lay.addWidget(self.label)
        #Guardar
        lay.addWidget(self.subtitulo6)
        lay.addWidget(self.subtitulo7)
        lay.addWidget(self.subtitulo8)
        lay.addWidget(self.subtitulo9)
        lay.addWidget(self.subtitulo10)
        lay.addWidget(self.label2)
        #Nuevo
        lay.addWidget(self.subtitulo11)
        lay.addWidget(self.subtitulo12)
        lay.addWidget(self.subtitulo13)
        lay.addWidget(self.subtitulo14)
        lay.addWidget(self.subtitulo15)
        lay.addWidget(self.label3)
        #Nuevo
        lay.addWidget(self.subtitulo16)
        lay.addWidget(self.subtitulo17)
        lay.addWidget(self.label17)
        lay.addStretch()

        scroll.setFixedHeight(480)

        self.tab1.layout.addWidget(scroll)

        self.tab1.setLayout(self.tab1.layout)
    
        #Create tab 2---------------------------------------------------------------------------------------------------------------
        scroll2= QtWidgets.QScrollArea()
        scroll2.resize(900,800)
        self.tab2.layout = QVBoxLayout(self)

        self.subsin= QLabel(self)
        self.subsin.setText("\t\t\tSintaxis\n")
        self.subsin.setFont(QFont('Arial', 20))

        #Reservadas
        self.subsin1= QLabel(self)
        self.subsin1.setText("Palabras reservadas ")
        self.subsin1.setFont(QFont('Arial', 15))

        #Control
        self.subsin2= QLabel(self)
        self.subsin2.setText("Estructuras de control")
        self.subsin2.setFont(QFont('Arial', 15))

        self.subsin3= QLabel(self)
        self.subsin3.setText("      En este leguaje existen dos estructuras principales.")
        self.subsin3.setFont(QFont('Arial', 12))

        self.subsin4= QLabel(self)
        self.subsin4.setText("\t<> Ciclos:")
        self.subsin4.setFont(QFont('Arial', 12))

        self.subsin5= QLabel(self)
        self.subsin5.setText("\t\t->PARA (For):")
        self.subsin5.setFont(QFont('Arial', 11))

        self.subsin6= QLabel(self)
        self.subsin6.setText("\t\t->MIENTRAS (while):")
        self.subsin6.setFont(QFont('Arial', 11))

        self.subsin7= QLabel(self)
        self.subsin7.setText("\t<> Condicionales:")
        self.subsin7.setFont(QFont('Arial', 12))

        self.subsin8= QLabel(self)
        self.subsin8.setText("\t\t->SI (if):")
        self.subsin8.setFont(QFont('Arial', 11))

        self.subsin9= QLabel(self)
        self.subsin9.setText("\t\t->CASOS (switch):")
        self.subsin9.setFont(QFont('Arial', 11))

        #Funciones
        self.subsin10= QLabel(self)
        self.subsin10.setText("Funciones.")
        self.subsin10.setFont(QFont('Arial', 15))

        self.subsin11= QLabel(self)
        self.subsin11.setText("      Para la declaración de funciones se usa la palabra reservada HAGA.")
        self.subsin11.setFont(QFont('Arial', 12))

        self.subsin12= QLabel(self)
        self.subsin12.setText("\tEstas se pueden declarar de dos formas:")
        self.subsin12.setFont(QFont('Arial', 12))

        self.subsin13= QLabel(self)
        self.subsin13.setText("\t\t# Con parámetros:")
        self.subsin13.setFont(QFont('Arial', 12))

        self.subsin14= QLabel(self)
        self.subsin14.setText("\t\t# Sin parámetros:")
        self.subsin14.setFont(QFont('Arial', 12))


        #Variables
        self.subsin15= QLabel(self)
        self.subsin15.setText("Variables")
        self.subsin15.setFont(QFont('Arial', 15))

        self.subsin16= QLabel(self)
        self.subsin16.setText("      Para la declaración de variables se hace con el nombre y el valor a asignar")
        self.subsin16.setFont(QFont('Arial', 12))

        self.subsin17= QLabel(self)
        self.subsin17.setText("\t# Variables simples:")
        self.subsin17.setFont(QFont('Arial', 12))

        self.subsin18= QLabel(self)
        self.subsin18.setText("\t\t- Entero:")
        self.subsin18.setFont(QFont('Arial', 12))

        self.subsin19= QLabel(self)
        self.subsin19.setText("\t\t- Texto:")
        self.subsin19.setFont(QFont('Arial', 12))

        self.subsin20= QLabel(self)
        self.subsin20.setText("\t\t- Booleano:")
        self.subsin20.setFont(QFont('Arial', 12))

        self.subsin21= QLabel(self)
        self.subsin21.setText("\t\t- Letra:")
        self.subsin21.setFont(QFont('Arial', 12))

        self.subsin22= QLabel(self)
        self.subsin22.setText("\t\t- Flotante:")
        self.subsin22.setFont(QFont('Arial', 12))


        self.subsin23= QLabel(self)
        self.subsin23.setText("\t# Variables compuestas")
        self.subsin23.setFont(QFont('Arial', 12))

        self.subsin24= QLabel(self)
        self.subsin24.setText("\t\t@ Arreglos:")
        self.subsin24.setFont(QFont('Arial', 12))

        self.subsin25= QLabel(self)
        self.subsin25.setText("\t\t\t+ Numerales:")
        self.subsin25.setFont(QFont('Arial', 12))

        self.subsin26= QLabel(self)
        self.subsin26.setText("\t\t\t+ String:")
        self.subsin26.setFont(QFont('Arial', 12))

        self.subsin29= QLabel(self)
        self.subsin29.setText("\t\t\t+ Llenar con ciclo PARA:")
        self.subsin29.setFont(QFont('Arial', 12))

        self.subsin27= QLabel(self)
        self.subsin27.setText("\t\t@ Matrices:")
        self.subsin27.setFont(QFont('Arial', 12))

        #Operadores
        self.subsin28= QLabel(self)
        self.subsin28.setText("Operadores")
        self.subsin28.setFont(QFont('Arial', 12))

        content_widget2 = QtWidgets.QWidget()
        scroll2.setWidget(content_widget2)
        scroll2.setWidgetResizable(True)
        lay2 = QtWidgets.QVBoxLayout(content_widget2)

        #Imagenes
        self.label = QLabel(self) 
        self.pixmap = QPixmap('Reservadas.png') 
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(self.pixmap) 
        self.label.resize(self.pixmap.width(), 
                          self.pixmap.height()) 
        
        self.label2 = QLabel(self) 
        self.pixmap2 = QPixmap('Operadores.png')
        self.label2.setPixmap(self.pixmap2) 
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.resize(self.pixmap2.width(), 
                          self.pixmap2.height()) 
        
        self.label3 = QLabel(self) 
        self.pixmap3 = QPixmap('IMAGENES/INT.png')
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setPixmap(self.pixmap3) 
        self.label3.resize(self.pixmap3.width(), 
                          self.pixmap3.height()) 

        self.label4= QLabel(self) 
        self.pixmap4 = QPixmap('IMAGENES/STRING.png') 
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setPixmap(self.pixmap4) 
        self.label4.resize(self.pixmap4.width(), 
                          self.pixmap4.height())

        self.label5 = QLabel(self) 
        self.pixmap5 = QPixmap('IMAGENES/BOOLEANA.png') 
        self.label5.setAlignment(Qt.AlignCenter)
        self.label5.setPixmap(self.pixmap5) 
        self.label5.resize(self.pixmap5.width(), 
                          self.pixmap5.height())
        
        self.label6 = QLabel(self) 
        self.pixmap6 = QPixmap('IMAGENES/VARCHAR.png')
        self.label6.setAlignment(Qt.AlignCenter) 
        self.label6.setPixmap(self.pixmap6) 
        self.label6.resize(self.pixmap6.width(), 
                          self.pixmap6.height())

        self.label7 = QLabel(self) 
        self.pixmap7 = QPixmap('IMAGENES/FLOAT.png')
        self.label7.setAlignment(Qt.AlignCenter) 
        self.label7.setPixmap(self.pixmap7) 
        self.label7.resize(self.pixmap7.width(), 
                          self.pixmap7.height())

        self.label8 = QLabel(self) 
        self.pixmap8 = QPixmap('IMAGENES/ARREGLO NUMERO.png') 
        self.label8.setAlignment(Qt.AlignCenter)
        self.label8.setPixmap(self.pixmap8) 
        self.label8.resize(self.pixmap8.width(), 
                          self.pixmap8.height())

        self.label9 = QLabel(self) 
        self.pixmap9 = QPixmap('IMAGENES/ARREGLO STRING.png') 
        self.label9.setAlignment(Qt.AlignCenter)
        self.label9.setPixmap(self.pixmap9) 
        self.label9.resize(self.pixmap9.width(), 
                          self.pixmap9.height())

        self.label20 = QLabel(self) 
        self.pixmap20 = QPixmap('IMAGENES/ARREGLO DESDE FOR.png')
        self.label20.setAlignment(Qt.AlignCenter) 
        self.label20.setPixmap(self.pixmap20) 
        self.label20.resize(self.pixmap20.width(), 
                          self.pixmap20.height())
        
        self.label10 = QLabel(self) 
        self.pixmap10 = QPixmap('IMAGENES/FOR.png')
        self.label10.setAlignment(Qt.AlignCenter) 
        self.label10.setPixmap(self.pixmap10) 
        self.label10.resize(self.pixmap10.width(), 
                          self.pixmap10.height())
        
        self.label11 = QLabel(self) 
        self.pixmap11 = QPixmap('IMAGENES/WHILE.png')
        self.label11.setAlignment(Qt.AlignCenter) 
        self.label11.setPixmap(self.pixmap11) 
        self.label11.resize(self.pixmap11.width(), 
                          self.pixmap11.height())
        
        self.label12 = QLabel(self) 
        self.pixmap12 = QPixmap('IMAGENES/IF.png')
        self.label12.setAlignment(Qt.AlignCenter) 
        self.label12.setPixmap(self.pixmap12) 
        self.label12.resize(self.pixmap12.width(), 
                          self.pixmap12.height())
        
        self.label13 = QLabel(self) 
        self.pixmap13 = QPixmap('IMAGENES/SWICTH.png') 
        self.label13.setAlignment(Qt.AlignCenter)
        self.label13.setPixmap(self.pixmap13) 
        self.label13.resize(self.pixmap13.width(), 
                          self.pixmap13.height())

        self.label14 = QLabel(self) 
        self.pixmap14 = QPixmap('IMAGENES/Funcion con parametros.png') 
        self.label14.setAlignment(Qt.AlignCenter)
        self.label14.setPixmap(self.pixmap14) 
        self.label14.resize(self.pixmap14.width(), 
                          self.pixmap14.height())

        self.label15 = QLabel(self) 
        self.pixmap15 = QPixmap('IMAGENES/FUNCION SIN PARAMETROS.png')
        self.label15.setAlignment(Qt.AlignCenter) 
        self.label15.setPixmap(self.pixmap15) 
        self.label15.resize(self.pixmap15.width(), 
                          self.pixmap15.height())

        self.label16 = QLabel(self) 
        self.pixmap16 = QPixmap('IMAGENES/matriz.png')
        self.label16.setAlignment(Qt.AlignCenter) 
        self.label16.setPixmap(self.pixmap16) 
        self.label16.resize(self.pixmap16.width(), 
                          self.pixmap16.height())
        
        

        #Reservadas
        lay2.addWidget(self.subsin)
        lay2.addWidget(self.subsin1)
        lay2.addWidget(self.label)

        #Variables
        lay2.addWidget(self.subsin15)
        lay2.addWidget(self.subsin16)
        lay2.addWidget(self.subsin17)
        lay2.addWidget(self.subsin18)
        lay2.addWidget(self.label3)
        lay2.addWidget(self.subsin19)
        lay2.addWidget(self.label4)
        lay2.addWidget(self.subsin20)
        lay2.addWidget(self.label5)
        lay2.addWidget(self.subsin21)
        lay2.addWidget(self.label6)
        lay2.addWidget(self.subsin22)
        lay2.addWidget(self.label7)
        lay2.addWidget(self.subsin23)
        lay2.addWidget(self.subsin24)
        lay2.addWidget(self.subsin25)
        lay2.addWidget(self.label8)
        lay2.addWidget(self.subsin26)
        lay2.addWidget(self.label9)
        lay2.addWidget(self.subsin29)
        lay2.addWidget(self.label20)
        lay2.addWidget(self.subsin27)
        lay2.addWidget(self.label16)

        #Operadores
        lay2.addWidget(self.subsin28)
        lay2.addWidget(self.label2)

        #Control
        lay2.addWidget(self.subsin2)
        lay2.addWidget(self.subsin3)
        lay2.addWidget(self.subsin4)
        lay2.addWidget(self.subsin5)
        lay2.addWidget(self.label10)
        lay2.addWidget(self.subsin6)
        lay2.addWidget(self.label11)
        lay2.addWidget(self.subsin7)
        lay2.addWidget(self.subsin8)
        lay2.addWidget(self.label12)
        lay2.addWidget(self.subsin9)
        lay2.addWidget(self.label13)
        #Funciones
        lay2.addWidget(self.subsin10)
        lay2.addWidget(self.subsin11)
        lay2.addWidget(self.subsin12)
        lay2.addWidget(self.subsin13)
        lay2.addWidget(self.label14)
        lay2.addWidget(self.subsin14)
        lay2.addWidget(self.label15)

        
        #lay2.addWidget(self.subtitulo1)

        lay2.addStretch()

        scroll2.setFixedHeight(480)

        self.tab2.layout.addWidget(scroll2)

        self.tab2.setLayout(self.tab2.layout)
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Atón lenguaje")
        self.resize(1000, 800)
        self.widget = QtWidgets.QWidget()
        self.widget2 = QtWidgets.QWidget()
        self.layout3 = QVBoxLayout(self.widget)
        self.layout4 = QHBoxLayout(self.widget2)
        

        self.txtcmd = QTextEdit(self)
        #self.txtcmd.setText(ResultadoF.Resultado+"\n"+Error.ErrorT)
        self.txtcmd.setDisabled(True)
        self.txtcmd.setPlaceholderText(">")
        self.txtcmd.setStyleSheet("background-color : black")
        self.txtcmd.setGeometry(10, 10, 10, 10)

        self.titulo= QLabel(self)
        self.titulo.setText("Terminal")
        self.titulo.setFont(QFont('Arial', 10))
        self.titulo.move(100, 200)

        pybutton = QPushButton(self)
        pybutton.resize(5,3)
        pybutton.setStyleSheet("background-color :rgba(255,255,255,0)")
        pybutton.clicked.connect(self.clickMethod)
        pybutton.setIcon(QIcon('IMAGENES/limpieza-de-datos.png'))

        self.txtTextoEditado = QTextEdit(self)
        self.txtTextoEditado.setPlaceholderText("Escriba el codigo")
        self.layout3.addWidget(self.txtTextoEditado)
        self.layout3.addWidget(self.widget2)
        self.layout4.addWidget(self.titulo)
        self.layout4.addWidget(pybutton)
        self.layout3.addWidget(self.txtcmd)
        self.setCentralWidget(self.widget)
        
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        NombreA  = ""
        self._connectActions()
        self._createStatusBar()

    def clickMethod(self):
        self.txtcmd.clear()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # File menu
        fileMenu = QMenu("&Archivo", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        
        # Open Recent submenu
        fileMenu.addAction(self.saveAction)

        # Separator
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        # Edit menu
        # Help menu
        helpMenu = menuBar.addMenu("&Ayuda")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)
    
    def _createToolBars(self):
        # File toolbar
        fileToolBar = self.addToolBar("Archivo")
        fileToolBar.setMovable(False)
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        # Edit toolbar
        editToolBar = QToolBar("Editar", self)
        self.addToolBar(editToolBar)

        ejecutar = QAction(QIcon("Ejecutar.bmp"),"Ejecutar",self)
        editToolBar.addAction(ejecutar)
        ejecutar.triggered.connect(self.Ejecutar)

        copilar = QAction(QIcon("IMAGENES/compilador.png"),"Copilar",self)
        editToolBar.addAction(copilar)
        copilar.triggered.connect(self.Copilar)



    def _createStatusBar(self):

        self.statusBar().children().pop().findChildren
        self.statusbar = self.statusBar()
        #Temporary message
        self.statusbar.showMessage("Listos para programar", 3000)
        
		
    def Copilar(self):
        try:
            Error.ErrorT=""
            ResultadoF.Resultado=""
            lexer = BasicLexer()
            parser = BasicParser()
            env = {}
            with open (NombreA, "r") as archivo:
                try:
                    linea = archivo.readline()
                    contadorL = 1
                    while linea:
                        tree = parser.parse(lexer.tokenize(linea))
                        BasicExecute(tree,env)
                        linea = archivo.readline()
                        contadorL+=1
                except SyntaxError:
                    print("Entre al error ")
           
            if(Error.ErrorT==None):
                self.txtcmd.setText(self.txtcmd.toPlainText()+"\n"+"No presenta errores")
            else:
                self.txtcmd.setText(self.txtcmd.toPlainText()+"\n"+Error.ErrorT)
        except Exception:
            e=sys.exc_info()[1]
          
            self.txtcmd.setText(self.txtcmd.toPlainText()+"\n"+"Error "+e.args[0])

    def _createActions(self):
        # File actions
        self.newAction = QAction(self)
        self.newAction.setText("&Nuevo")
        self.newAction.setIcon(QIcon(":file-new.svg"))

        self.openAction = QAction(QIcon(":file-open.svg"), "&Abrir...", self)

        self.saveAction = QAction(QIcon(":file-save.svg"), "&Guardar", self)

        self.exitAction = QAction("&Salir", self)
        # String-based key sequences
        self.newAction.setShortcut("Ctrl+N")
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction.setShortcut("Ctrl+S")
        # Help tips
        newTip = "Crear un nuevo archivo"
        self.newAction.setStatusTip(newTip)
        self.newAction.setToolTip(newTip)
        self.newAction.setWhatsThis("Crear un archivo de texto nuevo y vacío")
        # Help actions
        self.helpContentAction = QAction("&Contenido de ayuda...", self)
        self.aboutAction = QAction("&Acerca de...", self)


    def contextMenuEvent(self, event):
        # Context menu
        menu = QMenu(self.txtTextoEditado)
        # Populating the menu with actions
        menu.addAction(self.newAction)
        menu.addAction(self.openAction)
        menu.addAction(self.saveAction)
        # Separator
        separator = QAction(self)
        separator.setSeparator(True)
        menu.addAction(separator)
        # Launching the menu
        menu.exec(event.globalPos())

    def _connectActions(self):
        # Connect File actions
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)
        
        # Connect Help actions
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)

    # Slots
    def newFile(self):
        # Logic for creating a new file goes here...
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Archivos Atón (*.aton)", options=options)
            if fileName:
                global NombreA
                NombreA = fileName
                with open (fileName, "w") as archivo: #Creamos el archivo
                    archivo.write("")
                    #f.close()
                QMessageBox.about(self, "Accion exitosa", "El archivo se creo exitosamente")
        except Exception:
            e=sys.exc_info()[1]
      
            self.txtcmd.setText(self.txtcmd.toPlainText()+"\n"+"Error, no se pudo crear el archivo "+e.args[0])

    def openFile(self):
        # Logic for opening an existing file goes here...
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Archivos Atón (*.aton)", options=options)
            if file:
             
                global NombreA
                NombreA = file
                with open(file, "r") as archivo:
                    contenido = archivo.read()
                self.txtTextoEditado.setText(contenido)
        except Exception:
            e=sys.exc_info()[1]
           
            self.txtcmd.setText(self.txtcmd.toPlainText()+"\n"+"Error, el archivo no se puede abir "+e.args[0])

    def saveFile(self):
        # Logic for saving a file goes here...
        try:
            with open (NombreA, "w") as archivo: #Creamos el archivo
                archivo.writelines(self.txtTextoEditado.toPlainText())
                #f.close()
            QMessageBox.about(self, "Accion exitosa", "El archivo se guardo exitosamente")
        except Exception:
            e=sys.exc_info()[1]
            self.txtcmd.setText(self.txtcmd.toPlainText()+"\n"+"Error, el archivo no se guardo exitosamente"+"\n"+e.args[0])
            self.newFile()
            self.saveFile()


    def Ejecutar(self):
        try:
            ResultadoF.Resultado=""
            Error.ErrorT=""
            lexer = BasicLexer()
            parser = BasicParser()
            env = {}
            self.saveFile()
            with open (NombreA, "r") as archivo:
                try:
                    linea = archivo.readline()
                    contadorL = 1
                    while linea:
                        tree = parser.parse(lexer.tokenize(linea))
                        BasicExecute(tree,env)
                        linea = archivo.readline()
                        contadorL+=1
                except SyntaxError:
                    print("Entre al error ")
        
            self.txtcmd.setText(self.txtcmd.toPlainText()+"\n"+ResultadoF.Resultado+"\n"+Error.ErrorT)
        except Exception:
            e=sys.exc_info()[1]
        
            self.txtcmd.setText(self.txtcmd.toPlainText()+"\n"+"Error "+e.args[0])

    def helpContent(self):
        # Logic for launching help goes here...
        win = Ayuda2()
        win.exec_()

    def about(self):
        # Logic for showing an about dialog content goes here...
        abo =Acercade()
        abo.exec_()

    

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec_())


