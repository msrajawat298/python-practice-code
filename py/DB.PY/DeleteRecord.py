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
    print('Customer Id:',row[0])
    print('Name:', row[1])
    print('City:', row[2])
    print('Mobile:', row[3])
    print('Amount Paid :', row[4])
    print('Paid:', row[5])
    ch=input('Sure to Remove Above Record y/n?')
    if(ch=='y'):
        q='delete from customers where customerid={0}'.format(id)
        cmd.execute(q)
        db.commit()
        print('Record Deleted....')



