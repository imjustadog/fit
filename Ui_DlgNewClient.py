# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\fit\DlgNewClient.ui'
#
# Created: Wed Oct 04 18:06:24 2017
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

class Ui_DialogNewClient(QtGui.QDialog):
    def setupUi(self, DialogNewClient):
        DialogNewClient.setObjectName(_fromUtf8("DialogNewClient"))
        DialogNewClient.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(DialogNewClient)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit_name = QtGui.QLineEdit(DialogNewClient)
        self.lineEdit_name.setGeometry(QtCore.QRect(70, 40, 113, 20))
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.label = QtGui.QLabel(DialogNewClient)
        self.label.setGeometry(QtCore.QRect(30, 40, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(DialogNewClient)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogNewClient.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogNewClient.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNewClient)

    def retranslateUi(self, DialogNewClient):
        DialogNewClient.setWindowTitle(_translate("DialogNewClient", "添加客户", None))
        self.label.setText(_translate("DialogNewClient", "姓名", None))

