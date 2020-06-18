class Student:
 def getStd(self):
    self.__roll = input("Enter Roll No")
    self.__name = input("Enter Name:")
 def putStd(self):
    print(self.__roll, self.__name)


class BA(Student):
    def getBA(self):
        self.getStd()
        self._eco =int(input("Enter Economics:"))
        self._his =int(input("Enter History:"))
    def putBA(self):
        self.putStd()
        print(self._eco, self._his)


class Result(BA):
    def getResult(self):
        self.getBA()
        self.__totalmarks=self._eco+self._his
        self.__per=self.__totalmarks/2
    def putResult(self):
        self.putBA()
        print(self.__totalmarks,self.__per)

S=Result()
S.getResult()
S.putResult()





