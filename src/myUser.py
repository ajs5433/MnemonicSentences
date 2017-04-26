import datetime
import time
import json
import os
from datetime import datetime

filepath = 'A:/Desktop/mySecondProject/Project Files/userBook.txt'

class myUser:
    userBook = {}
    name =  ""
    lastName = ""
    username = ""
    password = ""
    passwordType = ""
    mnemonicSentence = ""
    passwordCreationDate = ""
    passwordTestDate = ""
    setupTime = ""

    '''
    passwordTestDate = "No test date yet"
    wouldUseThisMethodInTheFuture ="N/A"
    totalAttempts = "N/A"
    rememberedFromPassword = "N/A"
    specialNotes = "N/A"
    '''


    """
    def __init__(self,n,l,pt):
        # print("New User!")

        self.name = n
        self.lastName = l
        self.passwordType = pt

        self.username = self.name + self.lastName + self.passwordType
    """

    def checkIfUserExists(self):
        exists = False

        #check if file exists and if its empty
        if (os.path.isfile(filepath)):
            if(os.stat(filepath).st_size != 0):
                with open(filepath, "r") as f:
                    dataString = f.read()
                    dataBook = json.loads(dataString)

                    if self.username in dataString:
                        print("there's already a user named "+ self.username)
                        exists = True
        return exists

    def save(self):
        # print("Saving user")
        create = False

        # check if file exists and if its empty
        if (os.path.isfile(filepath)):
            if (os.stat(filepath).st_size != 0):
                with open(filepath, "r") as f:
                    dataString = f.read()
                    dataBook = json.loads(dataString)

                    if self.username in dataString:
                        print("there's already a user named " + self.username)
                        create = False
                    else:
                        print('no user named ' + self.username)
                        create = True

                if (create):
                    self.userBook[self.username] = {
                        'name:': self.name,
                        'last name': self.lastName,
                        'password type': self.passwordType,
                        'password': self.password,
                        'Full mnemonic sentence': self.mnemonicSentence,
                        'Password creation date': self.passwordCreationDate,
                        'Password-check date': self.passwordTestDate,
                        'setup time': self.setupTime,
                        'user remembered password': "",
                    }

                    dataBook.update(self.userBook)

                    with open(filepath, "w") as f:
                        newbook = json.dumps(dataBook)
                        f.write(newbook)
                        print("Saving new user!!  \nName: {} \tLast Name: {}\tPassword Type: {}".format(self.name, self.lastName, self.passwordType))

            else:
                self.userBook[self.username] = {
                    'name:': self.name,
                    'last name': self.lastName,
                    'password type': self.passwordType,
                    'password': self.password,
                    'Full mnemonic sentence': self.mnemonicSentence,
                    'Password creation date': self.passwordCreationDate,
                    'Password-check date': self.passwordTestDate,
                    'setup time': self.setupTime,
                    'user remembered password': "",
                }

                with open(filepath, "w") as f:
                    newbook = json.dumps(self.userBook)
                    f.write(newbook)
                    print(
                        "Saving new user!!  \nName: {} \tLast Name: {}\tPassword Type: {}".format(self.name,
                                                                                                  self.lastName,
                                                                                                  self.passwordType))
                    create = True

        else:
            self.userBook[self.username] = {
                'name:': self.name,
                'last name': self.lastName,
                'password type': self.passwordType,
                'password': self.password,
                'Full mnemonic sentence': self.mnemonicSentence,
                'Password creation date': self.passwordCreationDate,
                'Password-check date': self.passwordTestDate,
                'setup time': self.setupTime,
                'user remembered password': "",
            }

            with open(filepath, "w") as f:
                newbook = json.dumps(self.userBook)
                f.write(newbook)
                print(
                    "Saving new user!!  \nName: {} \tLast Name: {}\tPassword Type: {}".format(self.name, self.lastName,
                                                                                              self.passwordType))
                create = True

        return create

    def checkMatch(self, username, datafield, data):
        match = False

        if (os.path.isfile(filepath)):
            if (os.stat(filepath).st_size != 0):
                with open(filepath, "r") as f:
                    dataString = f.read()
                    dataBook = json.loads(dataString)

                    if self.username in dataString:
                        if(str(dataBook[username][datafield])==data):
                            print('password matched!!')
                            match = True
                        else:
                            print('passwords {} and {} did not match'.format(data,dataBook[username][datafield]))
                            match = False

                    else:
                        print('username does not exist')
                        match = False
        return match


    def getInfo(self, username, datafield):
        data = ""

        if (os.path.isfile(filepath)):
            if (os.stat(filepath).st_size != 0):
                with open(filepath, "r") as f:
                    dataString = f.read()
                    dataBook = json.loads(dataString)

                    if self.username in dataString:
                        data = dataBook[username][datafield]
                    else:
                        print('username does not exist')

        return data

    def checkIfTested(self, username):
        tested = False

        if (os.path.isfile(filepath)):
            if (os.stat(filepath).st_size != 0):
                with open(filepath, "r") as f:
                    dataString = f.read()
                    dataBook = json.loads(dataString)

                    if self.username in dataString:
                        if(dataBook[username]['user remembered password'] == ""):
                            tested = False
                            print('User has not been tested yet')
                        elif(dataBook[username]['user remembered password'] == "yes" or dataBook[username]['user remembered password'] == "no" ):
                            print('user was already tested')
                            tested = True
                    else:
                        print('user does not exist in the database')
        return tested

    def updateBook(self, username, datafield, newdata):
        updated = False

        if (os.path.isfile(filepath)):
            if (os.stat(filepath).st_size != 0):
                with open(filepath, "r") as f:
                    dataString = f.read()
                    dataBook = json.loads(dataString)

                    if self.username in dataString:
                        dataBook[username][datafield] = newdata
                        dataBook.update(self.userBook)

                        with open(filepath, "w") as f:
                            newbook = json.dumps(dataBook)
                            f.write(newbook)
                            print("Updating user: {} with {} = {}".format(username, datafield, newdata))
                            updated = True
                    else:
                        print('user not updated')
        return updated

if __name__ == "__main__":
    myuser = myUser("gotta", "Go888", "Test")
    myuser.save()