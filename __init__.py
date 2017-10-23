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
        self.dateEdit_date.setDate(QDate.currentDate())
        self.action_New.triggered.connect(self.openNewDlg)
        self.comboBox_name.editTextChanged.connect(self.editName)
        self.pushButton_upload.clicked.connect(self.upLoad)
        self.pushButton_clear.clicked.connect(self.clearAll)

        try:
            self.HeaderList = []
            self.HeaderList.append(u"动作名称")
            self.HeaderList.append(u"重量")
            self.HeaderList.append(u"组数")
            self.HeaderList.append(u"重复次数")
            self.HeaderList.append(u"组间休息")
            self.HeaderList.append(u"总时间")

            self.tableWidget.setRowCount(15)
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(self.HeaderList)

            for x in range(6):
                headItem = self.tableWidget.horizontalHeaderItem(x)
                headItem.setBackgroundColor(QColor(0, 0, 200))
                headItem.setTextColor(QColor(0, 0, 200))

            for i in range(15):
                combo = QComboBox()
                combo.setEditable(True)
                self.tableWidget.setCellWidget(i, 0, combo)
                combo.editTextChanged.connect(self.editChanged)

            self.tableWidget.setColumnWidth(0, 468)
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

    def upLoad(self):
        name = self.comboBox_name.currentText()
        for i in range(15):
            event = self.tableWidget.cellWidget(i, 0)
            if event:
                event = event.currentText()
            else:
                event = ''
            if event != '':

                weight = self.tableWidget.item(i, 1)
                if weight:
                    weight = int(weight.text())
                else:
                    weight = 0

                group = self.tableWidget.item(i, 2)
                if group:
                    group = int(group.text())
                else:
                    group = 0

                times = self.tableWidget.item(i, 3)
                if times:
                    times = int(times.text())
                else:
                    times = 0

                breaks = self.tableWidget.item(i, 4)
                if breaks:
                    breaks = int(breaks.text())
                else:
                    breaks = 0

                total = self.tableWidget.item(i, 5)
                if total:
                    total = int(total.text())
                else:
                    total = 0

                sql = "INSERT INTO `DATA`(`CLIENT_NAME`,`EVENT_NAME`,`WEIGHT`,`GROUP`,`TIMES`,`BREAK`,`TOTALTIME`) VALUES ('%s','%s',%d, %d,%d,%d,%d)" % (name,event,weight,group,times,breaks,total)

                try:
                    self.cursor.execute(sql)
                    self.db.commit()
                    res = self.cursor.fetchall()
                except:
                    print 'error'
                    self.db.rollback()

            else:
                break

    def clearAll(self):
        self.comboBox_name.clear()
        self.lineEdit_times.clear()
        self.tableWidget.clearContents()
        for i in range(10):
            combo = QComboBox()
            combo.setEditable(True)
            self.tableWidget.setCellWidget(i, 0, combo)
            combo.editTextChanged.connect(self.editChanged)


    def editName(self, text):
        self.comboBox_name.setEditable(False)
        self.comboBox_name.clear()

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
        self.comboBox_name.addItems(string_list)
        self.comboBox_name.setCurrentIndex(0)
        self.comboBox_name.setEditable(True)
        cursor = self.comboBox_name.cursor()
        cursor.movePosition(QTextCursor.End)
        self.comboBox_name.setCursor()


    def editChanged(self, text):
        sender = self.sender()
        sender.setEditable(False)
        sender.clear()

        sql = "SELECT `EVENT_NAME` FROM `event` WHERE `EVENT_NAME` LIKE '%s%%' ORDER BY EVENT_NAME" % text
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