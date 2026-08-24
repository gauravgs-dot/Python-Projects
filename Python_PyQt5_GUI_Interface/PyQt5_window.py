import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My Cool first GUI")
        self.setGeometry(700, 300, 500, 500)

        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        self.setWindowIcon(QIcon(icon_path))


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()