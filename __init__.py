# -*- coding: utf-8 -*-
from Ui_fitMainWindow import Ui_MainWindow
from Ui_DlgNewClient import Ui_DialogNewClient
import MySQLdb

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Code_DialogNewClient(Ui_DialogNewClient):
    signal_getNewparam = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Ui_DialogNewClient, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.signal_emiter)


    def signal_emiter(self):
        dictNew = {}
        dictNew['name'] = self.lineEdit_name.text()
        self.signal_getNewparam.emit(dictNew)


class Code_MainWindow(Ui_MainWindow):
    db = []

    def __init__(self, parent=None):
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionNew.triggered.connect(self.openNewDlg)

        try:
            self.HeaderList = []
            self.HeaderList.append(u"动作名称")
            self.HeaderList.append(u"重量")
            self.HeaderList.append(u"组数")
            self.HeaderList.append(u"重复次数")
            self.HeaderList.append(u"组间休息")
            self.HeaderList.append(u"总时间")

            self.tableWidget.setRowCount(10)
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(self.HeaderList)

            for x in range(6):
                headItem = self.tableWidget.horizontalHeaderItem(x)
                headItem.setBackgroundColor(QColor(0, 0, 200))
                headItem.setTextColor(QColor(0, 0, 200))

            for i in range(10):
                combo = QComboBox()
                combo.setEditable(True)
                self.tableWidget.setCellWidget(i, 0, combo)
                combo.editTextChanged.connect(self.editChanged)

            self.tableWidget.setColumnWidth(0, 350)
            self.tableWidget.setColumnWidth(1, 40)
            self.tableWidget.setColumnWidth(2, 40)
            self.tableWidget.setColumnWidth(3, 60)
            self.tableWidget.setColumnWidth(4, 60)
            self.tableWidget.setColumnWidth(5, 50)

        except Exception as e:
            print e

    def openNewDlg(self):
        ui_New = Code_DialogNewClient(self)
        ui_New.show()
        ui_New.signal_getNewparam.connect(self.getDictNew)

    def editChanged(self, text):
        sender = self.sender()
        sender.setEditable(False)
        sender.clear()

        sql = "SELECT `CLIENT_NAME` FROM `client` WHERE `CLIENT_NAME` LIKE '%s%%' ORDER BY CLIENT_NAME" % text
        try:
            self.cursor.execute(sql)
            self.db.commit()
            res = self.cursor.fetchall()

        except:
            print 'error'
            self.db.rollback()

        string_list = [text]
        for x in res:
            string_list.append(x[0])
        sender.addItems(string_list)
        sender.setCurrentIndex(0)
        sender.setEditable(True)


    @pyqtSlot(dict)
    def getDictNew(self, newParam):
        name = str(newParam['name'])
        sql = "INSERT INTO CLIENT(CLIENT_NAME) VALUES ('%s')" % name
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print 'error'
            self.db.rollback()


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    app = QApplication(sys.argv)
    ui_main = Code_MainWindow()
    ui_main.db = MySQLdb.connect("127.0.0.1", "root", "zsty8059", "fit", charset='utf8')
    ui_main.cursor = ui_main.db.cursor()
    ui_main.show()
sys.exit(app.exec_())
ui_main.db.close()