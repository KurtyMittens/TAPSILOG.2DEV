from PyQt5 import QtCore, QtGui, QtWidgets
from database import tapsi_sql
from tapsilog_frames import TapsiMAP, logFrame, register_frame, generate_frame, update_frame, qr_scanner, WORKERS, huck_cam
import functools


class Ui_MainWindow(QtWidgets.QMainWindow):
    """
    The main interface of TAPSILog Systems, were admins can manage the register and homeowners and visitors, generate qr codes, manage logs,
    and reinforced by our own facial recognition HUCK!

    Special thanks to BDSM to creating these Project:
    Designs by yseult
    Database development by leam
    programming and design logic by kynamittens
    encryption through database by xeno
    mobile development by draco
    """
    def __init__(self, name, account_logged):
        super().__init__()
        self.database_connection = tapsi_sql.TapsilogSql()
        self.account_id = account_logged
        self.workerCAm = WORKERS.WorkerCAMERA(self)
        self.workerHuck = WORKERS.WorkerHUCK(self)
        self.name = name
        self.setupUi(self)
        self.show()

    def closeEvent(self, a0):
        self.reply = QtWidgets.QMessageBox.question(self, "Are you sure?", "You are about to exit the TAPSILog System, You want to continue?")
        if self.reply == QtWidgets.QMessageBox.Yes:
            self.database_connection.add_admin_logout(self.account_id)
            a0.accept()
        else:
            a0.ignore()

    def open_scanner(self):
        self.workerCAm.start()
        self.workerCAm.img_update.connect(self.scanner.image_update)
        self.scanner.show()

    def open_huck(self):
        self.workerHuck.start()
        self.workerHuck.img_update.connect(self.huck.image_update)
        self.huck.show()
        self.huck.timer.start(5000)

    def open_generator(self):
        self.generate.show()


    def loading_recent_logs(self):
        self.reset = tapsi_sql.TapsilogSql()
        list = self.reset.show_homeowner_logs()
        self.RECENT_LOGS.setRowCount(len(list))
        self.RECENT_LOGS.repaint()
        for i, j in enumerate(list):
            for index, item in enumerate(j):
                if index == 1:
                    self.RECENT_LOGS.setItem(i, 0, QtWidgets.QTableWidgetItem(item))
                if index == 2:
                    self.RECENT_LOGS.setItem(i, 3, QtWidgets.QTableWidgetItem(item))
                if index == 3:
                    self.RECENT_LOGS.setItem(i, 1, QtWidgets.QTableWidgetItem(item))
                if index == 4:
                    self.RECENT_LOGS.setItem(i, 2, QtWidgets.QTableWidgetItem(item))
                else:
                    continue




    def close_all_frames(self):
        """Refreshes frames by hiding all of them"""
        self.REGISTER_changeable_panel.hide()
        self.HOME_changeable_panel.hide()
        self.LOGS_changeable_panel.hide()
        self.UPDATE_changeable_panel.hide()

    def show_home(self):
        self.close_all_frames()
        self.HOME_changeable_panel.show()

    def show_logs(self):
        self.close_all_frames()
        self.LOGS_changeable_panel.show()

    def show_register(self):
        self.close_all_frames()
        self.REGISTER_changeable_panel.show()

    def show_updates(self):
        self.close_all_frames()
        self.UPDATE_changeable_panel.show()



    def setupUi(self, MainWindow):
        """Designing the main window"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1275, 718)
        MainWindow.setMaximumSize(QtCore.QSize(1275, 820))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(-2)
        MainWindow.setStyleSheet("#MainWindow{background-color: rgb(213, 145, 110);}")

        # The central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        """FRAMES"""
        # Default Home Widget
        self.HOME_changeable_panel = QtWidgets.QWidget(self.centralwidget)
        self.HOME_changeable_panel.setEnabled(True)
        self.HOME_changeable_panel.setGeometry(QtCore.QRect(360, 0, 921, 721))
        self.HOME_changeable_panel.setStyleSheet("background-color: rgb(234, 196, 163);")
        self.HOME_changeable_panel.setObjectName("HOME_changeable_panel")

        # Logs Frame
        self.LOGS_changeable_panel = logFrame.Ui_log_frame(self.centralwidget)
        self.LOGS_changeable_panel.setGeometry(QtCore.QRect(360, 0, 921, 721))
        self.LOGS_changeable_panel.hide()

        # Register Frame
        self.REGISTER_changeable_panel = register_frame.Ui_registration_frame(self.centralwidget, self.account_id)
        self.REGISTER_changeable_panel.setGeometry(QtCore.QRect(360, 0, 921, 721))
        self.REGISTER_changeable_panel.hide()

        # Update Frame
        self.UPDATE_changeable_panel = update_frame.Ui_UPDATE_changeable_panel(self.centralwidget)
        self.UPDATE_changeable_panel.setGeometry(QtCore.QRect(360, 0, 921, 721))
        self.UPDATE_changeable_panel.hide()

        # Home_Labels
        self.GREETING_MSG = QtWidgets.QGroupBox(self.HOME_changeable_panel)
        self.GREETING_MSG.setGeometry(QtCore.QRect(50, 40, 641, 111))
        self.GREETING_MSG.setStyleSheet("font: 63 15pt \"OCR A Extended\";")
        self.GREETING_MSG.setFlat(False)
        self.GREETING_MSG.setObjectName("GREETING_MSG")
        self.TAPSI_LABEL = QtWidgets.QLabel(self.GREETING_MSG)
        self.TAPSI_LABEL.setGeometry(QtCore.QRect(100, 30, 461, 61))
        self.TAPSI_LABEL.setStyleSheet("font: 25pt \"Reem Kufi\";\n")
        self.TAPSI_LABEL.setObjectName("TAPSI_LABEL")

        # Recent Logs table
        self.RECENT_LOGS = QtWidgets.QTableWidget(self.HOME_changeable_panel)
        self.RECENT_LOGS.setGeometry(QtCore.QRect(30, 360, 511, 331))
        self.RECENT_LOGS.setToolTip("")
        self.RECENT_LOGS.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 20px;")
        self.RECENT_LOGS.setFrameShape(QtWidgets.QFrame.Box)
        self.RECENT_LOGS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RECENT_LOGS.setObjectName("RECENT_LOGS")
        self.RECENT_LOGS.setColumnCount(4)
        self.RECENT_LOGS.setHorizontalHeaderLabels(['Name', 'Time IN', 'Time OUT', 'Date'])
        self.RECENT_LOGS.setShowGrid(False)
        self.RECENT_LOGS.setColumnWidth(0, 100)
        self.RECENT_LOGS.setColumnWidth(1, 100)
        self.RECENT_LOGS.setColumnWidth(2, 100)
        self.RECENT_LOGS.setColumnWidth(3, 160)


        # Total Number of Registered Homeowners
        self.TOTAL_REG_HO = QtWidgets.QGroupBox(self.HOME_changeable_panel)
        self.TOTAL_REG_HO.setGeometry(QtCore.QRect(570, 190, 321, 61))
        self.TOTAL_REG_HO.setStyleSheet("font: 9pt \"OCR A Extended\";\n"
                                        "")
        self.TOTAL_REG_HO.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.TOTAL_REG_HO.setFlat(False)
        self.TOTAL_REG_HO.setObjectName("TOTAL_REG_HO")
        self.total_reg_ho_label = QtWidgets.QLabel(self.TOTAL_REG_HO)
        self.total_reg_ho_label.setGeometry(QtCore.QRect(150, 30, 81, 20))
        self.total_reg_ho_label.setObjectName("total_reg_ho_label")

        # Qr Scanner Button
        self.QR_SCANNER_BTN = QtWidgets.QPushButton(self.HOME_changeable_panel)
        self.QR_SCANNER_BTN.setGeometry(QtCore.QRect(70, 190, 100, 100))
        self.QR_SCANNER_BTN.setStyleSheet("QPushButton{\n"
                                          "    border-radius: 50px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:enabled {\n"
                                          "   background-color: #eac4a3;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "   background-color: #CE8865;\n"
                                          "\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover:!pressed {\n"
                                          "   background-color: #d5916e;\n"
                                          "    border-radius: 50px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:disabled {\n"
                                          "   background-color: #eac4a3;\n"
                                          "}")
        self.QR_SCANNER_BTN.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/qr-scan (1).png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.QR_SCANNER_BTN.setIcon(icon1)
        self.QR_SCANNER_BTN.setIconSize(QtCore.QSize(200, 200))
        self.QR_SCANNER_BTN.setObjectName("QR_SCANNER_BTN")
        self.QR_SCANNER_BTN.clicked.connect(self.open_scanner)

        # Total Number of Registered Visitors
        self.TOTAL_REG_VIS = QtWidgets.QGroupBox(self.HOME_changeable_panel)
        self.TOTAL_REG_VIS.setGeometry(QtCore.QRect(570, 280, 321, 61))
        self.TOTAL_REG_VIS.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.TOTAL_REG_VIS.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.TOTAL_REG_VIS.setObjectName("TOTAL_REG_VIS")
        self.total_reg_vis_label = QtWidgets.QLabel(self.TOTAL_REG_VIS)
        self.total_reg_vis_label.setGeometry(QtCore.QRect(150, 30, 81, 20))
        self.total_reg_vis_label.setObjectName("total_reg_vis_label")

        # HUCK activation button
        self.HUCK_BTN = QtWidgets.QPushButton(self.HOME_changeable_panel)
        self.HUCK_BTN.setGeometry(QtCore.QRect(230, 190, 100, 100))
        self.HUCK_BTN.setStyleSheet("QPushButton{\n"
                                    "    border-radius: 50px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:enabled {\n"
                                    "   background-color: #eac4a3;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "   background-color: #CE8865;\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover:!pressed {\n"
                                    "   background-color: #d5916e;\n"
                                    "    border-radius: 50px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:disabled {\n"
                                    "   background-color: #eac4a3;\n"
                                    "}")
        self.HUCK_BTN.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/huck.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HUCK_BTN.setIcon(icon2)
        self.HUCK_BTN.setIconSize(QtCore.QSize(100, 100))
        self.HUCK_BTN.setObjectName("HUCK_BTN")
        self.HUCK_BTN.clicked.connect(self.open_huck)

        # QR Generator Button
        self.QR_SCANNER_BTN_2 = QtWidgets.QPushButton(self.HOME_changeable_panel)
        self.QR_SCANNER_BTN_2.setGeometry(QtCore.QRect(390, 190, 100, 100))
        self.QR_SCANNER_BTN_2.setStyleSheet("QPushButton{\n"
                                            "    border-radius: 50px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:enabled {\n"
                                            "   background-color: #eac4a3;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "   background-color: #CE8865;\n"
                                            "\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover:!pressed {\n"
                                            "   background-color: #d5916e;\n"
                                            "    border-radius: 50px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:disabled {\n"
                                            "   background-color: #eac4a3;\n"
                                            "}")
        self.QR_SCANNER_BTN_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/qr2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QR_SCANNER_BTN_2.setIcon(icon3)
        self.QR_SCANNER_BTN_2.setIconSize(QtCore.QSize(200, 200))
        self.QR_SCANNER_BTN_2.setObjectName("QR_SCANNER_BTN_2")
        self.QR_SCANNER_BTN_2.clicked.connect(self.open_generator)

        # Label
        self.loglabel = QtWidgets.QLabel(self.HOME_changeable_panel)
        self.loglabel.setGeometry(QtCore.QRect(30, 320, 141, 31))
        self.loglabel.setStyleSheet("font: 10pt \"Reem Kufi\";")
        self.loglabel.setObjectName("loglabel")
        self.mapWidget = QtWidgets.QWidget(self.HOME_changeable_panel)
        self.mapWidget.setGeometry(QtCore.QRect(560, 360, 331, 331))
        self.mapWidget.setToolTipDuration(-1)
        self.mapWidget.setStyleSheet("background-color: rgb(236, 160, 122);\n"
                                  "border-radius: 20px;")

        # Map Displayer
        self.mapWidget.setObjectName("widget")
        self.mapLayout = QtWidgets.QVBoxLayout(self.mapWidget)
        self.mapLayout.setContentsMargins(0, 0, 0, 0)
        self.mapLayout.setObjectName("mapLayout")
        self.displayMap = TapsiMAP.JavaScriptMaps(self.mapLayout)
        self.TAPSI_NAME = QtWidgets.QLabel(self.centralwidget)
        self.TAPSI_NAME.setGeometry(QtCore.QRect(30, 210, 301, 41))
        self.TAPSI_NAME.setStyleSheet("background-color: rgb(213, 145, 110);\n"
                                      "\n"
                                      "font: 9pt \"OCR A Extended\";\n"
                                      "\n"
                                      "color: rgb(255, 255, 255);\n"
                                      " align: \"center\";")
        self.TAPSI_NAME.setObjectName("TAPSI_NAME")

        # Logo
        self.TAPSI_LOGO = QtWidgets.QLabel(self.centralwidget)
        self.TAPSI_LOGO.setGeometry(QtCore.QRect(100, 40, 161, 161))
        self.TAPSI_LOGO.setStyleSheet("background-color: rgb(234, 196, 163);\n"
                                      "border-radius: 40px;\n"
                                      "")
        self.TAPSI_LOGO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TAPSI_LOGO.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TAPSI_LOGO.setText("")
        self.TAPSI_LOGO.setPixmap(QtGui.QPixmap("assets/logo_smol.png"))
        self.TAPSI_LOGO.setAlignment(QtCore.Qt.AlignCenter)
        self.TAPSI_LOGO.setObjectName("TAPSI_LOGO")

        # Browser/Search button
        self.ENTER_BROWSER_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.ENTER_BROWSER_BTN.setGeometry(QtCore.QRect(270, 280, 41, 31))
        self.ENTER_BROWSER_BTN.setStyleSheet("QPushButton {\n"
                                             "   border-radius: 15px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:enabled {\n"
                                             "   background-color: #D5916E;\n"
                                             "   color: white;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "   background-color: #CE8865;\n"
                                             "   color: #ffffff;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover:!pressed {\n"
                                             "   background-color: #EAC4A3;\n"
                                             "   color: #008080;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:disabled {\n"
                                             "   background-color: #D5916E;\n"
                                             "   color: #ffffff;\n"
                                             "}")
        self.ENTER_BROWSER_BTN.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/search (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ENTER_BROWSER_BTN.setIcon(icon4)
        self.ENTER_BROWSER_BTN.setIconSize(QtCore.QSize(20, 20))
        self.ENTER_BROWSER_BTN.setObjectName("ENTER_BROWSER_BTN")

        # Vertical Widgets
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 330, 241, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Home Button
        self.HOME_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.HOME_BTN.setStyleSheet("QPushButton{\n"
                                    "    border-radius: 15px;\n"
                                    "}\n"
                                    "QPushButton:enabled {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #fffff;\n"
                                    "font: 13pt \"Reem Kufi\";\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #ffaa7f;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover:!pressed {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #ffffff;\n"
                                    "    border-radius: 23px;\n"
                                    "border-radius: 15px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:disabled {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #000000;\n"
                                    "}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HOME_BTN.setIcon(icon5)
        self.HOME_BTN.setIconSize(QtCore.QSize(20, 20))
        self.HOME_BTN.setObjectName("HOME_BTN")
        self.verticalLayout.addWidget(self.HOME_BTN)
        self.HOME_BTN.clicked.connect(self.show_home)

        # Update Button
        self.UPDATE_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.UPDATE_BTN.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 15px;\n"
                                      "}\n"
                                      "QPushButton:enabled {\n"
                                      "   background-color: #d5916e;\n"
                                      "   color: #fffff;\n"
                                      "font: 13pt \"Reem Kufi\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "   background-color: #d5916e;\n"
                                      "   color: #ffaa7f;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover:!pressed {\n"
                                      "   background-color: #d5916e;\n"
                                      "   color: #ffffff;\n"
                                      "    border-radius: 23px;\n"
                                      "border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:disabled {\n"
                                      "   background-color: #d5916e;\n"
                                      "   color: #000000;\n"
                                      "}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/refresh.png"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.UPDATE_BTN.setIcon(icon6)
        self.UPDATE_BTN.setIconSize(QtCore.QSize(20, 20))
        self.UPDATE_BTN.setObjectName("UPDATE_BTN")
        self.verticalLayout.addWidget(self.UPDATE_BTN)
        self.UPDATE_BTN.clicked.connect(self.show_updates)

        # Logs Button
        self.LOGS_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.LOGS_BTN.setStyleSheet("QPushButton{\n"
                                    "    border-radius: 15px;\n"
                                    "}\n"
                                    "QPushButton:enabled {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #fffff;\n"
                                    "font: 13pt \"Reem Kufi\";\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #ffaa7f;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover:!pressed {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #ffffff;\n"
                                    "    border-radius: 23px;\n"
                                    "border-radius: 15px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:disabled {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #000000;\n"
                                    "}")

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assets/book-open-cover.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOGS_BTN.setIcon(icon7)
        self.LOGS_BTN.setIconSize(QtCore.QSize(20, 20))
        self.LOGS_BTN.setObjectName("LOGS_BTN")
        self.verticalLayout.addWidget(self.LOGS_BTN)
        self.LOGS_BTN.clicked.connect(self.show_logs)

        # Register Button
        self.REG_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.REG_BTN.setStyleSheet("QPushButton{\n"
                                   "    border-radius: 15px;\n"
                                   "}\n"
                                   "QPushButton:enabled {\n"
                                   "   background-color: #d5916e;\n"
                                   "   color: #fffff;\n"
                                   "font: 13pt \"Reem Kufi\";\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "   background-color: #d5916e;\n"
                                   "   color: #ffaa7f;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover:!pressed {\n"
                                   "   background-color: #d5916e;\n"
                                   "   color: #ffffff;\n"
                                   "    border-radius: 23px;\n"
                                   "border-radius: 15px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:disabled {\n"
                                   "   background-color: #d5916e;\n"
                                   "   color: #000000;\n"
                                   "}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("assets/user_add.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.REG_BTN.setIcon(icon8)
        self.REG_BTN.setIconSize(QtCore.QSize(20, 20))
        self.REG_BTN.setObjectName("REG_BTN")
        self.verticalLayout.addWidget(self.REG_BTN)
        self.REG_BTN.clicked.connect(self.show_register)

        # Register Button
        self.GEN_QR_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.GEN_QR_BTN.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 15px;\n"
                                      "}\n"
                                      "QPushButton:enabled {\n"
                                      "   background-color: #d5916e;\n"
                                      "   color: #fffff;\n"
                                      "font: 13pt \"Reem Kufi\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "   background-color: #d5916e;\n"
                                      "   color: #ffaa7f;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover:!pressed {\n"
                                      "   background-color: #d5916e;\n"
                                      "   color: #ffffff;\n"
                                      "    border-radius: 23px;\n"
                                      "border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:disabled {\n"
                                      "   background-color: #d5916e;\n"
                                      "   color: #000000;\n"
                                      "}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("assets/settings.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.GEN_QR_BTN.setIcon(icon9)
        self.GEN_QR_BTN.setIconSize(QtCore.QSize(20, 20))
        self.GEN_QR_BTN.setObjectName("GEN_QR_BTN")
        self.verticalLayout.addWidget(self.GEN_QR_BTN)


        # Exit Button
        self.EXIT_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.EXIT_BTN.setStyleSheet("QPushButton{\n"
                                    "    border-radius: 15px;\n"
                                    "}\n"
                                    "QPushButton:enabled {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #fffff;\n"
                                    "font: 13pt \"Reem Kufi\";\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #ffaa7f;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover:!pressed {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #ffffff;\n"
                                    "    border-radius: 23px;\n"
                                    "border-radius: 15px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:disabled {\n"
                                    "   background-color: #d5916e;\n"
                                    "   color: #000000;\n"
                                    "}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("assets/exit.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.EXIT_BTN.setIcon(icon10)
        self.EXIT_BTN.setIconSize(QtCore.QSize(20, 20))
        self.EXIT_BTN.setObjectName("EXIT_BTN")
        self.verticalLayout.addWidget(self.EXIT_BTN)
        self.EXIT_BTN.clicked.connect(self.close)

        # Search Entry
        self.BROWSER = QtWidgets.QTextEdit(self.centralwidget)
        self.BROWSER.setGeometry(QtCore.QRect(40, 280, 221, 31))
        self.BROWSER.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 15px;\n"
                                   "font: 9pt \"Gill Sans MT\";")
        self.BROWSER.setFrameShape(QtWidgets.QFrame.Panel)
        self.BROWSER.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BROWSER.setDocumentTitle("")
        self.BROWSER.setObjectName("BROWSER")
        MainWindow.setCentralWidget(self.centralwidget)

        # Generate Dialog
        self.generate = generate_frame.Ui_generate_qr_panel(self.centralwidget)

        # Scanner Dialog
        self.scanner = qr_scanner.Ui_main_scanner(self.centralwidget, self.workerCAm, self.account_id)

        # Huck Dialog
        self.huck = huck_cam.Ui_main_scanner(self.centralwidget, self.workerHuck)

        # Timer for Updating RecentLogs
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.loading_recent_logs)
        self.timer.start(1000)



        # Re translating Window
        self.retranslateUi(MainWindow, self.name)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, name):
        """HTML Rich Text"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TAPSILog"))
        self.GREETING_MSG.setTitle(_translate("MainWindow", f"Welcome Admin {name}!"))
        self.TAPSI_LABEL.setText(_translate("MainWindow", "T.A.P.S.I.Log System V.2.0"))
        self.TOTAL_REG_HO.setTitle(_translate("MainWindow", "Total Registered Homeowners"))
        self.total_reg_ho_label.setText(_translate("MainWindow", f"{len(self.database_connection.show_homeowners())}"))
        self.QR_SCANNER_BTN.setToolTip(_translate("MainWindow", "QR Scanner"))
        self.TOTAL_REG_VIS.setTitle(_translate("MainWindow", "Total Registered Visitors"))
        self.total_reg_vis_label.setText(_translate("MainWindow", f"{len(self.database_connection.show_visitor())}"))
        self.HUCK_BTN.setToolTip(_translate("MainWindow", "HUCK AI Scanner"))
        self.QR_SCANNER_BTN_2.setToolTip(_translate("MainWindow", "QR Generator"))
        self.loglabel.setText(_translate("MainWindow", "Recent Log History"))
        self.TAPSI_NAME.setText(
            _translate("MainWindow", "  Total Activity Processed through <br /> a Strictly Implemented Log System"))
        self.HOME_BTN.setText(_translate("MainWindow", "   HOME"))
        self.UPDATE_BTN.setText(_translate("MainWindow", "   UPDATE"))
        self.LOGS_BTN.setText(_translate("MainWindow", "   LOGS"))
        self.REG_BTN.setText(_translate("MainWindow", "   REGISTER"))
        self.GEN_QR_BTN.setText(_translate("MainWindow", "   SETTINGS"))
        self.EXIT_BTN.setText(_translate("MainWindow", "   QUIT"))
        self.BROWSER.setPlaceholderText(_translate("MainWindow", "   Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow("Kurt", 1)
    sys.exit(app.exec_())
