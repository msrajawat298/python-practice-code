#sum of digits such as: 1234=1+2+3+4=10

x=input("Enter any digit : ")
y=len(x)
i=0
result=0
while(i<y):
    result = result + int(x[i])
    i=i+1
print(result)
