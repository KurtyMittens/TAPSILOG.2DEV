from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UPDATE_changeable_panel(QtWidgets.QFrame):
    def __init__(self, frame):
        super().__init__(frame)
        self.setupUi(self)

    def setupUi(self, UPDATE_changeable_panel):
        UPDATE_changeable_panel.setObjectName("UPDATE_changeable_panel")
        UPDATE_changeable_panel.resize(921, 721)
        UPDATE_changeable_panel.setStyleSheet("background-color: rgb(234, 196, 163);\n"
                                              "font: 8pt \"Reem Kufi\";")
        self.update_label = QtWidgets.QLabel(UPDATE_changeable_panel)
        self.update_label.setGeometry(QtCore.QRect(30, 40, 461, 31))
        self.update_label.setStyleSheet("font: 16pt \"Reem Kufi\";")
        self.update_label.setObjectName("update_label")
        self.decor_line = QtWidgets.QFrame(UPDATE_changeable_panel)
        self.decor_line.setGeometry(QtCore.QRect(0, 46, 921, 20))
        self.decor_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.decor_line.setLineWidth(1)
        self.decor_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.decor_line.setObjectName("decor_line")
        self.update_table = QtWidgets.QTableWidget(UPDATE_changeable_panel)
        self.update_table.setGeometry(QtCore.QRect(60, 170, 781, 271))
        self.update_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 10pt \"Reem Kufi\";")
        self.update_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.update_table.setObjectName("update_table")
        self.update_table.setColumnCount(5)
        self.update_table.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.update_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.update_table.setHorizontalHeaderItem(4, item)
        self.update_table.verticalHeader().setCascadingSectionResizes(False)
        self.update_browser = QtWidgets.QTextEdit(UPDATE_changeable_panel)
        self.update_browser.setGeometry(QtCore.QRect(30, 110, 256, 31))
        self.update_browser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "font: 8pt \"Reem Kufi\";\n"
                                          "border-radius: 15px;")
        self.update_browser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.update_browser.setObjectName("update_browser")
        self.search_btn_update = QtWidgets.QPushButton(UPDATE_changeable_panel)
        self.search_btn_update.setGeometry(QtCore.QRect(290, 110, 41, 31))
        self.search_btn_update.setStyleSheet("QPushButton {\n"
                                             "   border-radius: 15px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:enabled {\n"
                                             "   background-color: #EAC4A3;\n"
                                             "   color: white;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "   background-color: #CE8865;\n"
                                             "   color: #ffffff;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover:!pressed {\n"
                                             "   background-color: #D5916E;\n"
                                             "   color: #008080;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:disabled {\n"
                                             "   background-color: #EAC4A3;\n"
                                             "   color: #ffffff;\n"
                                             "}")
        self.search_btn_update.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/search (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn_update.setIcon(icon)
        self.search_btn_update.setIconSize(QtCore.QSize(20, 20))
        self.search_btn_update.setObjectName("search_btn_update")
        self.gridLayoutWidget = QtWidgets.QWidget(UPDATE_changeable_panel)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 440, 751, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.update_block_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.update_block_label.setStyleSheet("font: 10pt \"Reem Kufi\";")
        self.update_block_label.setObjectName("update_block_label")
        self.gridLayout.addWidget(self.update_block_label, 0, 2, 1, 1)
        self.update_HO_ID_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.update_HO_ID_label.setStyleSheet("font: 10pt \"Reem Kufi\";")
        self.update_HO_ID_label.setObjectName("update_HO_ID_label")
        self.gridLayout.addWidget(self.update_HO_ID_label, 0, 0, 1, 1)
        self.HO_ID_update = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.HO_ID_update.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;\n"
                                        "font: 10pt \"Reem Kufi\";")
        self.HO_ID_update.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.HO_ID_update.setObjectName("HO_ID_update")
        self.gridLayout.addWidget(self.HO_ID_update, 0, 1, 1, 1)
        self.block_update = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.block_update.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;\n"
                                        "font: 10pt \"Reem Kufi\";")
        self.block_update.setObjectName("block_update")
        self.gridLayout.addWidget(self.block_update, 0, 3, 1, 1)
        self.update_fname_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.update_fname_label.setStyleSheet("font: 10pt \"Reem Kufi\";")
        self.update_fname_label.setObjectName("update_fname_label")
        self.gridLayout.addWidget(self.update_fname_label, 1, 0, 1, 1)
        self.fname_update = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.fname_update.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;\n"
                                        "font: 10pt \"Reem Kufi\";")
        self.fname_update.setObjectName("fname_update")
        self.gridLayout.addWidget(self.fname_update, 1, 1, 1, 1)
        self.lot_update = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lot_update.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "font: 10pt \"Reem Kufi\";")
        self.lot_update.setObjectName("lot_update")
        self.gridLayout.addWidget(self.lot_update, 1, 3, 1, 1)
        self.update_lot_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.update_lot_label.setStyleSheet("font: 10pt \"Reem Kufi\";")
        self.update_lot_label.setObjectName("update_lot_label")
        self.gridLayout.addWidget(self.update_lot_label, 1, 2, 1, 1)
        self.update_lname_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.update_lname_label.setStyleSheet("font: 10pt \"Reem Kufi\";")
        self.update_lname_label.setObjectName("update_lname_label")
        self.gridLayout.addWidget(self.update_lname_label, 2, 0, 1, 1)
        self.lname_update = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lname_update.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;\n"
                                        "font: 10pt \"Reem Kufi\";")
        self.lname_update.setObjectName("lname_update")
        self.gridLayout.addWidget(self.lname_update, 2, 1, 1, 1)
        self.contact_update = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.contact_update.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 10px;\n"
                                          "font: 10pt \"Reem Kufi\";")
        self.contact_update.setObjectName("contact_update")
        self.gridLayout.addWidget(self.contact_update, 2, 3, 1, 1)
        self.update_contact_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.update_contact_label.setStyleSheet("font: 10pt \"Reem Kufi\";")
        self.update_contact_label.setObjectName("update_contact_label")
        self.gridLayout.addWidget(self.update_contact_label, 2, 2, 1, 1)
        self.update_save_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.update_save_btn.setStyleSheet("QPushButton{\n"
                                           "    border-radius: 5px;\n"
                                           "}\n"
                                           "QPushButton:enabled {\n"
                                           "   background-color: #d5916e;\n"
                                           "   color: #fffff;\n"
                                           "font: 10pt \"Reem Kufi\";\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "   background-color: #c88868;\n"
                                           "   color: #000000;\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover:!pressed {\n"
                                           "   background-color: #d5916e;\n"
                                           "   color: #ffffff;\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:disabled {\n"
                                           "   background-color: #d5916e;\n"
                                           "   color: #000000;\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "")
        self.update_save_btn.setObjectName("update_save_btn")
        self.gridLayout.addWidget(self.update_save_btn, 3, 3, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 1)
        self.gridLayout.setColumnMinimumWidth(3, 1)
        self.decor_line.raise_()
        self.update_label.raise_()
        self.update_table.raise_()
        self.update_browser.raise_()
        self.search_btn_update.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(UPDATE_changeable_panel)
        QtCore.QMetaObject.connectSlotsByName(UPDATE_changeable_panel)

    def retranslateUi(self, UPDATE_changeable_panel):
        _translate = QtCore.QCoreApplication.translate
        UPDATE_changeable_panel.setWindowTitle(_translate("UPDATE_changeable_panel", "UPDATE"))
        self.update_label.setText(_translate("UPDATE_changeable_panel", " UPDATE HOMEOWNER DATABASE"))
        self.update_table.setSortingEnabled(False)
        item = self.update_table.verticalHeaderItem(0)
        item.setText(_translate("UPDATE_changeable_panel", "1"))
        item = self.update_table.verticalHeaderItem(1)
        item.setText(_translate("UPDATE_changeable_panel", "2"))
        item = self.update_table.verticalHeaderItem(2)
        item.setText(_translate("UPDATE_changeable_panel", "3"))
        item = self.update_table.verticalHeaderItem(3)
        item.setText(_translate("UPDATE_changeable_panel", "4"))
        item = self.update_table.verticalHeaderItem(4)
        item.setText(_translate("UPDATE_changeable_panel", "5"))
        item = self.update_table.verticalHeaderItem(5)
        item.setText(_translate("UPDATE_changeable_panel", "6"))
        item = self.update_table.horizontalHeaderItem(0)
        item.setText(_translate("UPDATE_changeable_panel", "First Name"))
        item = self.update_table.horizontalHeaderItem(1)
        item.setText(_translate("UPDATE_changeable_panel", "Last Name"))
        item = self.update_table.horizontalHeaderItem(2)
        item.setText(_translate("UPDATE_changeable_panel", "Block no."))
        item = self.update_table.horizontalHeaderItem(3)
        item.setText(_translate("UPDATE_changeable_panel", "Lot no."))
        item = self.update_table.horizontalHeaderItem(4)
        item.setText(_translate("UPDATE_changeable_panel", "Contact"))
        self.update_browser.setHtml(_translate("UPDATE_changeable_panel",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Reem Kufi\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:8px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.update_browser.setPlaceholderText(_translate("UPDATE_changeable_panel", "   Search"))
        self.update_block_label.setText(_translate("UPDATE_changeable_panel", "Block no.:"))
        self.update_HO_ID_label.setText(_translate("UPDATE_changeable_panel", "Homeowner ID:"))
        self.update_fname_label.setText(_translate("UPDATE_changeable_panel", "First Name:"))
        self.update_lot_label.setText(_translate("UPDATE_changeable_panel", "Lot no.:"))
        self.update_lname_label.setText(_translate("UPDATE_changeable_panel", "Last Name:"))
        self.update_contact_label.setText(_translate("UPDATE_changeable_panel", "Contact no.:"))
        self.update_save_btn.setText(_translate("UPDATE_changeable_panel", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    UPDATE_changeable_panel = QtWidgets.QWidget()
    ui = Ui_UPDATE_changeable_panel()
    ui.setupUi(UPDATE_changeable_panel)
    UPDATE_changeable_panel.show()
    sys.exit(app.exec_())
