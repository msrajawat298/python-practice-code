class Bank:
    def openAccount(self):
        self.__name =input('Enter your name: ')
        self.__mobile_no =int(input('ENter ur mobile number : '))
        self.__balance=int(input('Enter Balance: '))
    def showAccount(self):
         print('=================================ACCOUNT DETAILS====================================')
         print('Name :',self.__name)
         print('MObile number : ',self.__mobile_no)
         print('Balance:',self.__balance)

#C1 or C2 is the costumer object of bank
C1=Bank()
C2=Bank()
C1.openAccount()
C2.openAccount()
C1.showAccount()
C2.showAccount()
