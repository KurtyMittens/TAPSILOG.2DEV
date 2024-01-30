from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from database import ICE
from huck import thisIsHuck


class WorkerCAMERA (QtCore.QThread):
    img_update = QtCore.pyqtSignal(QtGui.QImage)
    val = []

    def run(self):
        self.ThreadActive = True
        Cap = cv2.VideoCapture(0)
        self.qr_value = cv2.QRCodeDetector()
        while self.ThreadActive:
            ret, frame = Cap.read()
            self.data, one, _ = self.qr_value.detectAndDecode(frame)
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flipped = cv2.flip(Image, 1)
                convertQT = QtGui.QImage(flipped.data, flipped.shape[1], flipped.shape[0], QtGui.QImage.Format_RGB888)
                pic = convertQT.scaled(680, 480, QtCore.Qt.KeepAspectRatio)
                self.img_update.emit(pic)
                if self.data:
                    self.stop()
                    self.val = (self.data.split(","))
                    break

    def get_val(self):
        self.decoded = []
        for i in self.val:
            self.eyes = ICE.ICE()
            a = self.eyes.decode(i)
            self.decoded.append(a)
        return self.decoded

    def stop(self):
        self.ThreadActive = False
        self.quit()


class WorkerHUCK (QtCore.QThread):
    img_update = QtCore.pyqtSignal(QtGui.QImage)

    def run(self):
        self.recognition = thisIsHuck.HUCK()
        self.process_this_frame = 29
        self.ThreadActive = True
        Cap = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Cap.read()
            if ret:
                self.img = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                self.process_this_frame1 = self.process_this_frame + 1
                Image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                flipped = cv2.flip(Image, 1)
                convertQT = QtGui.QImage(flipped.data, flipped.shape[1], flipped.shape[0], QtGui.QImage.Format_RGB888)
                pic = convertQT.scaled(680, 480, QtCore.Qt.KeepAspectRatio)
                self.img_update.emit(pic)


    def recognize(self):
        if self.process_this_frame1 % 30 == 0:
            return self.recognition.huck_predicts(self.img, model_path='tapsilog_frames/huck.clf')


    def stop(self):
        self.ThreadActive = False
        self.quit()



