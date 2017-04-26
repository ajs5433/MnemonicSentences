# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoWindow.ui'
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

class Ui_generalInfo(object):
    def setupUi(self, generalInfo):
        generalInfo.setObjectName(_fromUtf8("generalInfo"))
        generalInfo.resize(637, 366)
        self.label = QtGui.QLabel(generalInfo)
        self.label.setGeometry(QtCore.QRect(40, 40, 561, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(generalInfo)
        QtCore.QMetaObject.connectSlotsByName(generalInfo)

    def retranslateUi(self, generalInfo):
        generalInfo.setWindowTitle(_translate("generalInfo", "Info", None))
        self.label.setText(_translate("generalInfo", "To make your password more secure you can:\n"
" \n"
"\n"
"        -Substitute lettes for symbols with similar meanings. For instance \"and\" and \"&\", \"for\" and \"4\", \"to\" and \"2\". \n"
"\n"
"        -You can personalize it using words in different languages.\n"
"\n"
"        -Add personalized symbols to modify the sentence.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    generalInfo = QtGui.QWidget()
    ui = Ui_generalInfo()
    ui.setupUi(generalInfo)
    generalInfo.show()
    sys.exit(app.exec_())

