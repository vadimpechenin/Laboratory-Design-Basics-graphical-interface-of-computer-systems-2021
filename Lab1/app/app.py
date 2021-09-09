"""
Класс для прорисовки и выполнения обработки событий с виджетов
"""
from settings import settings
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.Qt import QFont
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = settings.NAME
        self.left = settings.LEFT
        self.top = settings.TOP
        self.width = settings.WIDTH
        self.height = settings.HEIGHT
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.labl = QLabel(self)
        self.labl.setText(settings.TEXTINIT)
        self.labl.move(settings.WIDTH/2-40,settings.HEIGHT/4)

        self.button = QPushButton('button', self)
        self.button.move(settings.WIDTH/2-40,settings.HEIGHT/2+20)
        self.button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.labl.setText(settings.TEXTEND)
        self.labl.adjustSize()
        self.labl.setFont(QFont("Times", 12, QFont.Bold))
        self.labl.move(settings.WIDTH / 2 - 80, settings.HEIGHT / 4)
