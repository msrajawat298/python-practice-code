import pymysql
db=pymysql.connect(host='localhost',
    user='root',password='123',db='companydatabase')
cmd=db.cursor();
min=input('Enter Min Amount:')
max=input('Enter Max Amount:')

q="Select * from customers where totalamt between {0} and {1}".format(min,max)
cmd.execute(q)
row=cmd.fetchone()
if(row==None):
    print('Record Not Found...')
else:
     while row!=None:
         for col in row:
             print(col,end=',')
         print()
         row=cmd.fetchone()
