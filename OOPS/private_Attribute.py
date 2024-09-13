class Account:
    def __init__(self,acc_no,acc_password):
        self.acc_no = acc_no
        self.__acc_password = acc_password ## use __ ahead of attribute to make it private.

    def showPassword(self):
        return self.__acc_password
    
    def __update(self):
        print("Private function")

    def runPrivateFunction(self):
        self.__update()

acc1 = Account("1234","abcde")

print(acc1.acc_no)
## print(acc1.acc_password) #shows error

print(acc1.showPassword())

## acc1.update() ##shows error

acc1.runPrivateFunction()