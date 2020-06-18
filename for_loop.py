#for loop
#['one','two','three','only string object',1,2,3]
#series 0 to 10
#synatx : for variable_name in range(arguments):
#start and stop arguments it use if we start counting from 2 to 12


for i in range(1,11):
    print(i)
#=========================================
#function define sum upto n digits such as 1+2+3+....n

def add(n):
    result = 0
    for i in range(1,n+1):
        result = result + i
    return result
        

a=int(input("Enter any number : "))

print('sum =', add(a))

print('===================step argument===============')

for i in range(1,10,2): 
    print(i)
    
