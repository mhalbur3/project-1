from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 337)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frameMainMenu = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameMainMenu.setGeometry(QtCore.QRect(20, 20, 440, 300))
        self.frameMainMenu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameMainMenu.setObjectName("frameMainMenu")

        self.labelTitle = QtWidgets.QLabel(parent=self.frameMainMenu)
        self.labelTitle.setGeometry(QtCore.QRect(160, 30, 160, 30))
        self.labelTitle.setObjectName("labelTitle")

        self.buttonVote = QtWidgets.QPushButton(parent=self.frameMainMenu)
        self.buttonVote.setGeometry(QtCore.QRect(60, 130, 120, 40))
        self.buttonVote.setObjectName("buttonVote")

        self.buttonExit = QtWidgets.QPushButton(parent=self.frameMainMenu)
        self.buttonExit.setGeometry(QtCore.QRect(230, 130, 120, 40))
        self.buttonExit.setObjectName("buttonExit")

        self.frameVoteMenu = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameVoteMenu.setGeometry(QtCore.QRect(20, 20, 440, 300))
        self.frameVoteMenu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameVoteMenu.setObjectName("frameVoteMenu")
        self.frameVoteMenu.hide()

        self.labelChoose = QtWidgets.QLabel(parent=self.frameVoteMenu)
        self.labelChoose.setGeometry(QtCore.QRect(150, 20, 180, 30))
        self.labelChoose.setObjectName("labelChoose")

        self.radioJohn = QtWidgets.QRadioButton(parent=self.frameVoteMenu)
        self.radioJohn.setGeometry(QtCore.QRect(50, 80, 150, 30))
        self.radioJohn.setObjectName("radioJohn")

        self.radioJane = QtWidgets.QRadioButton(parent=self.frameVoteMenu)
        self.radioJane.setGeometry(QtCore.QRect(220, 80, 150, 30))
        self.radioJane.setObjectName("radioJane")

        self.labelID = QtWidgets.QLabel(parent=self.frameVoteMenu)
        self.labelID.setGeometry(QtCore.QRect(50, 50, 100, 20))
        self.labelID.setObjectName("labelID")

        self.inputID = QtWidgets.QLineEdit(parent=self.frameVoteMenu)
        self.inputID.setGeometry(QtCore.QRect(150, 50, 200, 20))
        self.inputID.setObjectName("inputID")

        self.buttonSubmitVote = QtWidgets.QPushButton(parent=self.frameVoteMenu)
        self.buttonSubmitVote.setGeometry(QtCore.QRect(50, 150, 130, 35))
        self.buttonSubmitVote.setObjectName("buttonSubmitVote")

        self.buttonBack = QtWidgets.QPushButton(parent=self.frameVoteMenu)
        self.buttonBack.setGeometry(QtCore.QRect(210, 150, 130, 35))
        self.buttonBack.setObjectName("buttonBack")

        self.textResults = QtWidgets.QTextEdit(parent=self.frameVoteMenu)
        self.textResults.setGeometry(QtCore.QRect(40, 200, 331, 91))
        self.textResults.setReadOnly(True)
        self.textResults.setObjectName("textResults")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voting System"))
        self.labelTitle.setText(_translate("MainWindow", "Voting System"))
        self.buttonVote.setText(_translate("MainWindow", "Vote"))
        self.buttonExit.setText(_translate("MainWindow", "Exit"))
        self.labelChoose.setText(_translate("MainWindow", "Choose a Candidate"))
        self.radioJohn.setText(_translate("MainWindow", "John"))
        self.radioJane.setText(_translate("MainWindow", "Jane"))
        self.buttonSubmitVote.setText(_translate("MainWindow", "Submit Vote"))
        self.buttonBack.setText(_translate("MainWindow", "Back"))
        self.labelID.setText(_translate("MainWindow", "Enter Voter ID:"))

