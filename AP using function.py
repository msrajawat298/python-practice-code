#A.P:- 1+2+5+7+9...............

def ap(a,d,l):
    while(a<=1):
        print (a)
        a = a + d

a=int(input("\nEnter first term of AP : "))
d=int(input("\nEnter differnce b/w two term AP : "))
n=int(input("\nEnter number of term : "))

l = a + n*d -d

f=ap(a,d,l)


