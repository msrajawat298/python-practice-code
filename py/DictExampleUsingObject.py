class Student:
    def __init__(self,rollno):
        self.__rollno=rollno
        self.__name=input("Enter Name:")
        self.__p =int(input("Enter Physics Marks:"))
        self.__c = int(input("Enter Chemistry Marks:"))
        self.__m = int(input("Enter Maths Marks:"))
    def ShowResult(self):
        print('Roll No:',self.__rollno)
        print('Name:', self.__name)
        print('Physics:', self.__p)
        print('Chemistry:', self.__c)
        print('Maths:', self.__m)
SD=dict() #or S={}
n=int(input('Enter Number Of Objects:'))
for i in range(0,n):
   rollno=input('Enter Roll no:')
   SD.setdefault(rollno,Student(rollno))
rollno=input('Enter Roll No U want to Serach?')

S=SD.get(rollno,'Record Not Found')
if(isinstance(S,Student)):
 S.ShowResult()
else:
 print(S)












