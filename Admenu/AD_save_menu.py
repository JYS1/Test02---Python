#!python

import cgi,os
form = cgi.FieldStorage()
title = form["title"].value
price = form['price'].value

opened_file = open('menu/'+title[:-4], 'w', encoding='utf-8')
opened_file.write(price)
opened_file.close()


print("Location: AD_menu_add.py")
print()
