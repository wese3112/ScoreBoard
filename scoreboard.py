# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from scoreboard_ui import Ui_MainWindow
from scoreboard_widget_ui import Ui_ScoreboardWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Player(QtGui.QWidget):
#class Player(object):
    def __init__(self, name, parent):
        super(Player, self).__init__()
        self.name = name
        self.score = 0

        # create widget and add it to main window
        self.scoreboard = Ui_ScoreboardWidget()
        self.scoreboard.setupUi(parent)
        self.scoreboard.setLayout(self.scoreboard.verticalLayout_2)
        parent.ui.horizontalLayout.addWidget(self.scoreboard)
        self.scoreboard.setLayout(self.scoreboard.verticalLayout_2)

        # set up signals etc
        self.scoreboard.lblPlayername.setText(parent.ui.ledPlayerName.text())
        self.scoreboard.btnPlus1.released.connect(self.btnPlus1_clicked)
        self.scoreboard.btnMinus1.released.connect(self.btnMinus1_clicked)

    def btnPlus1_clicked(self):
        self.score += 1
        self.update_score()

    def btnMinus1_clicked(self):
        self.score -= 1
        self.update_score()

    def update_score(self):
        self.scoreboard.lcdPoints.display(str(self.score))
        self.emit(QtCore.SIGNAL('update_score'))



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # user code here
        self.Players = dict()
        self.PlayersL = list()

        self.ui.btnAddplayer.released.connect(self.btnAddplayer_clicked)
        self.ui.btnStart.released.connect(self.btnStart_clicked)
        self.ui.tblRanking.setColumnWidth(0, 140)
        self.ui.tblRanking.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)

    def btnStart_clicked(self):
        for player in self.PlayersL:
            player.score = 0
            player.update_score()
        self.update_score_tbl()

    def btnAddplayer_clicked(self):
        if self.ui.ledPlayerName.text() == '':
            print 'no player name'
        elif self.ui.ledPlayerName.text() in [p.name for p in self.PlayersL]:
            print 'name already exists! choose a different one!'
        else:
            playerName = self.ui.ledPlayerName.text()
            self.PlayersL.append(Player(playerName, self))
            self.connect(self.PlayersL[-1], QtCore.SIGNAL("update_score"), self.update_score_tbl)
            self.ui.tblRanking.setRowCount(len(self.PlayersL))
            self.update_score_tbl()

    def update_score_tbl(self):
        self.PlayersL.sort(key=self.get_score, reverse=True)

        row = 0
        for player in self.PlayersL:
            self.ui.tblRanking.setItem(row, 0, QtGui.QTableWidgetItem(player.name))
            self.ui.tblRanking.setItem(row, 1, QtGui.QTableWidgetItem(str(player.score)))
            row += 1

    def get_score(self, player):
        return player.score

    def player_name_by_score(self, score):
        for player in self.PlayersL:
            if score == player.score:
                return player.name
        return 'Error'

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())



















