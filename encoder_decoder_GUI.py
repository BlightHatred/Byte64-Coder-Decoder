#Importing necessary built-in modules

import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, \
    QApplication, QLabel, QPlainTextEdit, QPushButton
from PyQt6.QtCore import Qt

#Importing code/decode functions from custom module
from encoder_decoder import encoder, decoder

#This is a Python intermediate exercise, byte64 GUI coder/decoder

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Coder-Decoder')
        self.setGeometry(100, 100, 400, 400)
                       
        self.input = QPlainTextEdit(self)
        self.input.setGeometry(25, 30, 350, 100)
        
        self.output = QPlainTextEdit(self)
        self.output.setGeometry(25, 230, 350, 100)
        self.output.setReadOnly(True)

        self.button = QPushButton('Encode' , self)
        self.button.setGeometry(25, 170, 150, 20)
        self.button.clicked.connect(self.encode)
    
        self.button = QPushButton('Decode' , self)
        self.button.setGeometry(225, 170, 150, 20)
        self.button.clicked.connect(self.decode)

    def encode(self):

        text = str(self.input.toPlainText())
        self.output.setPlainText(str(encoder(text)))
        self.input.clear()

    def decode(self):    
        text = self.input.toPlainText()
        self.output.setPlainText(str(decoder(text)))
        self.input.clear()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
    






    