from PySide6 import QtWidgets, QtGui, QtCore
from imap_CleanUp_Dialog import imap_ClnUp
from cleanUp_MailBx import iMapMailBox, create_CutOffDt
import sys


global mailBox
mailBox = iMapMailBox()
app = QtWidgets.QApplication(sys.argv)
MainWindow = imap_ClnUp.iMapDialog()
MainWindow.show()
sys.exit(app.exec_())
