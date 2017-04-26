# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomeWindow.ui'
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

class Ui_createPassword(object):
    def setupUi(self, createPassword):
        createPassword.setObjectName(_fromUtf8("createPassword"))
        createPassword.resize(410, 480)
        self.frame = QtGui.QFrame(createPassword)
        self.frame.setGeometry(QtCore.QRect(90, 130, 231, 251))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.checkMemory_btn = QtGui.QPushButton(self.frame)
        self.checkMemory_btn.setGeometry(QtCore.QRect(50, 150, 131, 51))
        self.checkMemory_btn.setObjectName(_fromUtf8("checkMemory_btn"))
        self.createNewPassword_btn = QtGui.QPushButton(self.frame)
        self.createNewPassword_btn.setGeometry(QtCore.QRect(50, 50, 131, 51))
        self.createNewPassword_btn.setObjectName(_fromUtf8("createNewPassword_btn"))

        self.retranslateUi(createPassword)
        QtCore.QMetaObject.connectSlotsByName(createPassword)

    def retranslateUi(self, createPassword):
        createPassword.setWindowTitle(_translate("createPassword", "Welcome", None))
        self.checkMemory_btn.setText(_translate("createPassword", "Test Password", None))
        self.createNewPassword_btn.setText(_translate("createPassword", "Create New Password", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    createPassword = QtGui.QWidget()
    ui = Ui_createPassword()
    ui.setupUi(createPassword)
    createPassword.show()
    sys.exit(app.exec_())

