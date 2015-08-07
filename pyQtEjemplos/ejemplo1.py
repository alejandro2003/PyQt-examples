

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 350)
widget.setWindowTitle('My Widget')
widget.show()


sys.exit(app.exec_())