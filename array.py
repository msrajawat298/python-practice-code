arr = [10,20,30,40,50]

print('\nPositve Index : ',arr[0],arr[1],arr[2],arr[3],arr[4])
print('\nNegative Index : ',arr[0],arr[-4],arr[-3],arr[-2],arr[-1])

print('\nLength of the Index :', len(arr)) #len is use to find the length of the list
                                         #Synatx :- len(name of the list) 

add =['M','A','Y','A','N','K']
print("\nNew List",add)
add.append('Singh') # append is use to add the data into exiting list
print("Aftetr adding new data : ",add)

#del,remove,pop are use to remove the data form the list
del arr[4] #syntax : -  del list_name[x], where x is index number of the list.
print("\nList after deleting the data using del : ",arr)
arr.pop(2)#syntax--> list_name.pop(x), where , index number of the list.
print('List after deleting the data using pop method:',arr)
print("\nLength of list after removing or deleting the data : ",len(arr))
add.remove('Singh')#syntax-->list_name.remove(x), where, index number of the list.
print("\nList after deleting the data using remove method ",add)

#==============================MODIFICAIONS============================================

add[0] = 'MAyank' # for modification in the list use this synatx: list_name[x]=new data
                  # where x is a index no. where u want to edit the data
print(add)
#================================Concatenating==========================================
arr+=add  # for adding the two or more differnt list into a one list using
          #syntax add = first list + 2nd list +......etc
print(arr)


