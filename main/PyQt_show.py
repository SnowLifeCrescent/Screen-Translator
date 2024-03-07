from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import Qt


class ControlWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)  # 设置窗口为独立置顶窗口
        self.setGeometry(100, 100, 200, 20)  # 设置窗口位置和大小
        self.setWindowOpacity(0.5)  # 设置窗口透明度
        self.setStyleSheet("font-size : 13px; font-family : Microsoft YaHei; color : rgba(0, 0, 0, 255);")
        self.setWindowTitle("控制处")
        self.button_toggle_stay_on_top = QPushButton("置顶")
        self.button_toggle_stay_on_top.clicked.connect(self.toggle_stay_on_top)

        layout = QVBoxLayout()
        layout.addWidget(self.button_toggle_stay_on_top)
        self.setLayout(layout)

    def toggle_stay_on_top(self):
        parent_window = self.parent()
        if parent_window is not None:
            flags = parent_window.windowFlags()
            if flags & Qt.WindowStaysOnTopHint:  # 窗口当前为置顶状态
                flags &= ~Qt.WindowStaysOnTopHint  # 取消置顶
            else:
                flags |= Qt.WindowStaysOnTopHint  # 设置为置顶
            parent_window.setWindowFlags(flags)
            parent_window.frameGeometry().moveCenter(QDesktopWidget().availableGeometry().center())  # 窗口居中
            parent_window.show()


class TextShow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 设置窗口无边框且置顶
        self.setAttribute(Qt.WA_TransparentForMouseEvents)  # 设置窗口点击穿透
        self.setWindowOpacity(0.2)  # 设置窗口透明度
        self.showFullScreen()  # 设置窗口全屏

        self.label_list = [QLabel(parent=self) for _ in range(100)]  # 创建标签列表
        #  [label.setStyleSheet("font-size: 15px; font-family: Microsoft YaHei; color: rgba(0, 0, 0, 255);"
        #                     "background-color: rgba(255, 255, 255, 200); font-weight: bold;")
        # for label in self.label_list]  # 设置标签样式
        #  [label.adjustSize() for label in self.label_list]  # 调整标签大小
        #  [label.show() for label in self.label_list]  # 显示标签

        self.control_window = ControlWindow(parent=self)  # 创建控制窗口
        self.control_window.show()

    def show_text(self, text, position):
        self.clear_text()  # 清空文本
        print("Show text start.")
        try:
            for i in range(len(text)):
                print(f"进入循环, i = {i}")
                self.label_list[i].setText(text[i])  # 设置标签文本
                self.label_list[i].setStyleSheet("font-size: 15px;"
                                                 " font-family: Microsoft YaHei;"
                                                 " color: rgba(0, 0, 0, 255);"
                                                 " background-color: rgba(255, 255, 255, 200);"
                                                 " font-weight: bold;")
                self.label_list[i].setMinimumWidth(self.label_list[i].sizeHint().width())  # 设置宽度
                self.label_list[i].setMinimumHeight(self.label_list[i].sizeHint().height())  # 设置高度
                x, y, width, height = position[i]
                print(f"Position: {x}, {y}, {width}, {height}")
                self.label_list[i].move(x, y+6)  # 设置标签位置
                self.label_list[i].show()  # 显示标签
                print("显示中....")
        except Exception as e:
            print(f"Show text failed: {e}")

    def clear_text(self):
        try:
            for label in self.label_list:
                label.setText("")  # 清空标签文本
                label.hide()  # 隐藏标签
        except Exception as e:
            print(f"Clear text failed: {e}")

    def hide_text(self):
        try:
            self.hide()
        except Exception as e:
            print(f"Hide text failed: {e}")

    def de_hide_text(self):
        try:
            self.show()
        except Exception as e:
            print(f"De-hide text failed: {e}")
