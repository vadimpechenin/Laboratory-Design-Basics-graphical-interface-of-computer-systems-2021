from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt, QPoint, QRect

import numpy as np
from settings import settings

class TestRect(QLabel):
    def __init__(self):
        super().__init__()
        self.begin = QPoint()
        self.end = QPoint()
        self.rectangles = []

        self.Angle1 = np.zeros(2)
        self.Angle2 = np.zeros(2)

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter(self)
        qp.setPen(QPen(Qt.black, 6, Qt.SolidLine))

        for rectangle in self.rectangles:
            qp.drawRect(rectangle)

        if not self.begin.isNull() and not self.end.isNull():
            qp.drawRect(QRect(self.begin, self.end).normalized())

    def mousePressEvent(self, event):
        self.begin = self.end = event.pos()
        self.Angle1[0], self.Angle1[1] = self.begin.x(), self.begin.y()
        self.update()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        r = QRect(self.begin, self.end).normalized()
        self.rectangles.append(r)
        self.begin = self.end = QPoint()
        self.Angle2[0], self.Angle2[1] = self.end.x(), self.end.y()
        settings.points_of_center.append([(self.Angle1[0] + self.Angle2[0]) / 2, (self.Angle1[1] + self.Angle2[1]) / 2])
        self.update()
        super().mouseReleaseEvent(event)
