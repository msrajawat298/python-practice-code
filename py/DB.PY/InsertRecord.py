import  pymysql
db=pymysql.connect(host='localhost',
    user='root',password='123',db='companydatabase')
cmd=db.cursor();
cid=input('Enter Customer Id:')
cn=input('Enter Customer Name:')
cc=input('Enter Customer City:')
cmb=input('Enter Customer Mobile Number:')
cta=input('Enter Customer Total Amount:')
cap=input('Enter Customer Amount Paid:')
q="insert into customers values({0},'{1}','{2}','{3}',{4},{5})".format(cid,cn,cc,cmb,cta,cap)
print(q)
cmd.execute(q)
db.commit()
print('Record Submitted')