# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createPasswordWindow.ui'
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

class Ui_createPasswordWindow(object):
    def setupUi(self, createPasswordWindow):
        createPasswordWindow.setObjectName(_fromUtf8("createPasswordWindow"))
        createPasswordWindow.resize(729, 257)
        self.retry_btn = QtGui.QPushButton(createPasswordWindow)
        self.retry_btn.setGeometry(QtCore.QRect(660, 120, 41, 41))
        self.retry_btn.setObjectName(_fromUtf8("retry_btn"))
        self.sentence_label = QtGui.QLabel(createPasswordWindow)
        self.sentence_label.setGeometry(QtCore.QRect(40, 100, 601, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sentence_label.setFont(font)
        self.sentence_label.setText(_fromUtf8(""))
        self.sentence_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sentence_label.setWordWrap(True)
        self.sentence_label.setObjectName(_fromUtf8("sentence_label"))
        self.password_le = QtGui.QLineEdit(createPasswordWindow)
        self.password_le.setGeometry(QtCore.QRect(450, 210, 161, 21))
        self.password_le.setObjectName(_fromUtf8("password_le"))
        self.label_2 = QtGui.QLabel(createPasswordWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 601, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ok_btn = QtGui.QPushButton(createPasswordWindow)
        self.ok_btn.setGeometry(QtCore.QRect(620, 200, 81, 31))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.label = QtGui.QLabel(createPasswordWindow)
        self.label.setGeometry(QtCore.QRect(360, 210, 71, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.retry_btn_2 = QtGui.QPushButton(createPasswordWindow)
        self.retry_btn_2.setGeometry(QtCore.QRect(670, 30, 31, 31))
        self.retry_btn_2.setObjectName(_fromUtf8("retry_btn_2"))

        self.retranslateUi(createPasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(createPasswordWindow)

    def retranslateUi(self, createPasswordWindow):
        createPasswordWindow.setWindowTitle(_translate("createPasswordWindow", "Create your password", None))
        self.retry_btn.setText(_translate("createPasswordWindow", "Retry", None))
        self.label_2.setText(_translate("createPasswordWindow", "Generate a password from the given sentence! \n"
"Feel free to personalize the sentence to make it more secure.", None))
        self.ok_btn.setText(_translate("createPasswordWindow", "Ok", None))
        self.label.setText(_translate("createPasswordWindow", "Password:", None))
        self.retry_btn_2.setToolTip(_translate("createPasswordWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Hint</span></p></body></html>", None))
        self.retry_btn_2.setText(_translate("createPasswordWindow", "?", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    createPasswordWindow = QtGui.QWidget()
    ui = Ui_createPasswordWindow()
    ui.setupUi(createPasswordWindow)
    createPasswordWindow.show()
    sys.exit(app.exec_())

