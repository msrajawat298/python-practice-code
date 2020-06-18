a=int(input('enter the first number :'))
b=int(input('enter the second number :'))

large = a
if b>large:
    large = b
print(large,'is largest number')

#================== U S I N G  M A X  O P E R A T O R ============================4

def large(a,b,c,d):
    return max(a,b,c,d)

a=int(input('enter the 1st number :'))
b=int(input('enter the 2nd number :'))
c=int(input('enter the 3rd number :'))
d=int(input('enter the 4th number :'))

x=large(a,b,c,d)
print("Large : ",x)

#================== U S I N G  M I N  O P E R A T O R ============================4

def large(a,b,c,d):
    return min(a,b,c,d)

a=int(input('enter the 1st number :'))
b=int(input('enter the 2nd number :'))
c=int(input('enter the 3rd number :'))
d=int(input('enter the 4th number :'))

x=large(a,b,c,d)
print("Large : ",x)
