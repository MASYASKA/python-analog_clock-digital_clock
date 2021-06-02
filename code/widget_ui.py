# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1080, 720)
        MainWidget.setStyleSheet("QWidget{\n"
"    background-color: rgb(12, 95, 112);\n"
"}")
        self.button_back = QtWidgets.QPushButton(MainWidget)
        self.button_back.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_back.setFont(font)
        self.button_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_back.setStyleSheet("QPushButton{\n"
"    background-color: rgb(11, 159, 182);\n"
"}")
        self.button_back.setObjectName("button_back")
        self.button_close = QtWidgets.QPushButton(MainWidget)
        self.button_close.setGeometry(QtCore.QRect(1040, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_close.setFont(font)
        self.button_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_close.setStyleSheet("QPushButton{\n"
"    background-color: rgb(11, 159, 182);\n"
"}")
        self.button_close.setObjectName("button_close")
        self.button_roll = QtWidgets.QPushButton(MainWidget)
        self.button_roll.setGeometry(QtCore.QRect(1000, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_roll.setFont(font)
        self.button_roll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_roll.setStyleSheet("QPushButton{\n"
"    background-color: rgb(11, 159, 182);\n"
"}")
        self.button_roll.setObjectName("button_roll")

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Form"))
        self.button_back.setText(_translate("MainWidget", "<<"))
        self.button_close.setText(_translate("MainWidget", "×"))
        self.button_roll.setText(_translate("MainWidget", "–"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWidget = QtWidgets.QWidget()
    ui = Ui_MainWidget()
    ui.setupUi(MainWidget)
    MainWidget.show()
    sys.exit(app.exec_())
