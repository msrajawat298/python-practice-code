class Student:
    def __init__(self):
        self.__rollno=input("Enter Roll No:")
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
    def Search(self,rollno):
        if(rollno==self.__rollno):
            return True
        else:
            return False


SL=list() #or S=[]
n=int(input('Enter Number Of Objects:'))
for i in range(0,n):
  SL.append(Student())
rollno=input('Enter Roll No U want to Serach?')

for S in SL:
 found=S.Search(rollno)
 if(found):
     S.ShowResult()
     break;
if(not found):
   print("Record Not Found")
