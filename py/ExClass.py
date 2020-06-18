class Student:
    def GetStudent(self):
        self.__rollno=input("Enter Roll No:")
        self.__name=input("Enter Name:")
    def GetMarks(self):
        self.__p =int(input("Enter Physics Marks:"))
        self.__c = int(input("Enter Chemistry Marks:"))
        self.m = int(input("Enter Maths Marks:"))
    def ShowResult(self):
        print('Roll No:',self.__rollno)
        print('Name:', self.__name)
        print('Physics:', self.__p)
        print('Chemistry:', self.__c)
        print('Maths:', self.m)
S=Student() #call the default constructor to instantiate the object
S.GetStudent()
print('======================================GET MARKS====================================')
S.GetMarks()
print('======================================RESULT=======================================')
S.ShowResult()
print('=================================s.m=4===============================================')
S.m=4
print('======================================RESULT=======================================')

S.ShowResult()

























