import pymysql
db=pymysql.connect(host='localhost',
    user='root',password='123',db='companydatabase')
cmd=db.cursor();
id=input('Enter Employee Id U Want to Search:')
q="Select * from customers where customerid={0}".format(id)
cmd.execute(q)
row=cmd.fetchone()
if(row==None):
    print('Record Not Found...')
else:
       for col in row:
          print(col,end=',')
