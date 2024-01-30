from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_log_frame(QtWidgets.QFrame):
    def __init__(self, frame):
        super().__init__(frame)
        self.setupUi(self)

    def setupUi(self, log_frame):
        log_frame.setObjectName("log_frame")
        log_frame.resize(921, 721)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(log_frame.sizePolicy().hasHeightForWidth())
        log_frame.setSizePolicy(sizePolicy)
        log_frame.setMinimumSize(QtCore.QSize(921, 721))
        log_frame.setMaximumSize(QtCore.QSize(921, 721))
        log_frame.setStyleSheet("background-color: rgb(234, 196, 163);")
        self.history_label = QtWidgets.QLabel(log_frame)
        self.history_label.setGeometry(QtCore.QRect(50, 50, 311, 51))
        self.history_label.setStyleSheet("font: 27pt \"Reem Kufi\";")
        self.history_label.setObjectName("history_label")
        self.BROWSER = QtWidgets.QTextEdit(log_frame)
        self.BROWSER.setGeometry(QtCore.QRect(450, 50, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BROWSER.setFont(font)
        self.BROWSER.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 15px;\n"
                                   "font: 12pt \"Gill Sans MT\";")
        self.BROWSER.setInputMethodHints(QtCore.Qt.ImhNone)
        self.BROWSER.setFrameShape(QtWidgets.QFrame.Box)
        self.BROWSER.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BROWSER.setDocumentTitle("")
        self.BROWSER.setUndoRedoEnabled(False)
        self.BROWSER.setAcceptRichText(False)
        self.BROWSER.setObjectName("BROWSER")
        self.ENTER_BROWSER_BTN = QtWidgets.QPushButton(log_frame)
        self.ENTER_BROWSER_BTN.setGeometry(QtCore.QRect(810, 50, 41, 41))
        self.ENTER_BROWSER_BTN.setStyleSheet("QPushButton {\n"
                                             "   border-radius: 20px;\n"
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
        self.ENTER_BROWSER_BTN.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/search (2).png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ENTER_BROWSER_BTN.setIcon(icon)
        self.ENTER_BROWSER_BTN.setIconSize(QtCore.QSize(25, 25))
        self.ENTER_BROWSER_BTN.setObjectName("ENTER_BROWSER_BTN")
        self.pushButton_2 = QtWidgets.QPushButton(log_frame)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 120, 151, 28))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/print.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.log_history_table = QtWidgets.QTableView(log_frame)
        self.log_history_table.setGeometry(QtCore.QRect(40, 160, 841, 541))
        self.log_history_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 20px;")
        self.log_history_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.log_history_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.log_history_table.setObjectName("log_history_table")

        self.retranslateUi(log_frame)
        QtCore.QMetaObject.connectSlotsByName(log_frame)

    def retranslateUi(self, log_frame):
        _translate = QtCore.QCoreApplication.translate
        log_frame.setWindowTitle(_translate("log_frame", "Frame"))
        self.history_label.setText(_translate("log_frame", "LOG HISTORY"))
        self.BROWSER.setPlaceholderText(_translate("log_frame", "   Search"))
        self.pushButton_2.setText(_translate("log_frame", "   Print History"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    log_frame = QtWidgets.QFrame()
    ui = Ui_log_frame()
    ui.setupUi(log_frame)
    log_frame.show()
    sys.exit(app.exec_())
