from PyQt5 import QtCore, QtGui, QtWidgets
from development_uis import tapsi_assets
import time
from tapsilog_frames import landing_page
from huck import thisIsHuck
import os
import sys
from urllib import request


class Trainer(QtCore.QObject):
    """
    Multithreading purposes, loading then HUCK Model into the system.
    This code is created by Kynamittens
    """
    running = False
    count = 0
    finished = QtCore.pyqtSignal()
    counter = QtCore.pyqtSignal(int)

    """It will load base to the number of faces registered in the system"""

    def run(self):
        for i in range(len(os.listdir('registered_faces'))):
            time.sleep(1)
            self.counter.emit(i + 1)
            self.count = i
        self.finished.emit()
        self.running = True

    def check_running(self):
        return self.running


class Ui_Form(QtWidgets.QWidget):
    """
        Thi.s app is created with PyQT5 Designer, Designs are From yseult
        Programming is from Kynamittens
        The Program will not run if the device is not connected to the internet
    """

    def __init__(self):
        super().__init__()
        self.huck = thisIsHuck.HUCK()
        self.setupUi(self)  # Own setup and designs
        self.run = Trainer()  # Trainer for multithreading loading
        self.thread = QtCore.QThread()  # multi threader
        self.timer = QtCore.QTimer()  # timer initialization

        if self.check_internet():
            """IF THERES INTERNET CONNECTION
            it connects and open"""
            self.show()

            # Threading
            self.run.moveToThread(self.thread)
            self.thread.started.connect(self.run.run)
            self.run.finished.connect(self.thread.quit)
            self.thread.start()

            self.timer.timeout.connect(self.check_the_running)
            self.timer.start(1000)
        else:
            """YET IF THERES NO CONNECTION
            gives a message box"""
            QtWidgets.QMessageBox.critical(self, "INTERNET IS REQUIRED",
                                           "Please Connect your device to an INTERNET CONNECTION to continue running TAPSILog System")
            sys.exit()

    def check_the_running(self):
        """
        when loading is done...
        :return: The homepage interface
        """
        if self.run.running:
            self.close()
            self.timer.stop()
            self.thread.quit()
            self.run = landing_page.Ui_TAPSILOGHOMEPAGE()  # Goes to Landing page

    def check_internet(self):
        """ internet checking by a website (planning to change if remotely database is done)"""
        try:
            request.urlopen("https://www.youtube.com", timeout=5)
            return True
        except:
            return False

    def setupUi(self, Form):
        """Designing the form"""
        Form.setObjectName("Form")
        Form.resize(378, 515)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Background Frame
        self.Background_frame = QtWidgets.QFrame(Form)
        self.Background_frame.setGeometry(QtCore.QRect(10, 10, 361, 501))
        self.Background_frame.setStyleSheet("#Background_frame{background-color: rgb(0, 0, 0);\n"
                                            "border-radius: 20px;}\n"
                                            "")
        self.Background_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background_frame.setObjectName("Background_frame")

        # The main Frame
        self.Frame_main = QtWidgets.QFrame(self.Background_frame)
        self.Frame_main.setGeometry(QtCore.QRect(10, 10, 341, 481))
        self.Frame_main.setStyleSheet("#Frame_main{background-color: rgb(234, 196, 163);\n"
                                      "border-image: url(:/pics/assets/Add_a_subheading-removebg-preview-removebg-preview.png);\n"
                                      "border-radius: 20px;}\n"
                                      "\n"
                                      "")
        self.Frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Frame_main.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Frame_main.setObjectName("Frame_main")

        # Frame for the logo
        self.logo_loads = QtWidgets.QLabel(self.Frame_main)
        self.logo_loads.setGeometry(QtCore.QRect(50, 30, 241, 241))
        self.logo_loads.setStyleSheet("image: url(:/pics/assets/logo.png);")
        self.logo_loads.setText("")
        self.logo_loads.setObjectName("logo_loads")

        # Label WELCOME
        self.WELCOME = QtWidgets.QLabel(self.Frame_main)
        self.WELCOME.setGeometry(QtCore.QRect(100, 260, 141, 41))
        self.WELCOME.setStyleSheet("font: 18pt \"Pricedown\";")
        self.WELCOME.setObjectName("WELCOME")

        # Loading Animation
        self.gif = QtGui.QMovie('assets/pulse.gif')
        self.loading_gif = QtWidgets.QLabel(self.Frame_main)
        self.loading_gif.setGeometry(QtCore.QRect(120, 350, 101, 81))
        self.gif.setScaledSize(QtCore.QSize(90, 90))
        self.loading_gif.setMovie(self.gif)
        self.loading_gif.setObjectName("loading_gif")
        self.gif.start()

        # Labels
        self.tapsilog = QtWidgets.QLabel(self.Frame_main)
        self.tapsilog.setGeometry(QtCore.QRect(-70, 300, 481, 21))
        self.tapsilog.setStyleSheet("font: 11pt \"Franklin Gothic Demi\";")
        self.tapsilog.setObjectName("tapsilog")
        self.tapsilog_2 = QtWidgets.QLabel(self.Frame_main)
        self.tapsilog_2.setGeometry(QtCore.QRect(100, 320, 141, 31))
        self.tapsilog_2.setStyleSheet("font: 60 8pt \"MS Sans Serif\";")
        self.tapsilog_2.setObjectName("tapsilog_2")

        # Re translating forms
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """HTML Rich text"""
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.WELCOME.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">WELCOME!</span></p></body></html>"))
        self.tapsilog.setText(_translate("Form",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:6pt;\">Total Activity Processed through a Strictly Implemented Log System</span></p></body></html>"))
        self.tapsilog_2.setText(_translate("Form",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">Loading, Please Wait</span></p></body></html>"))


if __name__ == "__main__":
    """Runs the main"""
    ai = thisIsHuck.HUCK()
    app = QtWidgets.QApplication(sys.argv)
    run = Ui_Form()
    sys.exit(app.exec_())
