#!c:/Python34/python.exe
import cgi
print("Content-Type: text/html")
print("""
""")
req=cgi.FieldStorage();
p=int(req.getvalue("p"))
c=int(req.getvalue("c"))
m=int(req.getvalue("m"))
t=p+c+m;
p=t/3;
div=''
if(p>=60 and p<=100):
     div='First'
elif(p>=48 and p<=59.99):
     div='Second'
elif(p>=35 and p<=47.99):
     div='Thrid'
else:
     div='Fail'

print("<html>")
print("<table border=1>")
print("<tr><th>Code</th><th>Subject</th><th>Min</th><th>Max</th><th>Marks<br>Obtained</th></tr>");
print("<tr><td>011<br>022<br>033</td><td>Physics<br>Chemistry<br>Maths</td><td>35<br>35<br>35</td><td>100<br>100<br>100</td><td>%r<br>%r<br>%r</td>" %(p,c,m))
print("<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp</td><td>Total:</td><td>%r</td>" %(t))

print("<tr><td>Percentage:</td><td>%r</td><td>&nbsp</td><td>Division:</td><td>%r</td>" %(p,div))

print("</table>")













