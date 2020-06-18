class Student:
 def getStd(self):
    self.__roll = input("Enter Roll No")
    self.__name = input("Enter Name:")
 def putStd(self):
    print(self.__roll, self.__name)


class BA(Student):
    def getBA(self):
        self.getStd()
        self.__eco =int(input("Enter Economics:"))
        self.__his =int(input("Enter History:"))
    def putBA(self):
        self.putStd()
        print(self.__eco, self.__his)
    def getTotal(self):
        return (self.__eco+self.__his);

class Result(BA):
    def getResult(self):
        self.getBA()
        self.__totalmarks=self.getTotal()
        self.__per=self.__totalmarks/2
    def putResult(self):
        self.putBA()
        print(self.__totalmarks,self.__per)

S=Result()
S.getResult()
S.putResult()





