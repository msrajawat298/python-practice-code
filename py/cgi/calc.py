#!c:/Python34/python.exe
import  cgi
print("Content-Type: text/html")
print("""
""")
req=cgi.FieldStorage()
f=int(req.getvalue('f'));
s=int(req.getvalue('s'));
btn=req.getvalue('btn');
if(btn=='Add'):
    c=f+s
else:
    c=f-s

print("<html>")
print("Result:",c)
print("</html>")