class TwoNum:
    def GetValues(self):
        self.__x=int(input('Enter x:'))
        self.__y=int(input('Enter y:'))
    def ShowValues(self):
        print(self.__x,self.__y,sep=',')
    def Add(self,T):
        R=TwoNum()
        R.__x=self.__x+T.__x
        R.__y=self.__y+T.__y
        return R
T1=TwoNum()
T1.GetValues()
T2=TwoNum()
T2.GetValues()

T3=T1.Add(T2)
T1.ShowValues()
T2.ShowValues()
T3.ShowValues()

