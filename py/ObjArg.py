#vikashmaharolya@gmail.com
#schoolfun
class Bank:
    def openAccount(self):
        self.__name =input('Enter your name:')
        self.__balance=int(input('Enter Balance:'))
    def showAccount(self):
         print('Balance:',self.__balance)
    def transfer(self,T,amount):
         T.__balance=T.__balance+amount
         self.__balance=self.__balance-amount



C1=Bank()
C2=Bank()
C1.openAccount()
C2.openAccount()
C1.showAccount()
C2.showAccount()
C1.transfer(C2,200000)
C1.showAccount()
C2.showAccount()
C2.transfer(C1,500000)
