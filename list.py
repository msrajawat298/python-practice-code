#List and Arrays are two different Data types in python.

#Array is a built in module or package which has to be imported.

#List doesn’t require any import to manipulate on it.

#The major difference is Array deals with similar data types (similar to C)

b#ut List support distinct data types which is not available in C.

#For ARRAY refer

#list

fruits =['apple','banana','grapes',',mango']
print(fruits)
print(fruits[0])
print(fruits[0].title())
fruits[0] = 'tamato'
print(fruits)
fruits.append('apple')#append:- is use for add the data in the list.
                      #synatx:- list_name.append('Variable or data')
print(fruits)
print(fruits[-1])
#==============insert method==================
fruits.insert(1,'pea')#insert:- is use for add the data in the list or a particular index.
                      #synatx:- list_name.insert(index number, 'Variable or data')
print(fruits)
#==============del method==================
del fruits[1]
print(fruits)

#==============pop method==================
fruits.pop()
x=fruits.pop()
x=fruits.pop(0)
print(fruits)
print(x)

#==============refer to notes==================
