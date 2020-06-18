#use of smtplib module
#The smtplib module defines an SMTP client session object that can be used to
#send mail to any Internet machine with an SMTP or ESMTP listener daemon.
#For details of SMTP and ESMTP operation, consult RFC 821
#(Simple Mail Transfer Protocol) and RFC 1869 (SMTP Service Extensions)
https://docs.python.org/3/library/smtplib.html#module-smtplib
import smtplib

connection =smtplib.SMTP('smtp.gmail.com' , 587)
connection.ehlo()
connection.starttls()
connection.login('amanbaj1230@gmail.com','qwerty1234@')
connection.sendmail('amanbaj1230@gmail.com' , 'amanbaj1230@gmail.com' , 'u hacked')
connection.quit()
