from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_support_frame(QtWidgets.QDialog):
    def __init__(self, main):
        super().__init__(main)
        self.setupUi(self)
        self.show()

    def setupUi(self, support_frame):
        support_frame.setObjectName("support_frame")
        support_frame.resize(462, 547)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(support_frame.sizePolicy().hasHeightForWidth())
        support_frame.setSizePolicy(sizePolicy)
        support_frame.setMinimumSize(QtCore.QSize(462, 547))
        support_frame.setMaximumSize(QtCore.QSize(462, 547))
        support_frame.setStyleSheet("#support_frame{\n"
"    background-color: rgb(234, 196, 163);\n"
"}")
        self.label = QtWidgets.QLabel(support_frame)
        self.label.setGeometry(QtCore.QRect(100, 170, 281, 31))
        self.label.setStyleSheet("font: 20pt \"Reem Kufi\";")
        self.label.setObjectName("label")
        self.TAPSI_LOGO = QtWidgets.QLabel(support_frame)
        self.TAPSI_LOGO.setGeometry(QtCore.QRect(150, 10, 161, 161))
        self.TAPSI_LOGO.setStyleSheet("image: url(:/pics/assets/logo.png);\n"
"background-color: rgb(234, 196, 163);\n"
"border-radius: 40px;\n"
"")
        self.TAPSI_LOGO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TAPSI_LOGO.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TAPSI_LOGO.setText("")
        self.TAPSI_LOGO.setPixmap(QtGui.QPixmap("../assets/logo_smol.png"))
        self.TAPSI_LOGO.setAlignment(QtCore.Qt.AlignCenter)
        self.TAPSI_LOGO.setObjectName("TAPSI_LOGO")
        self.pushButton = QtWidgets.QPushButton(support_frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 240, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(214, 146, 111);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(support_frame)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 310, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(214, 146, 111);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(support_frame)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 380, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(214, 146, 111);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(support_frame)
        self.label_2.setGeometry(QtCore.QRect(120, 530, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(support_frame)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 450, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(214, 146, 111);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.TAPSI_LOGO.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_2.raise_()
        self.pushButton_4.raise_()

        self.retranslateUi(support_frame)
        QtCore.QMetaObject.connectSlotsByName(support_frame)

    def retranslateUi(self, support_frame):
        _translate = QtCore.QCoreApplication.translate
        support_frame.setWindowTitle(_translate("support_frame", "Admin Support"))
        self.label.setText(_translate("support_frame", "ADMIN SUPPORT"))
        self.pushButton.setText(_translate("support_frame", "FORGOT MY PASSWORD"))
        self.pushButton_2.setText(_translate("support_frame", "HUCK is Failing"))
        self.pushButton_3.setText(_translate("support_frame", "Edit my Account"))
        self.label_2.setText(_translate("support_frame", "Created by BDSM, All rights reserved 2023"))
        self.pushButton_4.setText(_translate("support_frame", "RUN TROUBLESHOOTING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    support_frame = QtWidgets.QFrame()
    ui = Ui_support_frame(1)
    ui.setupUi(support_frame)
    support_frame.show()
    sys.exit(app.exec_())
