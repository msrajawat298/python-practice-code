print('Enter the marks of The Given Subjects\n')

m =int(input('Enter the marks of MAths : '))
e =int(input('Enter the marks of English : '))
h =int(input('Enter the marks of Hindi : '))
s =int(input('Enter the marks of Scince : '))
c =int(input('Enter the marks of Computers : '))

total = m+e+h+s+c
avg = total/5
print('Total Marks :',total,"\nAverage :",avg)

if avg>=80:
    print('\nGrade A')
elif avg>=70 and avg<80:        #in python else if replace by elif
    print('\nGrade B')

elif avg>=60 and avg<70:
    print('\nGrade C')

elif avg>=50 and avg<60:
    print('\nGrade C')

elif avg<50:
    print('\nFailed')

