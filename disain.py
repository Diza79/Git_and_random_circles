from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from random import randint
import sys


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 600, 650)
        self.setWindowTitle("Рандомные окружности")

        self.button = QPushButton('Нарисовать', self)
        self.button.move(10, 10)
        self.button.clicked.connect(self.circle)

        self.label = QLabel(self)
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)
        self.label.move(0, 50)

    def circle(self):
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        r = randint(0, 255)
        b = randint(0, 255)
        g = randint(0, 255)
        pen.setColor(QColor(r, b, g))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
