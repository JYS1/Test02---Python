#!python

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
price = form['price'].value

opened_file = open('menu/'+pageId, 'w', encoding='utf-8')
opened_file.write(price)
opened_file.close()

os.rename('menu/'+pageId, 'menu/'+title[:-4])


#Redirection
print("Location: menu_delete.py")
print()
