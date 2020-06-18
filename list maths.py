#9%2 = remainder 1
#2**2 = 8

x =list(range(1,11))
print(x)
#======================================
x =list(range(1,11))
for i in x:
    if i%2==0:
        print(i)
        
#======================================
x =list(range(1,11))
y=[]
for i in x:
    a= i**2
    y.append(a)
print('Squares list : ',y)
#============not include 5==========================
x =list(range(1,11))
for i in x:
   if i==5:
      continue
    print(i)


