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
    def Search(self,min,max):
        self.per=int((self.__p+self.__c+self.__m)/3);
        if(self.per>=min and self.per<=max):
            return True
        else:
            return False


SL=list() #or S=[]
n=int(input('Enter Number Of Objects:'))
for i in range(0,n):
  SL.append(Student())
min=int(input('Enter Min Percentage?'))
max=int(input('Enter Max Percentage?'))

count=0
for S in SL:
 found=S.Search(min,max)
 if(found):
     S.ShowResult()
     count+=1
if(count==0):
   print("Record Not Found")