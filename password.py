#password

while True:
    x = str(input("What is your username ?\nUsername :  "))
    if(x!="msrajawat"):
        print("enter valid user name\n")
        continue # if condition is true then its again jump to the x of again ask username
    y =str(input("ENter your password"))
    if(y=="1234"):
        break
print("=========================Access Granted====================")
