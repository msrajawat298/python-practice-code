import pymysql
db=pymysql.connect(host='localhost',
    user='root',password='123',db='companydatabase')
cmd=db.cursor();
pat=input('Enter Pattern:')
q="Select * from customers where customername like '%{0}%'".format(pat)
cmd.execute(q)
rows=cmd.fetchall();
if(rows==None):
    print('Record Not Found...')
else:
     for row in rows:
      #print(row[0],row[1])
      for col in row:
          print(col,end=',')
      print()