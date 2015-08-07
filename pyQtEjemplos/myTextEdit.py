
import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        # self en editor para que sea visible desde fuera de init
        self.editor = QtGui.QTextEdit()
        self.setCentralWidget(self.editor)
        # editor.setText("blablabla")

        #filename = QtGui.QFileDialog.getOpenFileName(self)
        #openedFile = open(filename,'r')
        #print openedFile.encoding  # ?
        #txt = openedFile.read()
        #openedFile.close()
        #editor.setText(txt)

        #fff = open('4.txt', 'w')
        #fff.write(txt)
        #fff.close()

        # menu exit
        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        self.connect(exitAction, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        # menu new
        newAction = QtGui.QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New File')
        self.connect(newAction, QtCore.SIGNAL('triggered()'), self.newFile)

         # menu open
        openAction = QtGui.QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file')
        self.connect(openAction, QtCore.SIGNAL('triggered()'), self.openFile)

         # menu SaveAs
        saveAction = QtGui.QAction('Save As', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save file as')
        self.connect(saveAction, QtCore.SIGNAL('triggered()'), self.saveAs)

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')

        file.addAction(newAction)
        file.addAction(openAction)
        file.addAction(saveAction)
        file.addAction(exitAction)

    def newFile(self):
        self.editor.setText("")

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self)
        openedFile = open(filename,'r')
        txt = openedFile.read()
        openedFile.close()
        self.editor.setText(txt)

    def saveAs(self):
        filename = QtGui.QFileDialog.getSaveFileName(self)
        openedFile = open(filename,'w')
        txt = self.editor.toPlainText() # plainText para llegar al contenido del editor
        openedFile.write(txt)
        openedFile.close()



app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())