class Student:
    def getStd(self):
        self.__roll=input("Enter Roll No")
        self.__name=input("Enter Name:")
    def putStd(self):
        print(self.__roll,self.__name)

class BA(Student):
    def getBA(self):
        self.getStd()

        self.__eco=input("Enter Economics:")
        self.__his=input("Enter History:")
    def putBA(self):
        self.putStd()
        print(self.__eco,self.__his)

S=BA()
#S.getStd()
S.getBA()

#S.putStd()
S.putBA()





