#!c:/Python34/python.exe

print("Content-Type: text/html")
print("""
""")
print("<html>")
print("<form action=calc.py>")
print("<table>")
print("<tr><td>First No:</td><td><input type=text name=f></td></tr>")
print("<tr><td>Second No:</td><td><input type=text name=s></td></tr>")
print("<tr><td><input type=submit name=btn value=Add></td><td><input type=submit name=btn value=Subtract></td></tr>")
print("</table></form></html>")