# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surveyMem.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_surveyMem(object):
    def setupUi(self, surveyMem):
        surveyMem.setObjectName(_fromUtf8("surveyMem"))
        surveyMem.resize(711, 546)
        self.widget_2 = QtGui.QWidget(surveyMem)
        self.widget_2.setGeometry(QtCore.QRect(60, 80, 591, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.checkBox = QtGui.QCheckBox(self.widget_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 221, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.widget_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 50, 221, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.widget_2)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 80, 361, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.ok_btn = QtGui.QPushButton(surveyMem)
        self.ok_btn.setGeometry(QtCore.QRect(600, 500, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.label = QtGui.QLabel(surveyMem)
        self.label.setGeometry(QtCore.QRect(70, 40, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(surveyMem)
        self.textEdit.setGeometry(QtCore.QRect(50, 400, 611, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(surveyMem)
        self.label_2.setGeometry(QtCore.QRect(50, 380, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget_3 = QtGui.QWidget(surveyMem)
        self.widget_3.setGeometry(QtCore.QRect(60, 310, 591, 51))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label_3 = QtGui.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spinBox = QtGui.QSpinBox(self.widget_3)
        self.spinBox.setGeometry(QtCore.QRect(260, 10, 42, 22))
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(10)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.widget_4 = QtGui.QWidget(surveyMem)
        self.widget_4.setGeometry(QtCore.QRect(60, 220, 591, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget_4.setFont(font)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.radioButton_3 = QtGui.QRadioButton(self.widget_4)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 10, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.widget_4)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 30, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_6 = QtGui.QRadioButton(self.widget_4)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 50, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))

        self.retranslateUi(surveyMem)
        QtCore.QMetaObject.connectSlotsByName(surveyMem)

    def retranslateUi(self, surveyMem):
        surveyMem.setWindowTitle(_translate("surveyMem", "Survey", None))
        self.checkBox.setText(_translate("surveyMem", "Easy learning method", None))
        self.checkBox_2.setText(_translate("surveyMem", "The sentences make it easy", None))
        self.checkBox_3.setText(_translate("surveyMem", "It would work better with different passwords", None))
        self.ok_btn.setText(_translate("surveyMem", "Ok", None))
        self.label.setText(_translate("surveyMem", "Please, let us know what you think!", None))
        self.label_2.setText(_translate("surveyMem", "Special notes:", None))
        self.label_3.setText(_translate("surveyMem", "Rate this password learning strategy (1-10):", None))
        self.radioButton_3.setText(_translate("surveyMem", "I would use this method in the future.", None))
        self.radioButton_4.setText(_translate("surveyMem", "I would only use this method if I generate my own sentences.", None))
        self.radioButton_6.setText(_translate("surveyMem", "I would never use this method for my passwords.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    surveyMem = QtGui.QWidget()
    ui = Ui_surveyMem()
    ui.setupUi(surveyMem)
    surveyMem.show()
    sys.exit(app.exec_())

