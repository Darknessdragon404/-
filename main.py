import io
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
import sqlite3
tem = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Кофе</string>
  </property>
  <widget class="QTableWidget" name="table">
   <property name="geometry">
    <rect>
     <x>5</x>
     <y>11</y>
     <width>391</width>
     <height>281</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Table(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(tem)
        uic.loadUi(f, self)
        self.con = sqlite3.connect(r"C:\Users\Professional\Desktop\coffee.db")
        query = "SELECT * FROM coffee"
        res = self.con.cursor().execute(query).fetchall()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.table.setRowCount(0)
        for i, row in enumerate(res):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Table()
    ex.show()
    sys.exit(app.exec())
