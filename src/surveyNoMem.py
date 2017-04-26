# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surveyNoMem.ui'
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

class Ui_surveyNoMem(object):
    def setupUi(self, surveyNoMem):
        surveyNoMem.setObjectName(_fromUtf8("surveyNoMem"))
        surveyNoMem.resize(711, 546)
        self.widget = QtGui.QWidget(surveyNoMem)
        self.widget.setGeometry(QtCore.QRect(50, 100, 591, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget.setFont(font)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.radioButton = QtGui.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(20, 10, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 30, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_5 = QtGui.QRadioButton(self.widget)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 50, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.widget_2 = QtGui.QWidget(surveyNoMem)
        self.widget_2.setGeometry(QtCore.QRect(50, 200, 591, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.widget_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 10, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.widget_2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 30, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_6 = QtGui.QRadioButton(self.widget_2)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 50, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.ok_btn = QtGui.QPushButton(surveyNoMem)
        self.ok_btn.setGeometry(QtCore.QRect(600, 500, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.label = QtGui.QLabel(surveyNoMem)
        self.label.setGeometry(QtCore.QRect(70, 40, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(surveyNoMem)
        self.textEdit.setGeometry(QtCore.QRect(50, 400, 611, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(surveyNoMem)
        self.label_2.setGeometry(QtCore.QRect(50, 380, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget_3 = QtGui.QWidget(surveyNoMem)
        self.widget_3.setGeometry(QtCore.QRect(50, 290, 591, 51))
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

        self.retranslateUi(surveyNoMem)
        QtCore.QMetaObject.connectSlotsByName(surveyNoMem)

    def retranslateUi(self, surveyNoMem):
        surveyNoMem.setWindowTitle(_translate("surveyNoMem", "Survey", None))
        self.radioButton.setText(_translate("surveyNoMem", "I was able to remember the sentence, but I made mistakes writing the password.", None))
        self.radioButton_2.setText(_translate("surveyNoMem", "The method works, but the assigned sentences were difficult to rememer.", None))
        self.radioButton_5.setText(_translate("surveyNoMem", "I did not remember the sentence at all.", None))
        self.radioButton_3.setText(_translate("surveyNoMem", "I would use this method in the future.", None))
        self.radioButton_4.setText(_translate("surveyNoMem", "I would only use this method if I generate my own sentences.", None))
        self.radioButton_6.setText(_translate("surveyNoMem", "I would never use this method for my passwords.", None))
        self.ok_btn.setText(_translate("surveyNoMem", "Ok", None))
        self.label.setText(_translate("surveyNoMem", "Please, let us know what you think!", None))
        self.label_2.setText(_translate("surveyNoMem", "Special notes:", None))
        self.label_3.setText(_translate("surveyNoMem", "Rate this password learning strategy (1-10):", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    surveyNoMem = QtGui.QWidget()
    ui = Ui_surveyNoMem()
    ui.setupUi(surveyNoMem)
    surveyNoMem.show()
    sys.exit(app.exec_())

