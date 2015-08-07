

import sys
from PyQt4 import QtGui

class MyWidget(QtGui.QWidget):

    def __init__(self):
        #ejecutar al padre
            QtGui.QWidget.__init__(self)
            self.resize(250, 150)
            self.setWindowTitle('Ejemplo')
            self.setWindowIcon(QtGui.QIcon('icon1.png'))

            self.setToolTip('This is a <b>QWidget</b> widget')
            QtGui.QToolTip.setFont(QtGui.QFont('Comic Sans MS', 20))
            self.show()

# inicio del objeto principal de la aplicacion
app = QtGui.QApplication(sys.argv)
# llamada a clase
qqq = MyWidget()
sys.exit(app.exec_())