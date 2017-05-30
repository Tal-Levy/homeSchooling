import sys
import form
from PyQt4 import QtCore, QtGui
import letters
import pygame


class ConnectorToMainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(ConnectorToMainWindow, self).__init__()
        self.expected_letter = ''
        self.timer = QtCore.QTimer()
        self.ui = form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.my_letters = letters.Letters()
        QtCore.QObject.connect(self.ui.restart_button, QtCore.SIGNAL(form._fromUtf8("clicked()")),
                               self.on_restartbutton_click)
        QtCore.QObject.connect(self.ui.audio_button, QtCore.SIGNAL(form._fromUtf8("clicked()")),
                               self.on_audiobutton_click)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.on_restartbutton_click()

    def on_restartbutton_click(self) :
        self.my_letters.re_init()
        self.ui.answer_window.clear()
        self.ui.img_display.clear()
        self.generate_a_letter()

    def on_audiobutton_click(self) :
        self.play_audio("./audio/letters/{}.mp3".format(self.expected_letter))

    def generate_a_letter(self) :
        self.ui.img_display.clear()
        letter = self.my_letters.pick_a_letter()
        self.play_audio("./audio/letters/{}.mp3".format(letter))
        self.expected_letter = letter
        self.ui.question_window.setText('{0}  {1}'.format(letter.upper(), letter))
        self.ui.answer_window.setFocus()

    def verify_result(self) :
        if str(self.ui.answer_window.toPlainText()).lower() == self.expected_letter :
            self.display_image(QtGui.QPixmap("./imgs/happy.png"))
            self.ui.answer_window.clear()
            QtCore.QTimer.singleShot(2000, self.generate_a_letter)
        else :
            self.display_image(QtGui.QPixmap("./imgs/try_again.png"))
            self.ui.answer_window.clear()
            self.retry()

    def retry(self) :
        self.ui.question_window.setText('{0}  {1}'.format(self.expected_letter.upper(),
                                                        self.expected_letter))
        self.on_audiobutton_click()
        self.ui.answer_window.setFocus()

    def display_image(self, img) :
        self.ui.img_display.setPixmap(img)
        self.ui.img_display.show()

    def play_audio(self, path) :
        pygame.mixer.init(frequency = 8000, channels = 1)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

    def keyPressEvent(self, e):
        self.ui.img_display.clear()
        if e.key() != QtCore.Qt.Key_Return and e.key() != QtCore.Qt.Key_Enter:
            if e.key() != QtCore.Qt.Key_Backspace:
                self.ui.answer_window.insertPlainText(str(e.text()).upper())
            else:
                mstr = str(self.ui.answer_window.toPlainText())[:-1]
                self.ui.answer_window.clear()
                self.ui.answer_window.insertPlainText(mstr)
        else:
            self.verify_result()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ConnectorToMainWindow()
    myapp.show()
    sys.exit(app.exec_())