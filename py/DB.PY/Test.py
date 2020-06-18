import  pymysql
db=pymysql.connect(host='localhost',
    user='root',password='123',db='companydatabase')
cmd=db.cursor();
query='select * from employees'
cmd.execute(query)
rows=cmd.fetchall()
for row in rows:
 print(row[0],row[1],row[2])
