import  pymysql
db=pymysql.connect(host='localhost',user='root',password='1234',db='student')
cmd=db.cursor();
query='create table customers(customerid numeric(5) primary key,customername varchar(20),city varchar(20),mobileno varchar(15),totalamt numeric(10),amtpaid numeric(10))'
cmd.execute(query)
print('Table Created')
