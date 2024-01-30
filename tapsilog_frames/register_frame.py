from PyQt5 import QtCore, QtGui, QtWidgets
from database import tapsi_sql


class Ui_registration_frame(QtWidgets.QFrame):
    def __init__(self, frame, account_id):
        super().__init__(frame)
        self.setupUi(self)
        self.database_connection = tapsi_sql.TapsilogSql()
        self.account_id = account_id

    def reset(self):
        self.hm_fname_entry.setText("")
        self.hm_lname_entry.setText("")
        self.hm_block_entry.setText("")
        self.hm_lot_entry.setText("")
        self.hm_contact_entry.setText("")
        self.hm_email_entry.setText("")
        self.hm_password_entry.setText("")
        self.hm_cpassword_entry.setText("")
        self.vs_affliation_entry.setText("")
        self.vs_fname_entry.setText("")
        self.vs_lname_entry.setText("")
        self.vs_contact_entry.setText("")
        self.vs_reason.setText("")
        self.vs_email_entry.setText("")

    def register_visitor(self):
        try:
            reg_code = self.database_connection.add_admin_reg(self.account_id)
            self.database_connection.add_visitor_by_admin(self.vs_affliation_entry.text(), self.vs_fname_entry.text(), self.vs_lname_entry.text(), self.vs_contact_entry.text(), self.vs_email_entry.text(), self.vs_reason.text(), reg_code)
            QtWidgets.QMessageBox.information(self, "REGISTER SUCCESSFUL",
                                           f"The Visitor {self.vs_fname_entry.text()}, {self.vs_lname_entry.text()} is succesfully registered!")
            self.reset()
        except:
            QtWidgets.QMessageBox.critical(self, "REGISTER UNSUCCESSFUL", "An Error occurred")

    def register_homeowner(self):
        try:
            if self.hm_password_entry.text() == self.hm_cpassword_entry.text():
                regcode = self.database_connection.add_admin_reg(self.account_id)
                self.database_connection.add_homeowner(self.hm_fname_entry.text(), self.hm_lname_entry.text(), self
                                                       .hm_block_entry.text(), self.hm_lot_entry.text(), self.hm_contact_entry.text(), self.hm_email_entry.text(),
                                                       self.hm_password_entry.text(), regcode)
                QtWidgets.QMessageBox.information(self, "REGISTER SUCCESSFUL", f"The Homeowner {self.hm_fname_entry.text()}, {self.hm_lname_entry.text()} is succesfully registered!")
                self.reset()

            else:
                QtWidgets.QMessageBox.critical(self, "REGISTER UNSUCCESSFUL", "Passwords doesn't match!")
        except:
            QtWidgets.QMessageBox.critical(self, "PROBLEM OCCURRED", "Even HUCK can't comprehend what you did...")

    def setupUi(self, registration_frame):
        registration_frame.setObjectName("registration_frame")
        registration_frame.resize(921, 721)
        registration_frame.setMinimumSize(QtCore.QSize(921, 721))
        registration_frame.setMaximumSize(QtCore.QSize(921, 721))
        registration_frame.setStyleSheet("#registration_frame{\n"
                                         "    background-color: rgb(234, 196, 163);\n"
                                         "}")
        self.register_folder = QtWidgets.QTabWidget(registration_frame)
        self.register_folder.setGeometry(QtCore.QRect(50, 110, 821, 581))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.register_folder.setFont(font)
        self.register_folder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.register_folder.setStyleSheet("selection-background-color: rgb(234, 196, 163);\n"
                                           "border-color: rgb(234, 196, 163);")
        self.register_folder.setTabPosition(QtWidgets.QTabWidget.North)
        self.register_folder.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.register_folder.setElideMode(QtCore.Qt.ElideNone)
        self.register_folder.setUsesScrollButtons(False)
        self.register_folder.setDocumentMode(False)
        self.register_folder.setTabsClosable(False)
        self.register_folder.setObjectName("register_folder")

        """HOMEOWNER REGISTRATION"""
        self.homeowner = QtWidgets.QWidget()
        self.homeowner.setStyleSheet("background-color: rgb(234, 216, 195);")
        self.homeowner.setObjectName("homeowner")

        # LABELS
        self.label_18 = QtWidgets.QLabel(self.homeowner)
        self.label_18.setGeometry(QtCore.QRect(290, 10, 271, 31))
        self.label_18.setStyleSheet("font: 14pt \"Reem Kufi\";")
        self.label_18.setObjectName("label_18")
        self.line = QtWidgets.QFrame(self.homeowner)
        self.line.setGeometry(QtCore.QRect(0, 10, 981, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_19 = QtWidgets.QLabel(self.homeowner)
        self.label_19.setGeometry(QtCore.QRect(30, 140, 111, 20))
        self.label_19.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_19.setObjectName("label_19")
        self.label_13 = QtWidgets.QLabel(self.homeowner)
        self.label_13.setGeometry(QtCore.QRect(420, 140, 111, 21))
        self.label_13.setStyleSheet("\n"
                                    "font: 12pt \"Reem Kufi\";")
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.homeowner)
        self.label_15.setGeometry(QtCore.QRect(30, 190, 55, 21))
        self.label_15.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_15.setObjectName("label_15")
        self.label_12 = QtWidgets.QLabel(self.homeowner)
        self.label_12.setGeometry(QtCore.QRect(420, 190, 101, 21))
        self.label_12.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.homeowner)
        self.label_11.setGeometry(QtCore.QRect(30, 240, 121, 21))
        self.label_11.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_11.setObjectName("label_11")
        self.label_21 = QtWidgets.QLabel(self.homeowner)
        self.label_21.setGeometry(QtCore.QRect(420, 240, 61, 31))
        self.label_21.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_21.setObjectName("label_21")
        self.label_14 = QtWidgets.QLabel(self.homeowner)
        self.label_14.setGeometry(QtCore.QRect(30, 290, 131, 21))
        self.label_14.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.homeowner)
        self.label_16.setGeometry(QtCore.QRect(420, 290, 121, 31))
        self.label_16.setStyleSheet("font: 8pt \"Reem Kufi\";")
        self.label_16.setObjectName("label_16")
        self.label_20 = QtWidgets.QLabel(self.homeowner)
        self.label_20.setGeometry(QtCore.QRect(270, 480, 341, 21))
        self.label_20.setStyleSheet("\n"
                                    "font: 8pt \"Reem Kufi\";")
        self.label_20.setObjectName("label_20")
        self.label_17 = QtWidgets.QLabel(self.homeowner)
        self.label_17.setGeometry(QtCore.QRect(270, 500, 371, 16))
        self.label_17.setStyleSheet("\n"
                                    "font: 8pt \"Reem Kufi\";")
        self.label_17.setObjectName("label_17")

        # SUBMIT BUTTON
        self.submit_button_hm = QtWidgets.QPushButton(self.homeowner)
        self.submit_button_hm.setGeometry(QtCore.QRect(630, 480, 151, 41))
        self.submit_button_hm.setStyleSheet("QPushButton{\n"
                                            "    border-radius: 15px;\n"
                                            "}\n"
                                            "QPushButton:enabled {\n"
                                            "   background-color: #eac4a3;\n"
                                            "   color: #fffff;\n"
                                            "font: 10pt \"Reem Kufi\";\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "   background-color: #CE8865;\n"
                                            "   color: #000000;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover:!pressed {\n"
                                            "   background-color: #eac4a3;\n"
                                            "   color: #ffffff;\n"
                                            "    border-radius: 23px;\n"
                                            "border-radius: 15px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:disabled {\n"
                                            "   background-color: #eac4a3;\n"
                                            "   color: #000000;\n"
                                            "}\n"
                                            "")
        self.submit_button_hm.setObjectName("submit_button_hm")
        self.submit_button_hm.clicked.connect(self.register_homeowner)

        # Password Entry - Homeowner
        self.hm_password_entry = QtWidgets.QLineEdit(self.homeowner)
        self.hm_password_entry.setGeometry(QtCore.QRect(140, 280, 271, 31))
        self.hm_password_entry.setStyleSheet("border-radius: 15px;\n"
                                             "background-color: rgb(255, 255, 255);")
        self.hm_password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.hm_password_entry.setObjectName("hm_password_entry")

        # Confirm Password - Homeowner
        self.hm_cpassword_entry = QtWidgets.QLineEdit(self.homeowner)
        self.hm_cpassword_entry.setGeometry(QtCore.QRect(530, 280, 271, 31))
        self.hm_cpassword_entry.setStyleSheet("border-radius: 15px;\n"
                                              "background-color: rgb(255, 255, 255);")
        self.hm_cpassword_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.hm_cpassword_entry.setObjectName("hm_cpassword_entry")

        # Lot Entry - Homeowner
        self.hm_lot_entry = QtWidgets.QLineEdit(self.homeowner)
        self.hm_lot_entry.setGeometry(QtCore.QRect(530, 230, 271, 31))
        self.hm_lot_entry.setStyleSheet("border-radius: 15px;\n"
                                        "background-color: rgb(255, 255, 255);")
        self.hm_lot_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.hm_lot_entry.setObjectName("hm_lot_entry")

        # Block Entry - Homeowner
        self.hm_block_entry = QtWidgets.QLineEdit(self.homeowner)
        self.hm_block_entry.setGeometry(QtCore.QRect(530, 180, 271, 31))
        self.hm_block_entry.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(255, 255, 255);")
        self.hm_block_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.hm_block_entry.setObjectName("hm_block_entry")

        # Last Entry - Homeowner
        self.hm_lname_entry = QtWidgets.QLineEdit(self.homeowner)
        self.hm_lname_entry.setGeometry(QtCore.QRect(530, 130, 271, 31))
        self.hm_lname_entry.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(255, 255, 255);")
        self.hm_lname_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.hm_lname_entry.setObjectName("hm_lname_entry")

        # Contact Number Entry - Homeowner
        self.hm_contact_entry = QtWidgets.QLineEdit(self.homeowner)
        self.hm_contact_entry.setGeometry(QtCore.QRect(140, 230, 271, 31))
        self.hm_contact_entry.setStyleSheet("border-radius: 15px;\n"
                                            "background-color: rgb(255, 255, 255);")
        self.hm_contact_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.hm_contact_entry.setObjectName("hm_contact_entry")

        # Email Entry - Homeowner
        self.hm_email_entry = QtWidgets.QLineEdit(self.homeowner)
        self.hm_email_entry.setGeometry(QtCore.QRect(140, 180, 271, 31))
        self.hm_email_entry.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(255, 255, 255);")
        self.hm_email_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.hm_email_entry.setObjectName("hm_email_entry")

        # First name Entry - Homeowner
        self.hm_fname_entry = QtWidgets.QLineEdit(self.homeowner)
        self.hm_fname_entry.setGeometry(QtCore.QRect(140, 130, 271, 31))
        self.hm_fname_entry.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(255, 255, 255);")
        self.hm_fname_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.hm_fname_entry.setObjectName("hm_fname_entry")

        # Other Homeowner Options
        self.label_14.raise_()
        self.line.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_13.raise_()
        self.label_15.raise_()
        self.label_12.raise_()
        self.label_11.raise_()
        self.label_21.raise_()
        self.label_16.raise_()
        self.label_20.raise_()
        self.label_17.raise_()
        self.submit_button_hm.raise_()
        self.hm_password_entry.raise_()
        self.hm_cpassword_entry.raise_()
        self.hm_lot_entry.raise_()
        self.hm_block_entry.raise_()
        self.hm_lname_entry.raise_()
        self.hm_contact_entry.raise_()
        self.hm_email_entry.raise_()
        self.hm_fname_entry.raise_()
        self.register_folder.addTab(self.homeowner, "")

        """VISITOR REGISTRATION"""
        self.visitor = QtWidgets.QWidget()
        self.visitor.setStyleSheet("border-color: rgb(213, 145, 110);\n"
                                   "background-color: #d5916e\n"
                                   "")
        self.visitor.setObjectName("visitor")
        self.line_5 = QtWidgets.QFrame(self.visitor)
        self.line_5.setGeometry(QtCore.QRect(0, 10, 991, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label = QtWidgets.QLabel(self.visitor)
        self.label.setGeometry(QtCore.QRect(170, 10, 501, 31))
        self.label.setStyleSheet("font: 14pt \"Reem Kufi\";")
        self.label.setObjectName("label")

        # First name entry - Visitors
        self.vs_fname_entry = QtWidgets.QLineEdit(self.visitor)
        self.vs_fname_entry.setGeometry(QtCore.QRect(140, 130, 271, 31))
        self.vs_fname_entry.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(255, 255, 255);")
        self.vs_fname_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.vs_fname_entry.setObjectName("vs_fname_entry")

        # Label
        self.label_22 = QtWidgets.QLabel(self.visitor)
        self.label_22.setGeometry(QtCore.QRect(30, 140, 111, 21))
        self.label_22.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_22.setObjectName("label_22")
        self.label_6 = QtWidgets.QLabel(self.visitor)
        self.label_6.setGeometry(QtCore.QRect(420, 140, 111, 21))
        self.label_6.setStyleSheet("\n"
                                   "font: 12pt \"Reem Kufi\";")
        self.label_6.setObjectName("label_6")

        # last name entry - Visitor
        self.vs_lname_entry = QtWidgets.QLineEdit(self.visitor)
        self.vs_lname_entry.setGeometry(QtCore.QRect(530, 130, 271, 31))
        self.vs_lname_entry.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(255, 255, 255);")
        self.vs_lname_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.vs_lname_entry.setObjectName("vs_lname_entry")

        # label
        self.label_3 = QtWidgets.QLabel(self.visitor)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 55, 21))
        self.label_3.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.visitor)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 101, 21))
        self.label_4.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.visitor)
        self.label_7.setGeometry(QtCore.QRect(420, 190, 121, 21))
        self.label_7.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.visitor)
        self.label_9.setGeometry(QtCore.QRect(420, 240, 111, 21))
        self.label_9.setStyleSheet("font: 12pt \"Reem Kufi\";")
        self.label_9.setObjectName("label_9")

        # Email entry - visitor
        self.vs_email_entry = QtWidgets.QLineEdit(self.visitor)
        self.vs_email_entry.setGeometry(QtCore.QRect(140, 180, 271, 31))
        self.vs_email_entry.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(255, 255, 255);")
        self.vs_email_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.vs_email_entry.setObjectName("vs_email_entry")

        # Contact entry - Visitor
        self.vs_contact_entry = QtWidgets.QLineEdit(self.visitor)
        self.vs_contact_entry.setGeometry(QtCore.QRect(530, 180, 271, 31))
        self.vs_contact_entry.setStyleSheet("border-radius: 15px;\n"
                                            "background-color: rgb(255, 255, 255);")
        self.vs_contact_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.vs_contact_entry.setObjectName("vs_contact_entry")

        # Affliation entry - Visitor
        self.vs_affliation_entry = QtWidgets.QLineEdit(self.visitor)
        self.vs_affliation_entry.setGeometry(QtCore.QRect(140, 230, 271, 31))
        self.vs_affliation_entry.setStyleSheet("border-radius: 15px;\n"
                                               "background-color: rgb(255, 255, 255);")
        self.vs_affliation_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.vs_affliation_entry.setObjectName("vs_affliation_entry")

        # Reason entry - Visitor
        self.vs_reason = QtWidgets.QLineEdit(self.visitor)
        self.vs_reason.setGeometry(QtCore.QRect(530, 230, 271, 31))
        self.vs_reason.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(255, 255, 255);")
        self.vs_reason.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.vs_reason.setObjectName("vs_reason")

        # label
        self.label_8 = QtWidgets.QLabel(self.visitor)
        self.label_8.setGeometry(QtCore.QRect(270, 480, 341, 21))
        self.label_8.setStyleSheet("\n"
                                   "font: 8pt \"Reem Kufi\";")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.visitor)
        self.label_10.setGeometry(QtCore.QRect(270, 500, 371, 16))
        self.label_10.setStyleSheet("\n"
                                    "font: 8pt \"Reem Kufi\";")
        self.label_10.setObjectName("label_10")

        # Submit button - visitor
        self.submit_button_vs = QtWidgets.QPushButton(self.visitor)
        self.submit_button_vs.setGeometry(QtCore.QRect(630, 480, 151, 41))
        self.submit_button_vs.setStyleSheet("QPushButton{\n"
                                            "    border-radius: 15px;\n"
                                            "}\n"
                                            "QPushButton:enabled {\n"
                                            "   background-color: #eac4a3;\n"
                                            "   color: #fffff;\n"
                                            "font: 10pt \"Reem Kufi\";\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "   background-color: #CE8865;\n"
                                            "   color: #000000;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover:!pressed {\n"
                                            "   background-color: #eac4a3;\n"
                                            "   color: #ffffff;\n"
                                            "    border-radius: 23px;\n"
                                            "border-radius: 15px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:disabled {\n"
                                            "   background-color: #eac4a3;\n"
                                            "   color: #000000;\n"
                                            "}\n"
                                            "")
        self.submit_button_vs.setObjectName("submit_button_vs")
        self.submit_button_vs.clicked.connect(self.register_visitor)

        # Additional Options
        self.label_10.raise_()
        self.line_5.raise_()
        self.label.raise_()
        self.vs_fname_entry.raise_()
        self.label_22.raise_()
        self.label_6.raise_()
        self.vs_lname_entry.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.vs_email_entry.raise_()
        self.vs_contact_entry.raise_()
        self.vs_affliation_entry.raise_()

        self.vs_reason.raise_()
        self.label_8.raise_()
        self.submit_button_vs.raise_()
        self.register_folder.addTab(self.visitor, "")
        self.history_label = QtWidgets.QLabel(registration_frame)
        self.history_label.setGeometry(QtCore.QRect(50, 50, 211, 51))
        self.history_label.setStyleSheet("font: 27pt \"Reem Kufi\";\n"
                                         "background-color: rgb(234, 196, 163);")
        self.history_label.setObjectName("history_label")
        self.privacy_button = QtWidgets.QPushButton(registration_frame)
        self.privacy_button.setGeometry(QtCore.QRect(720, 60, 81, 30))
        self.privacy_button.setStyleSheet("QPushButton {\n"
                                          "   border-radius: 15px;\n"
                                          "    font: 12pt \"Reem Kufi\";\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:enabled {\n"
                                          "   background-color: #EAC4A3;\n"
                                          "   color: black;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "   background-color: #EAC4A3;\n"
                                          "   color: #black;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover:!pressed {\n"
                                          "   background-color: #EAC4A3;\n"
                                          "   color: white;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:disabled {\n"
                                          "   background-color: #EAC4A3;\n"
                                          "   color: black;\n"
                                          "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/LOGS_panel.ui-20231123T155216Z-001/print (1).png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.privacy_button.setIcon(icon)
        self.privacy_button.setObjectName("privacy_button")
        self.terms_button = QtWidgets.QPushButton(registration_frame)
        self.terms_button.setGeometry(QtCore.QRect(800, 60, 71, 30))
        self.terms_button.setStyleSheet("QPushButton {\n"
                                        "   border-radius: 15px;\n"
                                        "    font: 12pt \"Reem Kufi\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:enabled {\n"
                                        "   background-color: #EAC4A3;\n"
                                        "   color: black;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "   background-color: #EAC4A3;\n"
                                        "   color: #black;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover:!pressed {\n"
                                        "   background-color: #EAC4A3;\n"
                                        "   color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:disabled {\n"
                                        "   background-color: #EAC4A3;\n"
                                        "   color: black;\n"
                                        "}")
        self.terms_button.setIcon(icon)
        self.terms_button.setObjectName("terms_button")
        self.pri_button_2 = QtWidgets.QPushButton(registration_frame)
        self.pri_button_2.setGeometry(QtCore.QRect(650, 60, 81, 30))
        self.pri_button_2.setStyleSheet("QPushButton {\n"
                                        "   border-radius: 15px;\n"
                                        "    font: 12pt \"Reem Kufi\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:enabled {\n"
                                        "   background-color: #EAC4A3;\n"
                                        "   color: black;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "   background-color: #EAC4A3;\n"
                                        "   color: #black;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover:!pressed {\n"
                                        "   background-color: #EAC4A3;\n"
                                        "   color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:disabled {\n"
                                        "   background-color: #EAC4A3;\n"
                                        "   color: black;\n"
                                        "}")
        self.pri_button_2.setIcon(icon)
        self.pri_button_2.setObjectName("pri_button_2")
        self.history_label.raise_()
        self.privacy_button.raise_()
        self.terms_button.raise_()
        self.register_folder.raise_()
        self.pri_button_2.raise_()
        self.pri_button_2.clicked.connect(self.reset)

        self.retranslateUi(registration_frame)
        self.register_folder.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(registration_frame)

    def retranslateUi(self, registration_frame):
        _translate = QtCore.QCoreApplication.translate
        registration_frame.setWindowTitle(_translate("registration_frame", "Frame"))
        self.label_18.setText(_translate("registration_frame", " Register as a Homeowner!"))
        self.label_19.setText(_translate("registration_frame", "First Name:"))
        self.label_13.setText(_translate("registration_frame", "Last Name:"))
        self.label_15.setText(_translate("registration_frame", "Email: "))
        self.label_12.setText(_translate("registration_frame", "Block #:"))
        self.label_11.setText(_translate("registration_frame", "Contact #:"))
        self.label_21.setText(_translate("registration_frame", "Lot #:"))
        self.label_14.setText(_translate("registration_frame", "Password:"))
        self.label_16.setText(_translate("registration_frame", "Confirm Password:"))
        self.label_20.setText(
            _translate("registration_frame", "By clicking submit, you agree to TAPSILOG SYSTEM v2.0\'s"))
        self.label_17.setText(
            _translate("registration_frame", "Terms of Service and accept that you\'ve read our Privacy Policy."))
        self.submit_button_hm.setText(_translate("registration_frame", "SUBMIT"))
        self.register_folder.setTabText(self.register_folder.indexOf(self.homeowner),
                                        _translate("registration_frame", "HOMEOWNER"))
        self.label.setText(
            _translate("registration_frame", " Register a Visitor! Fill with the visitor\'s information. "))
        self.label_22.setText(_translate("registration_frame", "First Name:"))
        self.label_6.setText(_translate("registration_frame", "Last Name:"))
        self.label_3.setText(_translate("registration_frame", "Email: "))
        self.label_4.setText(_translate("registration_frame", "Affiliation:"))
        self.label_7.setText(_translate("registration_frame", "Contact #:"))
        self.label_9.setText(_translate("registration_frame", "Reason:"))

        self.label_8.setText(
            _translate("registration_frame", "By clicking submit, you agree to TAPSILOG SYSTEM v2.0\'s"))
        self.label_10.setText(
            _translate("registration_frame", "Terms of Service and accept that you\'ve read our Privacy Policy."))
        self.submit_button_vs.setText(_translate("registration_frame", "SUBMIT"))
        self.register_folder.setTabText(self.register_folder.indexOf(self.visitor),
                                        _translate("registration_frame", "VISITOR"))
        self.history_label.setText(_translate("registration_frame", "REGISTER"))
        self.privacy_button.setText(_translate("registration_frame", "Privacy"))
        self.terms_button.setText(_translate("registration_frame", "Terms"))
        self.pri_button_2.setText(_translate("registration_frame", "Reset"))



