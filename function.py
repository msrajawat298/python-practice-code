#procedure: we define a function or create a function is known as procedure.
#+ operator take input two or more

print('===========================ADDTION USING FUNCTION==========================\n')
#function : def is use for define the function

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def pro(x,y):
    return x*y

def div(x,y):
    return x/y

a=int(input('Enter the 1st number : '))
b=int(input('Enter the 2nd number : '))

c=add(a,b)
print('Addtion of ',a,'-',b,' = ',c)

print('================================Subtraction function calling==================\n')
c=sub(a,b)
print('Substraction of ',a,'-',b,' = ',c)
print('================================Multiplication================================\n')
a=int(input('Enter the 1st number : '))
b=int(input('Enter the 2nd number : '))
c=pro(a,b)
print('Multiplication of ',a,'*',b,' = ',c)
print('================================Divition=======================================\n')
c=div(a,b)

print('Divition of ',a,'/',b,' = ',c)
