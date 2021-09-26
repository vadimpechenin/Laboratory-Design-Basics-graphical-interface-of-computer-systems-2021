"""
Лабораторная работа 2 по курсу Основы проектирования
графического интерфейса компьютерных систем. Загрузка картинки, рисование прямоугольников, сохранение их центров
"""
import sys
from PyQt5.QtWidgets import QApplication

from app.app import App

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())