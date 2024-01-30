from PyQt5 import QtCore, QtGui, QtWidgets
from huck import thisIsHuck


class Ui_main_scanner(QtWidgets.QDialog):
    def __init__(self, parent, worker):
        super().__init__(parent)
        self.worker = worker
        self.setupUi(self)
        self.huck = thisIsHuck.HUCK()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get)

    def closeEvent(self, a0):
        self.worker.stop()
        a0.accept()

    def get(self):
        if self.worker.recognize():
            if len(self.worker.recognize()) == 0:
                self.label_3.setText(f"IN-FRAME: NONE")
            else:
                self.label_3.setText(f"IN-FRAME: {self.worker.recognize()[0][0]}")
    def image_update(self, image):
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))


    def setupUi(self, main_scanner):
        main_scanner.setObjectName("main_scanner")
        main_scanner.resize(701, 580)
        main_scanner.setMinimumSize(QtCore.QSize(701, 580))
        main_scanner.setMaximumSize(QtCore.QSize(701, 580))
        self.scanner_frame = QtWidgets.QFrame(main_scanner)
        self.scanner_frame.setGeometry(QtCore.QRect(0, 0, 701, 581))
        self.scanner_frame.setStyleSheet("\n"
"background-color: rgb(234, 196, 163);")
        self.scanner_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scanner_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scanner_frame.setObjectName("scanner_frame")
        self.label = QtWidgets.QLabel(self.scanner_frame)
        self.label.setGeometry(QtCore.QRect(250, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scanner_frame)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 640, 480))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scanner_frame)
        self.label_3.setGeometry(QtCore.QRect(180, 540, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(main_scanner)
        QtCore.QMetaObject.connectSlotsByName(main_scanner)

    def retranslateUi(self, main_scanner):
        _translate = QtCore.QCoreApplication.translate
        main_scanner.setWindowTitle(_translate("main_scanner", "HUCK"))
        self.label.setText(_translate("main_scanner", "HUCK FACE RECOGNITION"))
        self.label_3.setText(_translate("main_scanner", "IN-FRAME:   <name>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_scanner = QtWidgets.QWidget()
    ui = Ui_main_scanner()
    ui.setupUi(main_scanner)
    main_scanner.show()
    sys.exit(app.exec_())
