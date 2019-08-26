#!python

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('menu/'+pageId)

#Redirection
print("Location: menu_delete.py")
print()
