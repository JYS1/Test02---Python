#!python

import cgi
form = cgi.FieldStorage()
name = form["title"].value
title = form["title"].value
price = form['price'].value
photo = form['photo'].value

opened_file = open('menu', 'a', encoding='utf-8')
opened_file.write(name + '=[')
opened_file.write(title + ',')
opened_file.write(price + ',')
opened_file.write(photo + ']\n')
print("Location: menu_add.py")
print()
