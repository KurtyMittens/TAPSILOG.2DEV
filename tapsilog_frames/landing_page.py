from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from tapsilog_frames import login_frame
from development_uis import tapsi_assets


class Ui_TAPSILOGHOMEPAGE(QtWidgets.QWidget):
    """Landing page serves a vehicle for not bombarding the user for sign up, log in,
     asking developers for concerns, manuals and contacts to reach us!
     GROUP: BDSM
     Designs from yseult, programming from kynamittens"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

    def run_loginFrame(self):
        """closing side frame animation while showing login frame: runs login_frame.py"""
        self.button_anim()
        self.log_in.show()

    def button_anim(self):
        """Open and close animation of the side frame"""
        self.animate = QtCore.QPropertyAnimation(self.side_frame, b'geometry')

        if self.side_frame.width() == 0:
            self.side_frame.show()
            self.animate.setStartValue(
                QtCore.QRect(self.side_frame.x(), self.side_frame.y(), 0, self.side_frame.height()))
            self.side_frame.setGeometry(QtCore.QRect(869, 0, 0, 631))
            self.animate.setEndValue(
                QtCore.QRect(self.side_frame.x(), self.side_frame.y(), 211, self.side_frame.height()))
            self.animate.start()

        else:
            self.animate.setStartValue(
                QtCore.QRect(self.side_frame.x(), self.side_frame.y(), 211, self.side_frame.height()))
            self.side_frame.setGeometry(QtCore.QRect(1100, 0, 211, 631))
            self.animate.setEndValue(
                QtCore.QRect(self.side_frame.x(), self.side_frame.y(), 0, self.side_frame.height()))
            self.animate.start()

    def setupUi(self, TAPSILOGHOMEPAGE):
        """Designing the window"""

        # Basic Settings of the window
        TAPSILOGHOMEPAGE.setObjectName("TAPSILOGHOMEPAGE")
        TAPSILOGHOMEPAGE.resize(1075, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TAPSILOGHOMEPAGE.sizePolicy().hasHeightForWidth())
        TAPSILOGHOMEPAGE.setSizePolicy(sizePolicy)
        TAPSILOGHOMEPAGE.setMaximumSize(QtCore.QSize(1075, 625))
        TAPSILOGHOMEPAGE.setBaseSize(QtCore.QSize(1075, 625))
        TAPSILOGHOMEPAGE.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        TAPSILOGHOMEPAGE.setMouseTracking(False)
        TAPSILOGHOMEPAGE.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/logo_smol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TAPSILOGHOMEPAGE.setWindowIcon(icon)
        TAPSILOGHOMEPAGE.setAutoFillBackground(False)
        TAPSILOGHOMEPAGE.setStyleSheet("")

        # Central Widgets
        self.centralwidget = QtWidgets.QWidget(TAPSILOGHOMEPAGE)
        self.centralwidget.setObjectName("centralwidget")

        # Main Frame Integration
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 1075, 625))
        self.main_frame.setStyleSheet("#main_frame{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.852632 rgb(234, 196, 163), stop:1 rgb(214, 146, 111))\n"
                                      "}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")

        # Log In Frame
        self.log_in = login_frame.Ui_login_frame(self, self.centralwidget)
        self.log_in.hide()

        # Menu Button Integration
        self.menubutton = QtWidgets.QPushButton(self.main_frame)
        self.menubutton.setEnabled(True)
        self.menubutton.clicked.connect(self.button_anim)
        self.menubutton.setGeometry(QtCore.QRect(1010, 10, 50, 50))
        self.menubutton.setMinimumSize(QtCore.QSize(50, 50))
        self.menubutton.setMaximumSize(QtCore.QSize(50, 50))
        self.menubutton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubutton.setAcceptDrops(False)
        self.menubutton.setStyleSheet("QPushButton {\n"
                                      "   \n"
                                      "    border-color: rgb(0, 0, 0);\n"
                                      "border-radius: 23px;\n"
                                      "    border-style:solid;\n"
                                      "    image: url(:/pics/assets/menu_bar.png);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover{\n"
                                      "    background-color: rgb(214, 146, 111);\n"
                                      "}")
        self.menubutton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.menubutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(""), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.menubutton.setIcon(icon1)
        self.menubutton.setIconSize(QtCore.QSize(60, 60))
        self.menubutton.setCheckable(True)
        self.menubutton.setChecked(False)
        self.menubutton.setAutoRepeat(True)
        self.menubutton.setDefault(False)
        self.menubutton.setFlat(True)
        self.menubutton.setObjectName("menubutton")

        # The side Frame
        self.side_frame = QtWidgets.QFrame(self.main_frame)
        self.side_frame.setGeometry(QtCore.QRect(1100, 0, 0, 631))
        self.side_frame.setStyleSheet("#side_frame{\n"
                                      "background-color: rgb(214, 146, 111);\n"
                                      "}")
        self.side_frame.hide()
        self.side_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_frame.setObjectName("side_frame")

        # Log In button of the side frame
        self.login_butt = QtWidgets.QPushButton(self.side_frame)
        self.login_butt.setGeometry(QtCore.QRect(0, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.login_butt.setFont(font)
        self.login_butt.setStyleSheet("QPushButton{\n"
                                      "font: 75 12pt \"Gill Sans MT\";\n"
                                      "border-width: 5px;\n"
                                      "border-color: rgb(0, 0, 0);\n"
                                      "border-radius: 20px;\n"
                                      "}\n"
                                      "QPushButton::hover{\n"
                                      "    font: 75 13pt \"Gill Sans MT\";\n"
                                      "    text-decoration: underline;\n"
                                      "color: rgb(255, 255, 255);"
                                      "}\n"
                                      "")
        self.login_butt.setObjectName("login_butt")
        self.login_butt.clicked.connect(self.run_loginFrame)  # Opens the login_frame.py

        # Product Button page
        self.product_butt = QtWidgets.QPushButton(self.side_frame)
        self.product_butt.setGeometry(QtCore.QRect(0, 230, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.product_butt.setFont(font)
        self.product_butt.setStyleSheet("QPushButton{\n"
                                        "font: 75 12pt \"Gill Sans MT\";\n"
                                        "border-width: 5px;\n"
                                        "border-color: rgb(0, 0, 0);\n"
                                        "border-radius: 20px;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "    font: 75 13pt \"Gill Sans MT\";\n"
                                        "    text-decoration: underline;\n"
                                        "color: rgb(255, 255, 255);"
                                        "}")
        self.product_butt.setObjectName("product_butt")

        # About Button
        self.about_button = QtWidgets.QPushButton(self.side_frame)
        self.about_button.setGeometry(QtCore.QRect(0, 330, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.about_button.setFont(font)
        self.about_button.setStyleSheet("QPushButton{\n"
                                        "font: 75 12pt \"Gill Sans MT\";\n"
                                        "border-width: 5px;\n"
                                        "border-color: rgb(0, 0, 0);\n"
                                        "border-radius: 20px;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "    font: 75 13pt \"Gill Sans MT\";\n"
                                        "    text-decoration: underline;\n"
                                        "color: rgb(255, 255, 255);"
                                        "}")
        self.about_button.setObjectName("about_button")

        # Inquiry Button
        self.inquiry_butt = QtWidgets.QPushButton(self.side_frame)
        self.inquiry_butt.setGeometry(QtCore.QRect(0, 430, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.inquiry_butt.setFont(font)
        self.inquiry_butt.setStyleSheet("QPushButton{\n"
                                        "font: 75 12pt \"Gill Sans MT\";\n"
                                        "border-width: 5px;\n"
                                        "border-color: rgb(0, 0, 0);\n"
                                        "border-radius: 20px;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "    font: 75 13pt \"Gill Sans MT\";\n"
                                        "    text-decoration: underline;\n"
                                        "color: rgb(255, 255, 255);"
                                        "}\n"
                                        "")
        self.inquiry_butt.setObjectName("inquiry_butt")

        # Line in the main homepage
        self.line = QtWidgets.QFrame(self.main_frame)
        self.line.setGeometry(QtCore.QRect(0, 310, 1071, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        # Labels
        self.label = QtWidgets.QLabel(self.main_frame)
        self.label.setGeometry(QtCore.QRect(360, 160, 371, 321))
        self.label.setStyleSheet("background-color: rgb(234, 196, 163);\n"
                                 "image: url(:/pics/assets/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.main_frame)
        self.label_2.setGeometry(QtCore.QRect(270, 110, 221, 51))
        self.label_2.setStyleSheet("font: 75 10pt \"Gill Sans MT\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.main_frame)
        self.label_3.setGeometry(QtCore.QRect(330, 500, 471, 51))
        self.label_3.setStyleSheet("font: 75 10pt \"Gill Sans MT\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.main_frame)
        self.label_4.setGeometry(QtCore.QRect(330, 460, 471, 51))
        self.label_4.setStyleSheet("font: 75 10pt \"Gill Sans MT\";")
        self.label_4.setObjectName("label_4")

        # Other Settings and basic layouts
        self.line.raise_()
        self.side_frame.raise_()
        self.menubutton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        # Re translating Forms
        self.retranslateUi(TAPSILOGHOMEPAGE)
        QtCore.QMetaObject.connectSlotsByName(TAPSILOGHOMEPAGE)

    def retranslateUi(self, TAPSILOGHOMEPAGE):
        """HTML RICH TEXT"""
        _translate = QtCore.QCoreApplication.translate
        TAPSILOGHOMEPAGE.setWindowTitle(_translate("TAPSILOGHOMEPAGE", "TAPSILOG HOMEPAGE"))
        self.menubutton.setToolTip(_translate("TAPSILOGHOMEPAGE", "menu"))
        self.login_butt.setText(_translate("TAPSILOGHOMEPAGE", "LOGIN"))
        self.product_butt.setText(_translate("TAPSILOGHOMEPAGE", "PRODUCT"))
        self.about_button.setText(_translate("TAPSILOGHOMEPAGE", "ABOUT"))
        self.inquiry_butt.setText(_translate("TAPSILOGHOMEPAGE", "HAVING PROBLEMS?"))
        self.label_2.setText(_translate("TAPSILOGHOMEPAGE",
                                        "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Welcome to</span></p></body></html>"))
        self.label_3.setText(_translate("TAPSILOGHOMEPAGE",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Gill Sans MT\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
                                        "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">SATISFY THE CRAVE FOR INNOVATION</span></p></body></html>"))
        self.label_4.setText(_translate("TAPSILOGHOMEPAGE",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Gill Sans MT\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">An AI Security System</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    run = Ui_TAPSILOGHOMEPAGE()
    sys.exit(app.exec_())
