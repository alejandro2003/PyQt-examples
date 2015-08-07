import sys
from PyQt4 import QtGui, QtCore


#  MainWindow es mas potente que Widget
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(250, 150)

        button1 = QtGui.QPushButton('Ampliar', self)
        button1.setGeometry(10, 10, 60, 35)
        self.connect(button1, QtCore.SIGNAL('clicked()'),
                         self.myslot1)  #myslot1 sin parentesis
        self.show()


    # las acciones al pulsar el boton
    def myslot1(self):
            self.resize(500, 200)
            self.setWindowTitle('Slot1')
            self.statusBar().showMessage('Ready')

app = QtGui.QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec_())