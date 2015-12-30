# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K:/programming/python/qt/scoreboard/scoreboard_widget.ui'
#
# Created: Wed Dec 30 16:23:39 2015
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

class Ui_ScoreboardWidget(QtGui.QWidget):
    def setupUi(self, ScoreboardWidget):
        ScoreboardWidget.setObjectName(_fromUtf8("ScoreboardWidget"))
#        ScoreboardWidget.resize(396, 745)
#        self.verticalLayout_2 = QtGui.QVBoxLayout(ScoreboardWidget)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.grpPlayer = QtGui.QGroupBox(ScoreboardWidget)
        self.grpPlayer.setObjectName(_fromUtf8("grpPlayer"))
        self.verticalLayout = QtGui.QVBoxLayout(self.grpPlayer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblPlayername = QtGui.QLabel(self.grpPlayer)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblPlayername.setFont(font)
        self.lblPlayername.setObjectName(_fromUtf8("lblPlayername"))
        self.verticalLayout.addWidget(self.lblPlayername)
        self.line = QtGui.QFrame(self.grpPlayer)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.lblPoints = QtGui.QLabel(self.grpPlayer)
        self.lblPoints.setObjectName(_fromUtf8("lblPoints"))
        self.verticalLayout.addWidget(self.lblPoints)
        self.lcdPoints = QtGui.QLCDNumber(self.grpPlayer)
        self.lcdPoints.setMinimumSize(QtCore.QSize(0, 90))
        self.lcdPoints.setStyleSheet(_fromUtf8("background-color: rgb(85, 85, 127);\n"
"color: rgb(0, 255, 127);"))
        self.lcdPoints.setObjectName(_fromUtf8("lcdPoints"))
        self.verticalLayout.addWidget(self.lcdPoints)
        self.line_2 = QtGui.QFrame(self.grpPlayer)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.btnPlus1 = QtGui.QPushButton(self.grpPlayer)
        self.btnPlus1.setMinimumSize(QtCore.QSize(0, 72))
        self.btnPlus1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnPlus1.setFont(font)
        self.btnPlus1.setObjectName(_fromUtf8("btnPlus1"))
        self.verticalLayout.addWidget(self.btnPlus1)
        self.btnMinus1 = QtGui.QPushButton(self.grpPlayer)
        self.btnMinus1.setMinimumSize(QtCore.QSize(0, 72))
        self.btnMinus1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnMinus1.setFont(font)
        self.btnMinus1.setObjectName(_fromUtf8("btnMinus1"))
        self.verticalLayout.addWidget(self.btnMinus1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.grpPlayer)

        self.retranslateUi(ScoreboardWidget)
        QtCore.QMetaObject.connectSlotsByName(ScoreboardWidget)

    def retranslateUi(self, ScoreboardWidget):
        ScoreboardWidget.setWindowTitle(_translate("ScoreboardWidget", "Form", None))
        self.grpPlayer.setTitle(_translate("ScoreboardWidget", "Player", None))
        self.lblPlayername.setText(_translate("ScoreboardWidget", "PlayerName", None))
        self.lblPoints.setText(_translate("ScoreboardWidget", "Points:", None))
        self.btnPlus1.setText(_translate("ScoreboardWidget", "+1 Point", None))
        self.btnMinus1.setText(_translate("ScoreboardWidget", "-1 Point", None))

