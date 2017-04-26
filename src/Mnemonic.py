import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject
import datetime
import dateutil.parser

from createPasswordWindow import Ui_createPasswordWindow
from createUserWindow import Ui_createUserWindow
from infoWindow import Ui_generalInfo
from loginWindow import Ui_loginWindow
from welcomeWindow import Ui_createPassword
from myDialog import Ui_Dialog
from surveyMem import Ui_surveyMem
from surveyNoMem import Ui_surveyNoMem

from myUser import myUser
from myExcel import myExcel

app = QtGui.QApplication(sys.argv)

createPasswordWindow = QtGui.QWidget()
createUserWindow = QtGui.QWidget()
infoWindow = QtGui.QWidget()
loginWindow = QtGui.QWidget()
welcomeWindow = QtGui.QWidget()
myDialog = QtGui.QWidget()
surveyPass = QtGui.QWidget()
surveyNoPass = QtGui.QWidget()

create_password_window = Ui_createPasswordWindow()
create_user_window = Ui_createUserWindow()
info_window = Ui_generalInfo()
login_window = Ui_loginWindow()
welcome_window = Ui_createPassword()
my_dialog_window = Ui_Dialog()
survey_passed_window = Ui_surveyMem()
survey_not_passed_window = Ui_surveyNoMem()

class mnemonic(QtGui.QWidget):
    current_user = myUser()
    setupStart = ""
    setupEnd = ""
    xlsheet = myExcel()
    startTime = ""

    password_attempts = 0
    password_max_attempts = 3

    def __init__(self):

        print(datetime.date.today())
        super(mnemonic, self).__init__()
        create_password_window.setupUi(createPasswordWindow)
        create_user_window.setupUi(createUserWindow)
        info_window.setupUi(infoWindow)
        login_window.setupUi(loginWindow)
        welcome_window.setupUi(welcomeWindow)
        my_dialog_window.setupUi(myDialog)
        survey_passed_window.setupUi(surveyPass)
        survey_not_passed_window.setupUi(surveyNoPass)

        #setting up events
        create_password_window.retry_btn_2.clicked.connect(self.openInfoWindow_event)
        create_password_window.retry_btn.clicked.connect(self.changeSentence_event)
        create_password_window.ok_btn.clicked.connect(self.finishCreatingPassword_event)
        create_user_window.ok_btn.clicked.connect(self.createMnemonic_event)
        login_window.showPassword_cb.stateChanged.connect(self.passwordCheckbox_event)
        login_window.ok_btn.clicked.connect(self.checkMemory)
        welcome_window.createNewPassword_btn.clicked.connect(self.createNewPassword_event)
        welcome_window.checkMemory_btn.clicked.connect(self.login_event)
        my_dialog_window.ok_btn.clicked.connect(self.closeMyDialog_event)
        #setting up format
        create_password_window.sentence_label.setText(self.xlsheet.getRandomItem("Sentence"))

    def openWindow(self):
        welcomeWindow.show()
        surveyNoPass.show()
        surveyPass.show()
        sys.exit(app.exec_())

    def finishCreatingPassword_event(self):
        user_was_created = False

        if(create_password_window.password_le.text()==""):
            print("password field empty")
            self.openDialog("Password field is empty")
        elif(len(create_password_window.password_le.text())<8):
            print("Your password must be at least 8 characters")
            self.openDialog("Your password must be at least 8 characters")
        else:
            self.current_user.password = create_password_window.password_le.text()
            self.current_user.mnemonicSentence = create_password_window.sentence_label.text()
            temp_setupTime = (datetime.datetime.now()-dateutil.parser.parse(self.startTime)).total_seconds()
            self.current_user.setupTime = str(temp_setupTime)
            print(self.current_user.setupTime )
            user_was_created = self.current_user.save()
            if (user_was_created):
                print("user saved successfully")
                self.openDialog("User created successfully!!!")
                createPasswordWindow.close()
            else:
                print("User did not save")

    def openInfoWindow_event(self):
        infoWindow.show()

    def passwordCheckbox_event(self):
        if login_window.showPassword_cb.isChecked():
            login_window.password_le.setEchoMode(QtGui.QLineEdit.Normal)
        else:
            login_window.password_le.setEchoMode(QtGui.QLineEdit.Password)

    def closeMyDialog_event(self):
        myDialog.close()

    def createNewPassword_event(self):
        createUserWindow.show()
        welcomeWindow.close()

    def createMnemonic_event(self):
        print(create_user_window.passwordType_cb.currentIndex())
        if(create_user_window.name_le.text()!="" and create_user_window.lastName_le.text()!="" and create_user_window.passwordType_cb.currentIndex()!= 0):
            self.startTime = datetime.datetime.now().isoformat()
            self.current_user = myUser()
            self.current_user.name = create_user_window.name_le.text()
            self.current_user.lastName = create_user_window.lastName_le.text()
            self.current_user.passwordType = create_user_window.passwordType_cb.currentText()
            self.current_user.username = create_user_window.name_le.text() + create_user_window.lastName_le.text()+create_user_window.passwordType_cb.currentText()
            if(self.current_user.checkIfUserExists()==False):
                self.current_user.passwordCreationDate = datetime.datetime.today().isoformat()
                self.setupStart = datetime.datetime.now().isoformat()
                createPasswordWindow.show()
                createUserWindow.close()
            else:
                self.openDialog("There's already a username in the database with this information. Please choose a different type of password.")

    def changeSentence_event(self):
        create_password_window.sentence_label.setText(self.xlsheet.getRandomItem("Sentence"))

    def login_event(self):
        loginWindow.show()
        welcomeWindow.close()

    def checkMemory(self):
        name = login_window.name_le.text()
        lastName = login_window.lastName_le.text()
        passType = login_window.passwordType_cb.currentText()
        username = name+lastName+passType
        password = login_window.password_le.text()
        userStartDate = dateutil.parser.parse(self.current_user.getInfo(username,'Password creation date'))
        totalDays = ((datetime.datetime.now()-userStartDate).total_seconds())/(24*60*60)
        print(totalDays)

        passwords_match = self.current_user.checkMatch(username, 'password', password)
        user_was_already_tested = self.current_user.checkIfTested(username)

        if(user_was_already_tested):
            self.openDialog('The specified user for the specified password type already completed the survey')
        elif(login_window.passwordType_cb.currentIndex()==0):
            self.openDialog('Remember to choose the correct "Password Type"')
        elif(passwords_match):
            self.openDialog("Congratulations!!!\n You were able to remember the password successfully!")
            self.current_user.updateBook(username, "Password-check date", datetime.datetime.today().isoformat())
            self.current_user.updateBook(username, "total attempts", self.password_attempts)
            self.current_user.updateBook(username, "user remembered password", "yes")
            self.password_attempts = 0
            loginWindow.close()
        elif(self.password_attempts>=self.password_max_attempts):
            self.openDialog("Im sorry!!!\n You were unable to remember the password after {} attempts!\Saving current data".format(self.password_attempts))
            self.current_user.updateBook(username, "Password-check date", datetime.datetime.today().isoformat())
            self.current_user.updateBook(username, "total attempts", self.password_attempts)
            self.current_user.updateBook(username, "user remembered password", "no")
            self.password_attempts = 0
            loginWindow.close()
        else:
            self.password_attempts = self.password_attempts+1
            attempts_left = self.password_max_attempts - self.password_attempts
            self.openDialog("Passwords did not match!!!\n You have {} attempts left!".format(attempts_left))
            self.current_user.updateBook(username,"Password-check date", datetime.datetime.today().isoformat())

    def openDialog(self,text):
        my_dialog_window.label.setText(text)
        myDialog.show()

if __name__ == "__main__":
    myApp = mnemonic()
    myApp.openWindow()