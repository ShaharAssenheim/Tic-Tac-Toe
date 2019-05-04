"""This is the code of the classic game "eix-eigul",
in this approach the computer has an artificial intelligence capabilities,
what Making it invincible.
The code written in python and the GUI with PyQt5."""

from PyQt5 import QtCore, QtGui, QtWidgets
import logo
import random

# variables defined to know what symbol the player and computer play at each round.
global playerSymbol, computerSymbol
playerSymbol = ''
computerSymbol = ''
# variables defined the game table.
global myTable
myTable = [' '] * 10
global position
position = 0
global comp_round_mum
comp_round_mum = 0

"""Class of the main program, controlling the GUI and the algorithm methods"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # definition of all GUI parameters.
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(711, 706)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 706))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/grey-background-v1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.startbtn = QtWidgets.QPushButton(self.centralwidget)
        self.startbtn.setGeometry(QtCore.QRect(380, 620, 131, 61))
        self.startbtn.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.startbtn.setObjectName("startbtn")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(220, 320, 301, 261))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/newPrefix/pic.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.logo.show()
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(180, 10, 351, 301))
        self.welcome.setText("")
        self.welcome.setPixmap(QtGui.QPixmap(":/newPrefix/log.png"))
        self.welcome.setScaledContents(True)
        self.welcome.setObjectName("welcome")
        self.welcome.show()
        self.homebtn = QtWidgets.QPushButton(self.centralwidget)
        self.homebtn.setGeometry(QtCore.QRect(20, 640, 81, 51))
        self.homebtn.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.homebtn.setObjectName("homebtn")
        self.homebtn.hide()
        self.newgamebtn = QtWidgets.QPushButton(self.centralwidget)
        self.newgamebtn.setGeometry(QtCore.QRect(300, 640, 121, 51))
        self.newgamebtn.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.newgamebtn.setObjectName("newgamebtn")
        self.newgamebtn.hide()
        self.box1 = QtWidgets.QPushButton(self.centralwidget)
        self.box1.setGeometry(QtCore.QRect(20, 70, 211, 181))
        self.box1.setText("")
        self.box1.setObjectName("box1")
        self.box1.hide()
        self.box4 = QtWidgets.QPushButton(self.centralwidget)
        self.box4.setGeometry(QtCore.QRect(20, 260, 211, 181))
        self.box4.setText("")
        self.box4.setObjectName("box4")
        self.box4.hide()
        self.box7 = QtWidgets.QPushButton(self.centralwidget)
        self.box7.setGeometry(QtCore.QRect(20, 450, 211, 181))
        self.box7.setText("")
        self.box7.setObjectName("box7")
        self.box7.hide()
        self.box8 = QtWidgets.QPushButton(self.centralwidget)
        self.box8.setGeometry(QtCore.QRect(250, 450, 211, 181))
        self.box8.setText("")
        self.box8.setObjectName("box8")
        self.box8.hide()
        self.box2 = QtWidgets.QPushButton(self.centralwidget)
        self.box2.setGeometry(QtCore.QRect(250, 70, 211, 181))
        self.box2.setText("")
        self.box2.setObjectName("box2_2")
        self.box2.hide()
        self.box5 = QtWidgets.QPushButton(self.centralwidget)
        self.box5.setGeometry(QtCore.QRect(250, 260, 211, 181))
        self.box5.setText("")
        self.box5.setObjectName("box5")
        self.box5.hide()
        self.box9 = QtWidgets.QPushButton(self.centralwidget)
        self.box9.setGeometry(QtCore.QRect(480, 450, 211, 181))
        self.box9.setText("")
        self.box9.setObjectName("box9")
        self.box9.hide()
        self.box3 = QtWidgets.QPushButton(self.centralwidget)
        self.box3.setGeometry(QtCore.QRect(480, 70, 211, 181))
        self.box3.setText("")
        self.box3.setObjectName("box3")
        self.box3.hide()
        self.box6 = QtWidgets.QPushButton(self.centralwidget)
        self.box6.setGeometry(QtCore.QRect(480, 260, 211, 181))
        self.box6.setText("")
        self.box6.setObjectName("box6")
        self.box6.hide()
        self.line1 = QtWidgets.QLabel(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(20, 440, 671, 16))
        self.line1.setText("")
        self.line1.setPixmap(QtGui.QPixmap(":/newPrefix/line1.png"))
        self.line1.setScaledContents(True)
        self.line1.setObjectName("line1")
        self.line1.hide()
        self.line2 = QtWidgets.QLabel(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(20, 250, 671, 16))
        self.line2.setText("")
        self.line2.setPixmap(QtGui.QPixmap(":/newPrefix/line1.png"))
        self.line2.setScaledContents(True)
        self.line2.setObjectName("line2")
        self.line2.hide()
        self.line3 = QtWidgets.QLabel(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(230, 70, 21, 561))
        self.line3.setText("")
        self.line3.setPixmap(QtGui.QPixmap(":/newPrefix/line2.png"))
        self.line3.setObjectName("line3")
        self.line3.hide()
        self.line4 = QtWidgets.QLabel(self.centralwidget)
        self.line4.setGeometry(QtCore.QRect(460, 70, 21, 561))
        self.line4.setText("")
        self.line4.setPixmap(QtGui.QPixmap(":/newPrefix/line2.png"))
        self.line4.setObjectName("line4")
        self.line4.hide()
        self.winline = QtWidgets.QLabel(self.centralwidget)
        self.winline.setGeometry(QtCore.QRect(50, 130, 651, 51))
        self.winline.setText("")
        self.winline.setPixmap(QtGui.QPixmap(":/newPrefix/redline.png"))
        self.winline.setScaledContents(True)
        self.winline.setObjectName("winline")
        self.winline.hide()
        self.winline2 = QtWidgets.QLabel(self.centralwidget)
        self.winline2.setGeometry(QtCore.QRect(40, 320, 651, 51))
        self.winline2.setText("")
        self.winline2.setPixmap(QtGui.QPixmap(":/newPrefix/redline.png"))
        self.winline2.setScaledContents(True)
        self.winline2.setObjectName("winline2")
        self.winline2.hide()
        self.winline3 = QtWidgets.QLabel(self.centralwidget)
        self.winline3.setGeometry(QtCore.QRect(50, 510, 651, 51))
        self.winline3.setText("")
        self.winline3.setPixmap(QtGui.QPixmap(":/newPrefix/redline.png"))
        self.winline3.setScaledContents(True)
        self.winline3.setObjectName("winline3")
        self.winline3.hide()
        self.winline4 = QtWidgets.QLabel(self.centralwidget)
        self.winline4.setGeometry(QtCore.QRect(90, 100, 51, 511))
        self.winline4.setText("")
        self.winline4.setPixmap(QtGui.QPixmap(":/newPrefix/redline.png"))
        self.winline4.setScaledContents(True)
        self.winline4.setObjectName("winline4")
        self.winline4.hide()
        self.winline5 = QtWidgets.QLabel(self.centralwidget)
        self.winline5.setGeometry(QtCore.QRect(330, 110, 51, 511))
        self.winline5.setText("")
        self.winline5.setPixmap(QtGui.QPixmap(":/newPrefix/redline.png"))
        self.winline5.setScaledContents(True)
        self.winline5.setObjectName("winline5")
        self.winline5.hide()
        self.winline6 = QtWidgets.QLabel(self.centralwidget)
        self.winline6.setGeometry(QtCore.QRect(560, 100, 51, 511))
        self.winline6.setText("")
        self.winline6.setPixmap(QtGui.QPixmap(":/newPrefix/redline.png"))
        self.winline6.setScaledContents(True)
        self.winline6.setObjectName("winline6")
        self.winline6.hide()
        self.winline7 = QtWidgets.QLabel(self.centralwidget)
        self.winline7.setGeometry(QtCore.QRect(50, 100, 631, 501))
        self.winline7.setText("")
        self.winline7.setPixmap(QtGui.QPixmap(":/newPrefix/redline3.png"))
        self.winline7.setScaledContents(True)
        self.winline7.setObjectName("winline7")
        self.winline7.hide()
        self.winline8 = QtWidgets.QLabel(self.centralwidget)
        self.winline8.setGeometry(QtCore.QRect(40, 100, 631, 501))
        self.winline8.setText("")
        self.winline8.setPixmap(QtGui.QPixmap(":/newPrefix/redline4.png"))
        self.winline8.setScaledContents(True)
        self.winline8.setObjectName("winline8")
        self.winline8.hide()
        self.compwon = QtWidgets.QLabel(self.centralwidget)
        self.compwon.setGeometry(QtCore.QRect(100, -10, 471, 81))
        self.compwon.setText("")
        self.compwon.setPixmap(QtGui.QPixmap(":/newPrefix/compwon.png"))
        self.compwon.setScaledContents(True)
        self.compwon.setObjectName("compwon")
        self.compwon.hide()
        self.tie = QtWidgets.QLabel(self.centralwidget)
        self.tie.setGeometry(QtCore.QRect(170, -10, 351, 81))
        self.tie.setText("")
        self.tie.setPixmap(QtGui.QPixmap(":/newPrefix/tie.png"))
        self.tie.setScaledContents(True)
        self.tie.setObjectName("tie")
        self.tie.hide()
        self.youwin = QtWidgets.QLabel(self.centralwidget)
        self.youwin.setGeometry(QtCore.QRect(190, -10, 291, 81))
        self.youwin.setText("")
        self.youwin.setPixmap(QtGui.QPixmap(":/newPrefix/youwon.png"))
        self.youwin.setScaledContents(True)
        self.youwin.setObjectName("youwin")
        self.youwin.hide()
        self.choose = QtWidgets.QLabel(self.centralwidget)
        self.choose.setGeometry(QtCore.QRect(240, 0, 381, 71))
        self.choose.setText("")
        self.choose.setPixmap(QtGui.QPixmap(":/newPrefix/choose.png"))
        self.choose.setScaledContents(True)
        self.choose.setObjectName("choose")
        self.choose.hide()
        self.eix = QtWidgets.QPushButton(self.centralwidget)
        self.eix.setGeometry(QtCore.QRect(210, 20, 41, 31))
        self.eix.setText("")
        self.eix.setObjectName("eix")
        self.eix.setStyleSheet("\n""font: 24pt \"Matura MT Script Capitals\";")
        self.eix.hide()
        self.eigul = QtWidgets.QPushButton(self.centralwidget)
        self.eigul.setGeometry(QtCore.QRect(150, 20, 41, 31))
        self.eigul.setText("")
        self.eigul.setStyleSheet("\n""font: 24pt \"Matura MT Script Capitals\";")
        self.eigul.setObjectName("eigul")
        self.eigul.hide()
        self.youstart = QtWidgets.QLabel(self.centralwidget)
        self.youstart.setGeometry(QtCore.QRect(220, 0, 241, 71))
        self.youstart.setText("")
        self.youstart.setPixmap(QtGui.QPixmap(":/newPrefix/youstart.png"))
        self.youstart.setScaledContents(True)
        self.youstart.setObjectName("youstart")
        self.youstart.hide()
        self.compstart = QtWidgets.QLabel(self.centralwidget)
        self.compstart.setGeometry(QtCore.QRect(240, 0, 241, 71))
        self.compstart.setText("")
        self.compstart.setPixmap(QtGui.QPixmap(":/newPrefix/compstart.png"))
        self.compstart.setScaledContents(True)
        self.compstart.setObjectName("compstart")
        self.compstart.hide()
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(200, 620, 131, 61))
        self.exit.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.homebtn.clicked.connect(self.homebtn.hide)
        self.homebtn.clicked.connect(self.box1.hide)
        self.homebtn.clicked.connect(self.box2.hide)
        self.homebtn.clicked.connect(self.box3.hide)
        self.homebtn.clicked.connect(self.box4.hide)
        self.homebtn.clicked.connect(self.box5.hide)
        self.homebtn.clicked.connect(self.box6.hide)
        self.homebtn.clicked.connect(self.box7.hide)
        self.homebtn.clicked.connect(self.box8.hide)
        self.homebtn.clicked.connect(self.box9.hide)
        self.homebtn.clicked.connect(self.line1.hide)
        self.homebtn.clicked.connect(self.line2.hide)
        self.homebtn.clicked.connect(self.line3.hide)
        self.homebtn.clicked.connect(self.line4.hide)
        self.homebtn.clicked.connect(self.choose.hide)
        self.homebtn.clicked.connect(self.eix.hide)
        self.homebtn.clicked.connect(self.eigul.hide)
        self.homebtn.clicked.connect(self.newgamebtn.hide)
        self.homebtn.clicked.connect(self.logo.show)
        self.homebtn.clicked.connect(self.welcome.show)
        self.homebtn.clicked.connect(self.startbtn.show)
        self.homebtn.clicked.connect(self.change_Exit_location)
        self.homebtn.clicked.connect(self.winline.hide)
        self.homebtn.clicked.connect(self.winline2.hide)
        self.homebtn.clicked.connect(self.winline3.hide)
        self.homebtn.clicked.connect(self.winline4.hide)
        self.homebtn.clicked.connect(self.winline5.hide)
        self.homebtn.clicked.connect(self.winline6.hide)
        self.homebtn.clicked.connect(self.winline7.hide)
        self.homebtn.clicked.connect(self.winline8.hide)
        self.homebtn.clicked.connect(self.youstart.hide)
        self.homebtn.clicked.connect(self.compstart.hide)
        self.homebtn.clicked.connect(self.youwin.hide)
        self.homebtn.clicked.connect(self.compwon.hide)
        self.homebtn.clicked.connect(self.tie.hide)
        self.startbtn.clicked.connect(self.logo.hide)
        self.startbtn.clicked.connect(self.welcome.hide)
        self.startbtn.clicked.connect(self.startbtn.hide)
        self.startbtn.clicked.connect(self.box1.show)
        self.box1.setEnabled(False)
        self.startbtn.clicked.connect(self.box2.show)
        self.box2.setEnabled(False)
        self.startbtn.clicked.connect(self.box3.show)
        self.box3.setEnabled(False)
        self.startbtn.clicked.connect(self.box4.show)
        self.box4.setEnabled(False)
        self.startbtn.clicked.connect(self.box5.show)
        self.box5.setEnabled(False)
        self.startbtn.clicked.connect(self.box6.show)
        self.box6.setEnabled(False)
        self.startbtn.clicked.connect(self.box7.show)
        self.box7.setEnabled(False)
        self.startbtn.clicked.connect(self.box8.show)
        self.box8.setEnabled(False)
        self.startbtn.clicked.connect(self.box9.show)
        self.box9.setEnabled(False)
        self.startbtn.clicked.connect(self.choose.show)
        self.startbtn.clicked.connect(self.eix.show)
        self.startbtn.clicked.connect(self.eigul.show)
        self.startbtn.clicked.connect(self.line1.show)
        self.startbtn.clicked.connect(self.line2.show)
        self.startbtn.clicked.connect(self.line3.show)
        self.startbtn.clicked.connect(self.line4.show)
        self.startbtn.clicked.connect(self.homebtn.show)
        self.startbtn.clicked.connect(self.newgamebtn.show)
        self.startbtn.clicked.connect(self.cleanTable)
        self.newgamebtn.clicked.connect(self.cleanTable)
        self.exit.clicked.connect(self.exitFunction)

        self.box1.clicked.connect(lambda: self.choosenPosition(1))
        self.box2.clicked.connect(lambda: self.choosenPosition(2))
        self.box3.clicked.connect(lambda: self.choosenPosition(3))
        self.box4.clicked.connect(lambda: self.choosenPosition(4))
        self.box5.clicked.connect(lambda: self.choosenPosition(5))
        self.box6.clicked.connect(lambda: self.choosenPosition(6))
        self.box7.clicked.connect(lambda: self.choosenPosition(7))
        self.box8.clicked.connect(lambda: self.choosenPosition(8))
        self.box9.clicked.connect(lambda: self.choosenPosition(9))
        self.eix.clicked.connect(lambda : self.chooseSymbol(1))
        self.eigul.clicked.connect(lambda: self.chooseSymbol(2))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "איקס עיגול - בינה מלאכותית"))
        self.startbtn.setText(_translate("MainWindow", "התחל לשחק"))
        self.homebtn.setText(_translate("MainWindow", "בית"))
        self.newgamebtn.setText(_translate("MainWindow", "משחק חדש"))
        self.eix.setText(_translate("MainWindow", "x"))
        self.eigul.setText(_translate("MainWindow", "o"))
        self.exit.setText(_translate("MainWindow", "יציאה"))

    """GUI Function - set all game table buttons to not enabled"""
    def set_Not_Enable(self):
        self.box1.setEnabled(False)
        self.box2.setEnabled(False)
        self.box3.setEnabled(False)
        self.box4.setEnabled(False)
        self.box5.setEnabled(False)
        self.box6.setEnabled(False)
        self.box7.setEnabled(False)
        self.box8.setEnabled(False)
        self.box9.setEnabled(False)

    """GUI Function - change the exit button position"""
    def change_Exit_location(self):
        self.exit.setGeometry(QtCore.QRect(200, 620, 131, 61))

    """Terminate the program"""
    def exitFunction(self):
        exit(1)

    """The method calld when the player choose a symbol (X or O)
    and decided how will play first."""
    def chooseSymbol(self, chosen):
        self.box1.setEnabled(True)
        self.box2.setEnabled(True)
        self.box3.setEnabled(True)
        self.box4.setEnabled(True)
        self.box5.setEnabled(True)
        self.box6.setEnabled(True)
        self.box7.setEnabled(True)
        self.box8.setEnabled(True)
        self.box9.setEnabled(True)
        self.choose.hide()
        self.eigul.hide()
        self.eix.hide()

        # Assigns a value according to the player's choice.
        global playerSymbol, computerSymbol
        if chosen == 1:
            playerSymbol = 'X'
            computerSymbol = 'O'
        elif chosen == 2:
            playerSymbol = 'O'
            computerSymbol = 'X'

        # Random select who will go first.
        if random.randint(0, 1) == 1:
            self.compstart.show()
            current_turn = 'computer'
        else:
            self.youstart.show()
            current_turn = 'player'

        # turn a flag if the player start.
        # else, the computer start.
        global player_start_flag
        player_start_flag = 0
        if current_turn == 'player':
            player_start_flag = 1
        else:
            current_move = self.computerTurn(myTable, computerSymbol, playerSymbol)
            myTable[current_move] = computerSymbol
            self.PrintCompMove(computerSymbol, current_move)
            if self.findWinner(myTable, computerSymbol,1):
                self.compstart.hide()
                self.youstart.hide()
                self.compwon.show()
                self.set_Not_Enable()
                self.newgamebtn.setEnabled(True)
            elif self.checkForTie(myTable):
                self.compstart.hide()
                self.youstart.hide()
                self.tie.show()
                self.newgamebtn.setEnabled(True)
                self.set_Not_Enable()

    """the function called at any beginning of a game,
    it clean the window and 'myTable' array"""
    def cleanTable(self):
        global comp_round_mum
        comp_round_mum = 0
        global position
        position=0
        self.newgamebtn.setEnabled(False)
        global myTable
        myTable = [' '] * 10
        self.youwin.hide()
        self.tie.hide()
        self.compwon.hide()
        self.compstart.hide()
        self.youstart.hide()
        self.choose.show()
        self.eix.show()
        self.eigul.show()
        self.exit.setGeometry(QtCore.QRect(610, 640, 81, 51))
        self.box1.setStyleSheet("\n""border-image: url(:/newPrefix/);")
        self.box1.setEnabled(False)
        self.box2.setStyleSheet("\n""border-image: url(:/newPrefix/);")
        self.box2.setEnabled(False)
        self.box3.setStyleSheet("\n""border-image: url(:/newPrefix/);")
        self.box3.setEnabled(False)
        self.box4.setStyleSheet("\n""border-image: url(:/newPrefix/);")
        self.box4.setEnabled(False)
        self.box5.setStyleSheet("\n""border-image: url(:/newPrefix/);")
        self.box5.setEnabled(False)
        self.box6.setStyleSheet("\n""border-image: url(:/newPrefix/);")
        self.box6.setEnabled(False)
        self.box7.setStyleSheet("\n""border-image: url(:/newPrefix/);")
        self.box7.setEnabled(False)
        self.box8.setStyleSheet("\n""border-image: url(:/newPrefix/);")
        self.box8.setEnabled(False)
        self.box9.setStyleSheet("\n""border-image: url(:/newPrefix/);")
        self.box9.setEnabled(False)
        self.winline.hide()
        self.winline2.hide()
        self.winline3.hide()
        self.winline4.hide()
        self.winline5.hide()
        self.winline6.hide()
        self.winline7.hide()
        self.winline8.hide()

    """The function control on the player chosen movement
    it place the symbol in the chosen box and after it the computer play."""
    def choosenPosition(self, place):
        global playerSymbol, computerSymbol
        global myTable
        if place == 1:
            if playerSymbol == 'O':
                self.box1.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
                self.box1.setEnabled(False)
            else:
                self.box1.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
                self.box1.setEnabled(False)
        if place == 2:
            if playerSymbol == 'O':
                self.box2.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
                self.box2.setEnabled(False)
            else:
                self.box2.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
                self.box2.setEnabled(False)
        if place == 3:
            if playerSymbol == 'O':
                self.box3.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
                self.box3.setEnabled(False)
            else:
                self.box3.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
                self.box3.setEnabled(False)
        if place == 4:
            if playerSymbol == 'O':
                self.box4.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
                self.box4.setEnabled(False)
            else:
                self.box4.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
                self.box4.setEnabled(False)
        if place == 5:
            if playerSymbol == 'O':
                self.box5.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
                self.box5.setEnabled(False)
            else:
                self.box5.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
                self.box5.setEnabled(False)
        if place == 6:
            if playerSymbol == 'O':
                self.box6.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
                self.box6.setEnabled(False)
            else:
                self.box6.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
                self.box6.setEnabled(False)
        if place == 7:
            if playerSymbol == 'O':
                self.box7.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
                self.box7.setEnabled(False)
            else:
                self.box7.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
                self.box7.setEnabled(False)
        if place == 8:
            if playerSymbol == 'O':
                self.box8.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
                self.box8.setEnabled(False)
            else:
                self.box8.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
                self.box8.setEnabled(False)
        if place == 9:
            if playerSymbol == 'O':
                self.box9.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
                self.box9.setEnabled(False)
            else:
                self.box9.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
                self.box9.setEnabled(False)
        # update myTable array
        if myTable[place] == ' ':
            current_move = int(place)
        myTable[current_move] = playerSymbol
        # looking for a winner or a tie to end the game.
        # otherwise the computer play.
        if self.findWinner(myTable, playerSymbol,1):
            self.compstart.hide()
            self.youstart.hide()
            self.youwin.show()
            self.newgamebtn.setEnabled(True)
            self.set_Not_Enable()
        elif self.checkForTie(myTable):
            self.compstart.hide()
            self.youstart.hide()
            self.tie.show()
            self.newgamebtn.setEnabled(True)
            self.set_Not_Enable()
        else:
            current_move = self.computerTurn(myTable, computerSymbol, playerSymbol)
            myTable[current_move] = computerSymbol
            self.PrintCompMove(computerSymbol, current_move)
            if self.findWinner(myTable, computerSymbol,1):
                self.compstart.hide()
                self.youstart.hide()
                self.compwon.show()
                self.newgamebtn.setEnabled(True)
                self.set_Not_Enable()
            elif self.checkForTie(myTable):
                self.compstart.hide()
                self.youstart.hide()
                self.tie.show()
                self.newgamebtn.setEnabled(True)
                self.set_Not_Enable()

    """This function charge on finding a winner"""
    def findWinner(self, table, symbol, flag_real):
        if (table[7] == symbol and table[8] == symbol and table[9] == symbol):  # horizontal lower
            if flag_real:
                self.winline3.show()
            return 1
        elif (table[4] == symbol and table[5] == symbol and table[6] == symbol):  # horizontal middle
            if flag_real:
                self.winline2.show()
            return 1
        elif (table[1] == symbol and table[2] == symbol and table[3] == symbol):  # horizontal upper
            if flag_real:
                self.winline.show()
            return 1
        elif (table[7] == symbol and table[4] == symbol and table[1] == symbol):  # vertical left
            if flag_real:
                self.winline4.show()
            return 1
        elif (table[8] == symbol and table[5] == symbol and table[2] == symbol):  # vertical middle
            if flag_real:
                self.winline5.show()
            return 1
        elif (table[9] == symbol and table[6] == symbol and table[3] == symbol):  # vertical right
            if flag_real:
                self.winline6.show()
            return 1
        elif (table[7] == symbol and table[5] == symbol and table[3] == symbol):  # diagonal line
            if flag_real:
                self.winline7.show()
            return 1
        elif (table[9] == symbol and table[5] == symbol and table[1] == symbol):  # diagonal line
            if flag_real:
                self.winline8.show()
            return 1

    """The function check if the table is full,
     in this case return True and the game finish with a Tie."""
    def checkForTie(self, table):
        for i in range(1, 10):
            if table[i] == ' ':
                return False
        return True

    """This function copy 'myTable' array, for the computer to testing different scenarios """
    def copyTable(self, table):
        copytable = []
        for i in table:
            copytable.append(i)
        return copytable

    """The function return a valid position on the table from the position list,
        it returns None if there is no valid position."""
    def randomChoosen(self, table, positionList):
        possiblePosition = []
        for i in positionList:
            if table[i] == ' ':
                possiblePosition.append(i)
        if len(possiblePosition) != 0:
            return random.choice(possiblePosition)
        else:
            return None

    """The main artificial intelligence method,
        the computer has few scenarios to check before Before he plays the best move for him"""
    def computerTurn(self, table, computerSymbol, playerSymbol):
        global player_start_flag
        global comp_round_mum
        comp_round_mum = comp_round_mum + 1
        # first the computer check if he can win.
        for i in range(1, 10):
            copy = self.copyTable(table)
            if table[i] == ' ':
                copy[i]=computerSymbol
                if self.findWinner(copy, computerSymbol, 0):
                    player_start_flag = 0
                    return i
        # if not, the computer check if the player can win in his next move.
        for i in range(1, 10):
            copy = self.copyTable(table)
            if table[i] == ' ':
                copy[i] = playerSymbol
                if self.findWinner(copy, playerSymbol, 0):
                    player_start_flag = 0
                    return i

        # if player_start_flag=1 it means that the player play first,
        # then checking if he took the middle, if not take the middle.
        global position
        if (player_start_flag == 1 and table[5] == ' '):
            for i in [2, 4, 6, 8]:
                if not table[i] == ' ':
                    player_start_flag = 2  # the player took one of the middle sides
                    position = i  # we need to save the position for next round.
                    return 5
            else:
                player_start_flag = 3  # the player took one of the  corners
                return 5

        # if the player play first took one of the middle sides, and then the computer took the middle,
        # then the computer next move must be one of the corners around the middle sides.
        elif player_start_flag == 2:
            player_start_flag = 0
            if position == 2:
                return self.randomChoosen(table, [1, 3])
            elif position == 4:
                return self.randomChoosen(table, [1, 7])
            elif position == 6:
                return self.randomChoosen(table, [3, 9])
            elif position == 8:
                return self.randomChoosen(table, [7, 9])

        # if the player play first took one of the corners and then the computer took the middle,
        elif player_start_flag == 3:
            player_start_flag = 0
            for i in [2,4,6,8]:
                if table[i]== playerSymbol:
                    if i == 2:
                        return self.randomChoosen(table, [1, 3])
                    if i == 4:
                        return self.randomChoosen(table, [1, 7])
                    if i == 6:
                        return self.randomChoosen(table, [3, 9])
                    if i == 8:
                        return self.randomChoosen(table, [7, 9])
            return self.randomChoosen(table, [2, 4, 6, 8])

        if(player_start_flag==0 and comp_round_mum==2 and table[5] == ' '):
            return 5

        # if the computer start ot in any other sitoation not mantion above,
        # it take one of the corners if it possible
        current_move = self.randomChoosen(table, [1, 3, 7, 9])
        if current_move != None:
            player_start_flag = 0
            return current_move

        # if not the computer take the middle if it possible
        if table[5] == ' ':
            player_start_flag = 0
            return 5

        # otherwise the computer take one of the middle sides
        else:
            player_start_flag = 0
            return self.randomChoosen(table, [2, 4, 6, 8])

    """The function print the computer move on the GUI window."""
    def PrintCompMove(self, symbol, current_move):
        if current_move == 1:
            if symbol == 'X':
                self.box1.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
            elif symbol == 'O':
                self.box1.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
            self.box1.setEnabled(False)
        if current_move == 2:
            if symbol == 'X':
                self.box2.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
            elif symbol == 'O':
                self.box2.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
            self.box2.setEnabled(False)
        if current_move == 3:
            if symbol == 'X':
                self.box3.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
            elif symbol == 'O':
                self.box3.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
            self.box3.setEnabled(False)
        if current_move == 4:
            if symbol == 'X':
                self.box4.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
            elif symbol == 'O':
                self.box4.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
            self.box4.setEnabled(False)
        if current_move == 5:
            if symbol == 'X':
                self.box5.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
            elif symbol == 'O':
                self.box5.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
            self.box5.setEnabled(False)
        if current_move == 6:
            if symbol == 'X':
                self.box6.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
            elif symbol == 'O':
                self.box6.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
            self.box6.setEnabled(False)
        if current_move == 7:
            if symbol == 'X':
                self.box7.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
            elif symbol == 'O':
                self.box7.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
            self.box7.setEnabled(False)
        if current_move == 8:
            if symbol == 'X':
                self.box8.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
            elif symbol == 'O':
                self.box8.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
            self.box8.setEnabled(False)
        if current_move == 9:
            if symbol == 'X':
                self.box9.setStyleSheet("\n""border-image: url(:/newPrefix/x.png);")
            elif symbol == 'O':
                self.box9.setStyleSheet("\n""border-image: url(:/newPrefix/circle.png);")
            self.box9.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
