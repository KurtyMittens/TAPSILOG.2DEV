from PyQt5 import QtCore, QtGui, QtWidgets
from development_uis import tapsi_assets
from tapsilog_frames import mainTapsilog, login_support
from database import tapsi_sql


class Ui_login_frame(QtWidgets.QFrame):
    """
    The login Frame for the Admins
    Designs are from yseult
    Programming and backend logic kynamittens
    Database logic and encrypting xeno
    """

    def __init__(self, main, frame):
        super().__init__(frame)
        self.database_connect = tapsi_sql.TapsilogSql()
        self.frame = frame
        self.landing_page = main  # Takes the Landing page for an easy closing of window
        self.setupUi(self)

    def forgot_pressed(self):
        self.forgot_frame.show()

    def back_pressed(self):
        """When pressed, the frame will close and refreshes, returning to the main landing page"""
        self.hide()
        self.loading.stop()
        self.loading_frame.hide()
        self.buttons_frame.show()

    def login_pressed(self):
        """Login Button is pressed. The loading animation will start,
        takes the data from email and password entry {UPDATE this part when database is good}"""
        self.buttons_frame.hide()
        self.loading_frame.show()
        self.loading.start()
        self.all_admins = self.database_connect.show_admin()
        self.inputted_email = self.email_entry.text()
        self.inputted_pass = self.password_entry.text()
        self.found = []
        try:
            if self.inputted_email == "" or self.inputted_pass == "":
                QtWidgets.QMessageBox.information(self, "WARNING!", "All entries should have input!")
                self.loading.stop()
                self.loading_frame.hide()
                self.buttons_frame.show()

            else:
                for i, j in enumerate(self.all_admins):
                    if j[3].lower() == self.inputted_email:
                        self.found = self.all_admins[i]
                        break

                if len(self.found) == 0:
                    QtWidgets.QMessageBox.critical(self, "LOG IN UNSUCCESSFUL!",
                                                   "Login variables doesn't match our database")
                    self.loading.stop()
                    self.password_entry.setText("")
                    self.email_entry.setText("")
                    self.loading_frame.hide()
                    self.buttons_frame.show()
                else:
                    if str(self.found[4]).lower() == self.inputted_pass:
                        """When its true it closes the whole landing page opening the main TAPSILog System"""
                        QtWidgets.QMessageBox.information(self, 'LOG IN SUCCESSFUL!',
                                                          'Proceeding to the TAPSILog System...')
                        self.landing_page.close()
                        self.name = self.found[2]
                        self.database_connect.add_admin_log_in(self.found[0])
                        self.database_connect.close_connection()
                        self.run = mainTapsilog.Ui_MainWindow(self.name, self.found[0])  # Opening the mainTapsilog.py
                    else:
                        """When its false, stops the loading animation. Presenting an error dialogue"""
                        QtWidgets.QMessageBox.critical(self, "LOG IN UNSUCCESSFUL!", "Password is incorrect")
                        self.password_entry.setText("")
                        self.loading.stop()
                        self.loading_frame.hide()
                        self.buttons_frame.show()
        except:
            QtWidgets.QMessageBox.critical(self, "AN ERROR OCCURED", "I dunno what you do but it causes the program to crash, please don't do it again - HUCK")

    def setupUi(self, login_frame):
        """Designing the frame"""

        # Login Frame settings
        login_frame.setObjectName("login_frame")
        login_frame.resize(1075, 625)
        login_frame.setStyleSheet("#login_frame{\n"
                                  "background-color: rgb(214, 146, 111);\n"
                                  "}")

        # Inner Frame
        self.frame = QtWidgets.QFrame(login_frame)
        self.frame.setGeometry(QtCore.QRect(50, 60, 971, 521))
        self.frame.setStyleSheet("#frame{\n"
                                 "background-color: rgb(234, 196, 163);\n"
                                 "border-radius: 69px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.forgot_frame = login_support.Ui_support_frame(login_frame)
        self.forgot_frame.hide()

        # Email Entry and settings
        self.email_entry = QtWidgets.QLineEdit(self.frame)
        self.email_entry.setGeometry(QtCore.QRect(50, 180, 361, 51))
        self.email_entry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 75 15pt \"Gill Sans MT\";\n"
                                       "border-radius: 10px;")
        self.email_entry.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.email_entry.setClearButtonEnabled(True)
        self.email_entry.setObjectName("email_entry")

        # Password entry and settings
        self.password_entry = QtWidgets.QLineEdit(self.frame)
        self.password_entry.setGeometry(QtCore.QRect(50, 260, 361, 51))
        self.password_entry.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.password_entry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "font: 75 15pt \"Gill Sans MT\";\n"
                                          "border-radius: 10px;")
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_entry.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.password_entry.setClearButtonEnabled(True)
        self.password_entry.setObjectName("email_entry_2")

        # Labels
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 70, 281, 51))
        self.label_6.setStyleSheet("font: 75 10pt \"Gill Sans MT\";")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(460, 10, 441, 461))
        self.label.setStyleSheet("image: url(:/pics/assets/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(80, 110, 281, 51))
        self.label_8.setStyleSheet("font: 75 10pt \"Gill Sans MT\";")
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(460, 430, 471, 51))
        self.label_5.setStyleSheet("font: 75 10pt \"Gill Sans MT\";")
        self.label_5.setObjectName("label_5")

        # Frame for Login Button
        self.buttons_frame = QtWidgets.QFrame(self.frame)
        self.buttons_frame.setGeometry(QtCore.QRect(120, 350, 191, 121))
        self.buttons_frame.setStyleSheet("#button_frame{\n"
                                         "background-color: rgb(234, 196, 163);\n"
                                         "}")
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_frame.setObjectName("buttons_frame")

        # Login Button
        self.login_button = QtWidgets.QPushButton(self.buttons_frame)
        self.login_button.setGeometry(QtCore.QRect(10, 20, 171, 51))
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setToolTip("")
        self.login_button.setWhatsThis("")
        self.login_button.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(214, 146, 111);\n"
                                        "border-radius: 20px;\n"
                                        "    font: 15pt \"Gill Sans Ultra Bold\";\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}")
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.login_pressed)  # runs the Login algo before opening mainTapsilog.py

        # Forgot Button
        self.forgot_pass_btn = QtWidgets.QPushButton(self.buttons_frame)
        self.forgot_pass_btn.setGeometry(QtCore.QRect(20, 70, 161, 28))
        self.forgot_pass_btn.setStyleSheet("QPushButton{\n"
                                           "font: 75 12pt \"Gill Sans MT\";\n"
                                           "border-width: 5px;\n"
                                           "border-color: rgb(0, 0, 0);\n"
                                           "border-radius: 20px;\n"
                                           "}\n"
                                           "QPushButton::hover{\n"
                                           "    font: 75 13pt \"Gill Sans MT\";\n"
                                           "    text-decoration: underline;\n"
                                           "    \n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "}")
        self.forgot_pass_btn.setFlat(True)
        self.forgot_pass_btn.setObjectName("forgot_pass_btn")
        self.forgot_pass_btn.clicked.connect(self.forgot_pressed)

        # loading Frame and Animations
        self.loading_frame = QtWidgets.QFrame(self.frame)
        self.loading_frame.setGeometry(QtCore.QRect(120, 350, 191, 121))
        self.loading_frame.setStyleSheet("background-color: rgb(234, 196, 163);")
        self.loading_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loading_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loading_frame.setObjectName("loading_frame")
        self.loading = QtGui.QMovie('assets/pulse.gif')
        self.loading_pixmap = QtWidgets.QLabel(self.loading_frame)
        self.loading_pixmap.setGeometry(QtCore.QRect(14, 15, 161, 91))
        self.loading_pixmap.setMovie(self.loading)
        self.loading_pixmap.setObjectName("loading_pixmap")

        # Exit Button
        self.exit_button = QtWidgets.QPushButton(login_frame)
        self.exit_button.setEnabled(True)
        self.exit_button.setGeometry(QtCore.QRect(1010, 10, 50, 50))
        self.exit_button.setMinimumSize(QtCore.QSize(50, 50))
        self.exit_button.setMaximumSize(QtCore.QSize(50, 50))
        self.exit_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.exit_button.setAcceptDrops(False)
        self.exit_button.setStyleSheet("QPushButton {\n"
                                       "   \n"
                                       "    background-color: rgb(234, 196, 163);\n"
                                       "    border-color: rgb(0, 0, 0);\n"
                                       "border-radius: 23px;\n"
                                       "    border-style:solid;\n"
                                       "    image: url(:/pics/assets/exit.png);\n"
                                       "    \n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::hover{\n"
                                       "    background-color: rgb(214, 146, 111);\n"
                                       "}")
        self.exit_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.exit_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/BUTTON_ORIG-removebg-preview.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QtCore.QSize(60, 60))
        self.exit_button.setCheckable(True)
        self.exit_button.setChecked(False)
        self.exit_button.setAutoRepeat(True)
        self.exit_button.setDefault(False)
        self.exit_button.setFlat(True)
        self.exit_button.setObjectName("menubutton")
        self.exit_button.clicked.connect(self.back_pressed) # Closes the frame returning to the main landing frame

        # Other Settings
        self.loading_frame.raise_()
        self.label_6.raise_()
        self.email_entry.raise_()
        self.password_entry.raise_()
        self.label.raise_()
        self.label_8.raise_()
        self.label_5.raise_()
        self.buttons_frame.raise_()

        # Re translating Form
        self.retranslateUi(login_frame)
        QtCore.QMetaObject.connectSlotsByName(login_frame)

    def retranslateUi(self, login_frame):
        """HTML Rich Text"""
        _translate = QtCore.QCoreApplication.translate
        login_frame.setWindowTitle(_translate("login_frame", "Frame"))
        self.label_6.setText(_translate("login_frame",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">SECURITY</span></p></body></html>"))
        self.email_entry.setPlaceholderText(_translate("login_frame", "Email"))
        self.password_entry.setPlaceholderText(_translate("login_frame", "Password"))
        self.label_8.setText(_translate("login_frame",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">LOG IN</span></p></body></html>"))
        self.label_5.setText(_translate("login_frame",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Gill Sans MT\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
                                        "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">SATISFY THE CRAVE FOR INNOVATION</span></p></body></html>"))
        self.login_button.setText(_translate("login_frame", "LOG IN"))
        self.forgot_pass_btn.setText(_translate("login_frame", "Forgot Password?"))
        self.exit_button.setToolTip(_translate("login_frame", "menu"))
