import requests
import sys

from PyQt5.Qt import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QSpinBox
from PyQt5.QtGui import QPixmap, QKeyEvent


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
            'z': self.zoom.text()
        }
        response = requests.get(self.link, params=params)
        with open('test.png', 'wb') as file:
            file.write(response.content)

        self.pixmap = QPixmap('test.png')
        self.map.setPixmap(self.pixmap)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_PageUp:
            new_value = int(self.zoom.text()) + 1
            self.zoom.setValue(new_value)
            self.get_map()
        if event.key() == Qt.Key_PageDown:
            new_value = int(self.zoom.text()) - 1
            self.zoom.setValue(new_value)
            self.get_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())