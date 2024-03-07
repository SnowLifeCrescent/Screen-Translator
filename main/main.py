import sys
from translator import Translator
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QVBoxLayout, QWidget, QDesktopWidget


class TranslationApp(QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类构造函数
        self.setWindowTitle("实时翻译工具")
        self.setGeometry(200, 500, 300, 200)
        self.move(QDesktopWidget().availableGeometry().center())

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.start_button = QPushButton("开始翻译", self)
        self.start_button.clicked.connect(self.start_translation)
        self.layout.addWidget(self.start_button)

        self.stop_button = QPushButton("终止翻译", self)
        self.stop_button.clicked.connect(self.stop_translation)
        self.layout.addWidget(self.stop_button)
        self.translator = Translator()

    def start_translation(self):
        try:
            self.translator.start()
        except Exception as e:
            print(f"Start translation failed: {e}")

    def stop_translation(self):
        try:
            self.translator.stop()
        except Exception as e:
            print(f"Stop translation failed: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslationApp()
    window.show()
    sys.exit(app.exec_())
