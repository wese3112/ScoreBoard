# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scoreboard.ui'
#
# Created: Wed Dec 30 17:22:14 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(762, 723)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.ledPlayerName = QtGui.QLineEdit(self.groupBox)
        self.ledPlayerName.setMinimumSize(QtCore.QSize(200, 40))
        self.ledPlayerName.setText(_fromUtf8(""))
        self.ledPlayerName.setObjectName(_fromUtf8("ledPlayerName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.ledPlayerName)
        self.btnAddplayer = QtGui.QPushButton(self.groupBox)
        self.btnAddplayer.setMinimumSize(QtCore.QSize(0, 40))
        self.btnAddplayer.setObjectName(_fromUtf8("btnAddplayer"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.btnAddplayer)
        self.verticalLayout.addLayout(self.formLayout)
        self.btnStart = QtGui.QPushButton(self.groupBox)
        self.btnStart.setMinimumSize(QtCore.QSize(0, 40))
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.verticalLayout.addWidget(self.btnStart)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tblRanking = QtGui.QTableWidget(self.groupBox)
        self.tblRanking.setObjectName(_fromUtf8("tblRanking"))
        self.tblRanking.setColumnCount(2)
        self.tblRanking.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblRanking.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblRanking.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tblRanking)
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Overview", None))
        self.btnAddplayer.setText(_translate("MainWindow", "Add player", None))
        self.btnStart.setText(_translate("MainWindow", "Start new game", None))
        self.label.setText(_translate("MainWindow", "Ranking", None))
        item = self.tblRanking.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tblRanking.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Score", None))

