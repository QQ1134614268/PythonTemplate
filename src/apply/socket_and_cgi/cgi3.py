#!/usr/bin/python3
# coding=utf-8
import cgi;

form = cgi.FieldStorage()
name = form.getvalue("name", "world")
print("Content-type： text/html\n")
print("hello, {}".format(name))
