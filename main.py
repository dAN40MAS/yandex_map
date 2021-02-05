from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
import os
import requests
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.map_file_name = 'map.png'

        self.setupUi(self)
        self.ok_btn.clicked.connect(self.show_result)

    def closeEvent(self, event):
        os.remove(self.map_file_name)

    def show_result(self):
        try:
            self.statusbar.clearMessage()
            coords = self.coords_input.text()
            scale = self.scale_input.text()

            params = {
                'l': 'map',
                'll': ','.join(list(reversed(coords.split(', ')))),
                'z': int(scale)
            }
            response = requests.get('https://static-maps.yandex.ru/1.x/', params=params)
            if not response:
                raise ValueError('Неправильные значения')
            with open(self.map_file_name, 'wb') as f:
                f.write(response.content)

            pixmap = QPixmap(self.map_file_name)
            self.map_image.setPixmap(pixmap)
        except Exception as e:
            self.statusbar.showMessage(f'Ошибка: {e}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
