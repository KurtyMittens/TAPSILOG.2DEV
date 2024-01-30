from PyQt5 import QtCore, QtGui, QtWidgets
from database import tapsi_sql
import datetime
import cv2


class Ui_main_scanner(QtWidgets.QDialog):
    def __init__(self, parent, worker, id):
        super().__init__(parent)
        self.worker = worker
        self.id = id
        self.database_connection = tapsi_sql.TapsilogSql()
        self.setupUi(self)

    def closeEvent(self, a0):
        try:
            self.worker.stop()
            self.label_3.setText("REMARKS: FALSE")
            self.add()
            a0.accept()
        except:
            self.worker.stop()
            self.label_3.setText("REMARKS: FALSE")
            a0.accept()

    def remark_checker(self):
        try:
            date = datetime.datetime.now()
            date_of_entry = date.strftime('%m-%d-%Y')
            if date_of_entry != self.worker.get_val()[2]:
                return "EXPIRED"
            else:
                return "TRUE"
        except:
            return "FALSE"

    def add(self):
        if self.database_connection.is_exit_nan(self.worker.get_val()[0]):
            self.database_connection.add_homeowner_logout(self.database_connection.is_exit_nan(self.worker.get_val()[0]))
        elif self.database_connection.is_exit_nan(self.worker.get_val()[0]) is None:
            self.database_connection.add_homeowner_login(self.id, self.worker.get_val())

    def image_update(self, image):
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))
        self.label_3.setText(f"REMARKS: {self.remark_checker()}")

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
        self.label.setGeometry(QtCore.QRect(210, 10, 311, 41))
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
        self.label_3.setGeometry(QtCore.QRect(210, 540, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(main_scanner)
        QtCore.QMetaObject.connectSlotsByName(main_scanner)

    def retranslateUi(self, main_scanner):
        _translate = QtCore.QCoreApplication.translate
        main_scanner.setWindowTitle(_translate("main_scanner", "QR SCANNER"))
        self.label.setText(_translate("main_scanner", "ALIGN YOUR QR CODE IN THE FRAME"))
        self.label_3.setText(_translate("main_scanner", "REMARKS:   <TRUE, FALSE, EXPIRED>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_scanner = QtWidgets.QWidget()
    ui = Ui_main_scanner()
    ui.setupUi(main_scanner)
    main_scanner.show()
    sys.exit(app.exec_())
