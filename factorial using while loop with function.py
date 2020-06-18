def fact(x):
    f=1
    while(x>=1):
        f = f*x
        x=x-1
    return f

a=int(input("Enter any number : "))

print("ANswer : ",fact(a))
        
