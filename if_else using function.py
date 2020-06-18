def greater(a,b):
    if(a>b):
        return a
    else:
        return b

            
x=int(input("ENter 1st number: "))
y=int(input("ENter 2nd number: "))

g=greater(x,y)

print("Large number is :",g)

#===========================================

def abc(name):
    if (name[0]=="A"):
        return True
    else:
        return False

x=input("Enter your name : ")
print(abc(x))

#left side or right operator

def abc(name):
    if (name[0]==("A")) or (name[0]==("M")):
        return True
    else:
        return False

x=input("Enter your name : ")
print(abc(x))

