# to enter the desinger, in the terminal enter: designer
# to convert to python document
# pyuic5 -x weigh_scale_ui.ui -o weigh_scale_ui.py


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Weigh Scale UI")
        MainWindow.resize(856, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.weigh_input = QtWidgets.QLCDNumber(self.centralwidget)
        self.weigh_input.setGeometry(QtCore.QRect(380, 30, 391, 81))
        self.weigh_input.setObjectName("weigh_input")
        self.qr_code = QtWidgets.QLabel(self.centralwidget)
        self.qr_code.setGeometry(QtCore.QRect(220, 240, 551, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.qr_code.setFont(font)
        self.qr_code.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qr_code.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qr_code.setObjectName("qr_code")
        self.current_weight_label = QtWidgets.QLabel(self.centralwidget)
        self.current_weight_label.setGeometry(QtCore.QRect(20, 20, 331, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.current_weight_label.setFont(font)
        self.current_weight_label.setObjectName("current_weight_label")
        self.bins_tipped = QtWidgets.QLCDNumber(self.centralwidget)
        self.bins_tipped.setGeometry(QtCore.QRect(20, 480, 161, 61))
        self.bins_tipped.setObjectName("bins_tipped")
        self.bins_tipped_label = QtWidgets.QLabel(self.centralwidget)
        self.bins_tipped_label.setGeometry(QtCore.QRect(30, 420, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bins_tipped_label.setFont(font)
        self.bins_tipped_label.setObjectName("bins_tipped_label")
        self.total_weight_label = QtWidgets.QLabel(self.centralwidget)
        self.total_weight_label.setGeometry(QtCore.QRect(220, 420, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.total_weight_label.setFont(font)
        self.total_weight_label.setObjectName("total_weight_label")
        self.total_weight = QtWidgets.QLCDNumber(self.centralwidget)
        self.total_weight.setGeometry(QtCore.QRect(220, 480, 161, 61))
        self.total_weight.setObjectName("total_weight")
        self.min_weight_label = QtWidgets.QLabel(self.centralwidget)
        self.min_weight_label.setGeometry(QtCore.QRect(440, 420, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.min_weight_label.setFont(font)
        self.min_weight_label.setObjectName("min_weight_label")
        self.min_weight = QtWidgets.QLCDNumber(self.centralwidget)
        self.min_weight.setGeometry(QtCore.QRect(430, 480, 161, 61))
        self.min_weight.setObjectName("min_weight")
        self.max_weight_label = QtWidgets.QLabel(self.centralwidget)
        self.max_weight_label.setGeometry(QtCore.QRect(640, 420, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.max_weight_label.setFont(font)
        self.max_weight_label.setObjectName("max_weight_label")
        self.max_weight = QtWidgets.QLCDNumber(self.centralwidget)
        self.max_weight.setGeometry(QtCore.QRect(640, 480, 161, 61))
        self.max_weight.setObjectName("max_weight")
        self.current_weight_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.current_weight_bar.setGeometry(QtCore.QRect(380, 130, 391, 81))
        self.current_weight_bar.setMinimum(200)
        self.current_weight_bar.setMaximum(600)
        self.current_weight_bar.setProperty("value", 350)
        self.current_weight_bar.setTextVisible(False)
        self.current_weight_bar.setObjectName("current_weight_bar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.qr_code.setText(_translate("MainWindow", "QR CODE"))
        self.current_weight_label.setText(_translate("MainWindow", "Current Weight"))
        self.bins_tipped_label.setText(_translate("MainWindow", "Bins Tipped"))
        self.total_weight_label.setText(_translate("MainWindow", "Total Weight"))
        self.min_weight_label.setText(_translate("MainWindow", "Min Weight"))
        self.max_weight_label.setText(_translate("MainWindow", "Max Weight"))
        self.current_weight_bar.setFormat(_translate("MainWindow", "%p%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())