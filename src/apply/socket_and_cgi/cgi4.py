#!/usr/bin/python3
# coding=utf-8
import cgi;

form = cgi.FieldStorage()
name = form.getvalue("name", "world")
print("""Content-type： text/html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Greeeting</title>
</head>
<body>
    <h1>hello,{}</h1>
<form action="cgi4.py">
    change name<input type="text" name="name"/>
    <input type="submit"/>
</form>
</body>
</html>""".format(name))
