"""
Класс для прорисовки и выполнения обработки событий с виджетов
"""
from settings import settings
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.Qt import QFont
from PyQt5.QtCore import pyqtSlot, Qt

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
        self.labl.move(20, 40)
        self.labl.resize(settings.WIDTH-40, settings.HEIGHT-40)
        #Управляющие кнопки
        self.buttonLoad = QPushButton('button', self)
        self.buttonLoad.setText(settings.TEXTBUTTONLOAD)
        self.buttonLoad.setStyleSheet('QPushButton {background-color: ' + settings.BUTTONLOADBACKGROUNDCOLOR+ '; color: '+ settings.BUTTONLOADTEXTCOLOR + ';}')
        self.buttonLoad.move(20, 10)
        self.buttonLoad.clicked.connect(self.onClickLoad)

        self.buttonSave = QPushButton('button', self)
        self.buttonSave.setText(settings.TEXTBUTTONSAVE)
        self.buttonSave.setStyleSheet('QPushButton {background-color: ' + settings.BUTTONSAVEBACKGROUNDCOLOR+ '; color: '+ settings.BUTTONSAVETEXTCOLOR + ';}')
        self.buttonSave.move(180, 10)
        self.buttonSave.clicked.connect(self.onClickSave)
        #Окно
        #self.image = QImage()
        #self.image = QImage(settings.WIDTH - 40, settings.HEIGHT - 40)
        #self.image.move(20, 20)
        self.show()

    @pyqtSlot()
    def onClickLoad(self):
        #Загрузить изображение
        #Универсальная загрузка интересующего изображения через диалог
        fname = QFileDialog.getOpenFileName(self,"Открыть Файл",None,"Image (*.png *.jpg *jpeg)")[0]
        self.pixmap = QPixmap(fname)
        #self.pixmap = QPixmap(settings.PATHTOIMAGE)
        self.image = QImage(settings.PATHTOIMAGE)
        #self.pixmap.scaled(self.labl.size(), Qt.KeepAspectRatio)
        #Добавить изображение к label
        self.labl.setPixmap(self.pixmap.scaled(self.labl.size(), Qt.KeepAspectRatio))
        #self.pixmap.scaled(self.labl.size(), Qt.KeepAspectRatio)


    def preRead(self, *args, **kwargs):
        self.pixmap = QPixmap(settings.PATHTOIMAGE)
        #self.image.load(settings.PATHTOIMAGE)

        #self.image.size(settings.WIDTH - 40, settings.HEIGHT - 40)
        #self.image.move(20, 20)

        width = self.image.width()
        depth = self.image.height()

        largest = max(width, depth)
        width = width / largest * (settings.WIDTH - 40)
        depth = depth / largest * (settings.HEIGHT - 40)

        #self.image.setWidthAndDepth(width, depth)
        #self._ui.showConfigUI()
        #self._ui.waitForUIToClose()

    @pyqtSlot()
    def onClickSave(self):
       pass
