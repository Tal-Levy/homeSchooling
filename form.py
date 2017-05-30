# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(530, 523)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.answer_window = QtGui.QTextEdit(self.centralwidget)
        self.answer_window.setGeometry(QtCore.QRect(300, 130, 200, 64))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.answer_window.setFont(font)
        self.answer_window.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard)
        self.answer_window.setObjectName(_fromUtf8("answer_window"))
        self.question_window = QtGui.QTextBrowser(self.centralwidget)
        self.question_window.setGeometry(QtCore.QRect(80, 130, 200, 64))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_window.sizePolicy().hasHeightForWidth())
        self.question_window.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.question_window.setFont(font)
        self.question_window.setObjectName(_fromUtf8("question_window"))
        self.restart_button = QtGui.QPushButton(self.centralwidget)
        self.restart_button.setGeometry(QtCore.QRect(80, 30, 95, 80))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restart_button.sizePolicy().hasHeightForWidth())
        self.restart_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.restart_button.setFont(font)
        self.restart_button.setAutoFillBackground(False)
        self.restart_button.setObjectName(_fromUtf8("restart_button"))
        self.img_display = QtGui.QLabel(self.centralwidget)
        self.img_display.setGeometry(QtCore.QRect(162, 210, 256, 256))
        self.img_display.setText(_fromUtf8(""))
        self.img_display.setObjectName(_fromUtf8("img_display"))
        self.audio_button = QtGui.QPushButton(self.centralwidget)
        self.audio_button.setGeometry(QtCore.QRect(30, 150, 32, 32))
        self.audio_button.setStyleSheet(_fromUtf8(""))
        self.audio_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/audio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audio_button.setIcon(icon)
        self.audio_button.setObjectName(_fromUtf8("audio_button"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.restart_button.setText(_translate("MainWindow", "RESTART", None))

