import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(700, 300, 500, 500)

        label1 = QLabel(self)
        label1.setGeometry(0, 0, 250, 250)

        # Get the path of icon.png
        image_path = os.path.join(os.path.dirname(__file__), "icon.png")

        pixmap = QPixmap(image_path)

        # Check if image was loaded
        print("Image loaded:", not pixmap.isNull())
        print("Image path:", image_path)

        label1.setPixmap(pixmap)
        label1.setScaledContents(True)

        # Center the image
        label1.setGeometry(
            (self.width() - label1.width()) // 2,
            (self.height() - label1.height()) // 2,
            label1.width(),
            label1.height()
        )


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()