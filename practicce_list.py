x=int(input('How many item you want to store in the list: '))
# 1st of all we create a empty list
items = []

i=0    #bcz postion of the list starting from index 0
while(i<x):
    y = input('Enter the item for you want to add in the item list : ')
    items.append(y)
    i=i+1

z=sorted(items)

print('Your list of item is : ', z)

a=input('you want to change any item in list yes/no : ')
if(a=='yes'):
    b=input('Which Item you want to change : ')
    c =z.index(b)

print('Okay which item u wnat at place of',b)
t=input()
z[c]=t
print('now your complete list is ',z)
if(a=='no'):
    print('Thankyou')
    






