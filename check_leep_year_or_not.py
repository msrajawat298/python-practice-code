y=int(input("Enter the Year to check Leap or Not : "))

if y%4==0 and y%100!=0 or y%400==0:
    print("\tEnter year Leap year")
else:
    print("\tEnter year Not Leap year")
