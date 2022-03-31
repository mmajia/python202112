# coding=gbk
import sys

from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QMessageBox,QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = randint(1,100)

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('学点编程吧--猜数字')
        self.setWindowIcon(QIcon('123.ico'))

        self.bt1 = QPushButton('启动',self)
        self.bt1.setGeometry(115,150,70,30)
        self.bt1.setToolTip('<b>点击这里猜数字<b>')
        self.bt1.clicked.connect(self.iopp)

        self.text = QLineEdit('在这里输入数字',self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80,50,150,30)

        self.show()

    def showMessage(self):
        guessnumber = int(self.text.text())
        print(self.num)

        if guessnumber>self.num:
            QMessageBox.about(self,'看结果','猜大了！')
            self.text.setFocus()
        elif guessnumber<self.num:
            QMessageBox.about(self,'看结果','猜小了！')
        else:
            QMessageBox.about(self,'看结果','答对了！进入下一轮！')
            self.num = randint(1,100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event):
        reply = QMessageBox.question(self,'确认','确认退出吗',QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def iopp(self):
        input(6666)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())