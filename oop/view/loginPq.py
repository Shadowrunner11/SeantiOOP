from PyQt5.QtWidgets import *
import sys


class Root(QDialog):
    def __init__(self, parent=None):
        super(Root, self).__init__(parent)
        button= QPushButton("Hola",self)
        button.clicked.connect(self.handle)
    def handle(self):
        print("Hola")




if __name__ == "__main__":
    Applicaction = QApplication(sys.argv)
    App = Root()
    App.show()
    sys.exit(Applicaction.exec_())
