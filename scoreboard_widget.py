# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from scoreboard_widget_ui import Ui_ScoreboardWidget

class Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ScoreboardWidget()
        self.ui.setupUi(self)

        # user code here
        # QtCore.QObject.connect(self.ui.btnOpen, QtCore.SIGNAL("clicked()"), self.btnOpen_clicked)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Form()
    myapp.show()
    sys.exit(app.exec_())
