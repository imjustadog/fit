# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\fit\fitMainWindow.ui'
#
# Created: Mon Oct 23 14:03:59 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 609)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 10, 21, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_times = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_times.setGeometry(QtCore.QRect(480, 10, 51, 20))
        self.lineEdit_times.setObjectName(_fromUtf8("lineEdit_times"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 10, 41, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.dateEdit_date = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_date.setGeometry(QtCore.QRect(650, 10, 110, 22))
        self.dateEdit_date.setObjectName(_fromUtf8("dateEdit_date"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 10, 41, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_upload = QtGui.QPushButton(self.centralwidget)
        self.pushButton_upload.setGeometry(QtCore.QRect(600, 540, 75, 23))
        self.pushButton_upload.setObjectName(_fromUtf8("pushButton_upload"))
        self.pushButton_clear = QtGui.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(680, 540, 75, 23))
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 721, 491))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.comboBox_name = QtGui.QComboBox(self.centralwidget)
        self.comboBox_name.setGeometry(QtCore.QRect(80, 10, 81, 22))
        self.comboBox_name.setEditable(True)
        self.comboBox_name.setObjectName(_fromUtf8("comboBox_name"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_New = QtGui.QAction(MainWindow)
        self.action_New.setObjectName(_fromUtf8("action_New"))
        self.action_statistics = QtGui.QAction(MainWindow)
        self.action_statistics.setObjectName(_fromUtf8("action_statistics"))
        self.menu.addAction(self.action_New)
        self.menu.addAction(self.action_statistics)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "客户信息管理系统", None))
        self.label.setText(_translate("MainWindow", "姓名", None))
        self.label_2.setText(_translate("MainWindow", "第", None))
        self.label_3.setText(_translate("MainWindow", "次训练", None))
        self.label_4.setText(_translate("MainWindow", "日期", None))
        self.pushButton_upload.setText(_translate("MainWindow", "提交", None))
        self.pushButton_clear.setText(_translate("MainWindow", "清空", None))
        self.menu.setTitle(_translate("MainWindow", "选项", None))
        self.action_New.setText(_translate("MainWindow", "新建", None))
        self.action_statistics.setText(_translate("MainWindow", "统计", None))

