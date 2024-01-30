from PyQt5 import QtCore, QtGui, QtWidgets
from qr_generator import generator


class Ui_generate_qr_panel(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.generate = generator.GenerateQR()

    def qr_tohome(self):
        self.generate.generate()
        self.close()

    def setupUi(self, generate_qr_panel):
        generate_qr_panel.setObjectName("generate_qr_panel")
        generate_qr_panel.resize(636, 455)
        generate_qr_panel.setStyleSheet("background-color: rgb(213, 145, 110);\n"" ")
        self.label = QtWidgets.QLabel(generate_qr_panel)
        self.label.setGeometry(QtCore.QRect(140, 60, 361, 31))
        self.label.setStyleSheet("font: 20pt \"Reem Kufi\";")
        self.label.setObjectName("label")
        self.HUCK_BTN = QtWidgets.QPushButton(generate_qr_panel)
        self.HUCK_BTN.setGeometry(QtCore.QRect(70, 180, 100, 100))
        self.HUCK_BTN.setToolTip("")
        self.HUCK_BTN.setStyleSheet("QPushButton{\n"
                                    "    border-radius: 50px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:enabled {\n"
                                    "   background-color: #d5916e;\n"
                                    "}\n"
                                    "\n"       
                                    "QPushButton:pressed {\n"
                                    "   background-color: #CE8865;\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover:!pressed {\n"
                                    "   background-color: #eac4a3;\n"
                                    "    border-radius: 50px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:disabled {\n"
                                    "   background-color: #d5916e;\n"
                                    "}")
        self.HUCK_BTN.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/envelope.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HUCK_BTN.setIcon(icon)
        self.HUCK_BTN.setIconSize(QtCore.QSize(130, 130))
        self.HUCK_BTN.setObjectName("HUCK_BTN")
        self.HUCK_BTN.clicked.connect(self.qr_tohome)
        self.label_2 = QtWidgets.QLabel(generate_qr_panel)
        self.label_2.setGeometry(QtCore.QRect(70, 290, 111, 31))
        self.label_2.setStyleSheet("font: 13pt \"Reem Kufi\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(generate_qr_panel)
        self.label_3.setGeometry(QtCore.QRect(40, 320, 171, 31))
        self.label_3.setStyleSheet("font: 13pt \"Reem Kufi\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.HUCK_BTN_2 = QtWidgets.QPushButton(generate_qr_panel)
        self.HUCK_BTN_2.setGeometry(QtCore.QRect(460, 180, 100, 100))
        self.HUCK_BTN_2.setToolTip("")
        self.HUCK_BTN_2.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 50px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:enabled {\n"
                                      "   background-color: #d5916e;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "   background-color: #CE8865;\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover:!pressed {\n"
                                      "   background-color: #eac4a3;\n"
                                      "    border-radius: 50px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:disabled {\n"
                                      "   background-color: #d5916e;\n"
                                      "}")
        self.HUCK_BTN_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/gift-card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HUCK_BTN_2.setIcon(icon1)
        self.HUCK_BTN_2.setIconSize(QtCore.QSize(130, 130))
        self.HUCK_BTN_2.setObjectName("HUCK_BTN_2")
        self.HUCK_BTN_3 = QtWidgets.QPushButton(generate_qr_panel)
        self.HUCK_BTN_3.setGeometry(QtCore.QRect(270, 180, 100, 100))
        self.HUCK_BTN_3.setToolTip("")
        self.HUCK_BTN_3.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 50px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:enabled {\n"
                                      "   background-color: #d5916e;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "   background-color: #CE8865;\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover:!pressed {\n"
                                      "   background-color: #eac4a3;\n"
                                      "    border-radius: 50px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:disabled {\n"
                                      "   background-color: #d5916e;\n"
                                      "}")
        self.HUCK_BTN_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/paper-plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HUCK_BTN_3.setIcon(icon2)
        self.HUCK_BTN_3.setIconSize(QtCore.QSize(130, 130))
        self.HUCK_BTN_3.setObjectName("HUCK_BTN_3")
        self.label_4 = QtWidgets.QLabel(generate_qr_panel)
        self.label_4.setGeometry(QtCore.QRect(270, 290, 111, 31))
        self.label_4.setStyleSheet("font: 13pt \"Reem Kufi\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(generate_qr_panel)
        self.label_5.setGeometry(QtCore.QRect(280, 320, 91, 31))
        self.label_5.setStyleSheet("font: 13pt \"Reem Kufi\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(generate_qr_panel)
        self.label_6.setGeometry(QtCore.QRect(460, 290, 111, 31))
        self.label_6.setStyleSheet("font: 13pt \"Reem Kufi\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(generate_qr_panel)
        self.label_7.setGeometry(QtCore.QRect(440, 320, 151, 31))
        self.label_7.setStyleSheet("font: 13pt \"Reem Kufi\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.progressBar = QtWidgets.QProgressBar(generate_qr_panel)
        self.progressBar.setGeometry(QtCore.QRect(120, 400, 411, 23))
        self.progressBar.setStyleSheet(" QProgressBar {\n"
                                       "        border: 2px solid rgba(33, 37, 43, 180);\n"
                                       "        border-radius: 5px;\n"
                                       "        text-align: center;\n"
                                       "        background-color: rgba(33, 37, 43, 180);\n"
                                       "        color: black;\n"
                                       "    }\n"
                                       "    QProgressBar::chunk {\n"
                                       "       \n"
                                       "    background-color: rgb(234, 196, 163);\n"
                                       "    }")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(generate_qr_panel)
        QtCore.QMetaObject.connectSlotsByName(generate_qr_panel)

    def retranslateUi(self, generate_qr_panel):
        _translate = QtCore.QCoreApplication.translate
        generate_qr_panel.setWindowTitle(_translate("generate_qr_panel", "GENERATE QR"))
        self.label.setText(_translate("generate_qr_panel", "GENERATE QR CODES"))
        self.label_2.setText(_translate("generate_qr_panel", "Send QR to"))
        self.label_3.setText(_translate("generate_qr_panel", "all Home Owners"))
        self.label_4.setText(_translate("generate_qr_panel", "Send QR to"))
        self.label_5.setText(_translate("generate_qr_panel", "a Visitor"))
        self.label_6.setText(_translate("generate_qr_panel", "Send QR to"))
        self.label_7.setText(_translate("generate_qr_panel", "a Selected User"))

