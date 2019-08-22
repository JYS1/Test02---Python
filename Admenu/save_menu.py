#!python

import cgi
form = cgi.FieldStorage()
name = form["title"].value
title = form["title"].value
price = form['price'].value
photo = form['photo'].value

opened_file = open('menu.txt', 'a', encoding='utf-8')
opened_file.write(name + ',')
opened_file.write(title + ',')
opened_file.write(price + ',')
opened_file.write(photo + ','+'\n')

open_menu = open('menu.py', 'a', encoding='utf-8')
open_menu.write('print(s[i])'+'\n')
open_menu.write('i += 4' + '\n')

print("Location: menu_add.py")
print()
