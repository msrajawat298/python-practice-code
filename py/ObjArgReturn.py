class Twonum:
    def getValues(self):
        self.__x=int(input("Enter First Number:"))
        self.__y=int(input("Enter Second Number:"))
    def putValues(self):
        print(self.__x,self.__y)

    def add(self,T):
        R=Twonum()
        R.__x=self.__x+T.__x
        R.__y=self.__y+T.__y
        return  R
T1=Twonum()
T2=Twonum()
T1.getValues()
T2.getValues()
Z=T1.add(T2)
T1.putValues()
T2.putValues()
Z.putValues()