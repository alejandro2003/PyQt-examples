
import sys
from PyQt4 import QtGui, QtCore

class MyWidget2(QtGui.QWidget):

    def __init__(self):
        #ejecutar al padre
            QtGui.QWidget.__init__(self)
            self.resize(250, 150)
            # boton ampliar
            button1 = QtGui.QPushButton('Ampliar', self)
            button1.setGeometry(10, 10, 60, 35)

            # self.connect(button1, QtCore.SIGNAL('clicked()'),QtGui.qApp,
            #           QtCore.SLOT('quit()'))

            # otra accion
            self.connect(button1, QtCore.SIGNAL('clicked()'),
                         self.myslot1)  #myslot1 sin parentesis
            self.show()

    def myslot1(self):
        self.resize(500, 200)
        self.setWindowTitle('Slot1')





app = QtGui.QApplication(sys.argv)
qqq = MyWidget2()
sys.exit(app.exec_())