# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myDialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(483, 162)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 431, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.ok_btn = QtGui.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(390, 110, 61, 31))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Notice", None))
        self.label.setText(_translate("Dialog", "There\'s already a username in the database with this information. Please choose a different type of password.", None))
        self.ok_btn.setText(_translate("Dialog", "Ok!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

