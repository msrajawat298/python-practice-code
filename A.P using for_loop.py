def ap(a,l,d):
    result =0
    for i in range(a,l+1,d):
        print (i)
        result = result+i
    return result

a=int(input('Enter the first number of the series : '))
d=int(input('Enter the differnce betwen two number of the series:'))
n=int(input('Enter the number of term in the series: '))

l=a+(n*d-d)
print(ap(a,l,d))
