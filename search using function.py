#x ="i like to play guitar and i am learing guitar"
#input =2
#1=variable
#2= word which u want to search

#Basicly we create a function to find the string or word from the senteces at 2nd poition.

def position2(search,target):
    first =(search.find(target))
    second = (search.find(target,first+1))
    #return first #no any required to return this value bcz we need to find 2nd position of the string
    return second

x =("i like to play guitar and i am learing guitar")
y=(position2(x,"like"))
print(y)
if y==-1:
    print("Entered string not found more than one place.")

