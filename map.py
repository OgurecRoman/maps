import requests
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('map.ui', self)
        self.find.clicked.connect(self.get_map)
        self.link = "http://static-maps.yandex.ru/1.x/"

    def get_map(self):
        coords = f'{self.coords2.text()},{self.coords1.text()}'

        params = {
            'l': 'sat',
            'll': coords,
            'z': self.n.text()
        }
        response = requests.get(self.link, params=params)
        with open('test.png', 'wb') as file:
            file.write(response.content)

        self.pixmap = QPixmap('test.png')
        self.map.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())