"""
Класс для прорисовки и выполнения обработки событий с виджетов
"""
from settings import settings
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen, QBrush, QIcon, QColor, QPainterPath
from PyQt5.Qt import QFont
from PyQt5.QtCore import pyqtSlot, Qt, QPoint, QRect

import numpy as np
import cv2
from app.drawRect import TestRect

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = settings.NAME
        self.left = settings.LEFT
        self.top = settings.TOP
        self.width = settings.WIDTH
        self.height = settings.HEIGHT
        self.main_layout = QVBoxLayout()
        self.central_widget = QWidget(self)
        self.current_image = None
        self.btn_layout = QHBoxLayout()
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Управляющие кнопки
        self.buttonLoad = QPushButton('button', self)
        self.buttonLoad.setText(settings.TEXTBUTTONLOAD)
        self.buttonLoad.setStyleSheet('QPushButton {background-color: ' + settings.BUTTONLOADBACKGROUNDCOLOR+ '; color: '+ settings.BUTTONLOADTEXTCOLOR + ';}')
        self.buttonLoad.move(40, 10)
        self.buttonLoad.setMinimumWidth(160)
        self.buttonLoad.clicked.connect(self.onClickLoad)
        self.btn_layout.addWidget(self.buttonLoad)

        self.buttonSave = QPushButton('button', self)
        self.buttonSave.setText(settings.TEXTBUTTONSAVE)
        self.buttonSave.setStyleSheet('QPushButton {background-color: ' + settings.BUTTONSAVEBACKGROUNDCOLOR+ '; color: '+ settings.BUTTONSAVETEXTCOLOR + ';}')
        self.buttonSave.move(220, 10)
        self.buttonSave.clicked.connect(self.onClickSave)
        self.btn_layout.addWidget(self.buttonSave)

        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        #Окно
        #self.image = QImage()
        #self.image = QImage(settings.WIDTH - 40, settings.HEIGHT - 40)
        #self.image.move(20, 20)
        self.show()

    #@pyqtSlot()
    def onClickLoad(self):
        #Загрузить изображение
        #Универсальная загрузка интересующего изображения через диалог
        fname = QFileDialog.getOpenFileName(self,"Открыть Файл",None,"Image (*.png *.jpg *jpeg)")[0]
        fname1 = fname.split('/')
        path = fname1[-2] + '/' + fname1[-1]
        image = TestRect()
        self.main_layout.addWidget(image)
        uploaded = cv2.imread(path)
        rgb_img = cv2.cvtColor(uploaded, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(rgb_img, (settings.WIDTH - 40, settings.HEIGHT - 40))
        height, width = settings.WIDTH - 40, settings.HEIGHT - 40
        self.current_image = QImage(resized, height, width, QImage.Format_RGB888)
        image.setPixmap(QPixmap(self.current_image))

    @pyqtSlot()
    def onClickSave(self):
        # Запись
        with open(settings.filename, 'w') as file_object:
            for item in settings.points_of_center:
                file_object.write(str(item) + "\n")
