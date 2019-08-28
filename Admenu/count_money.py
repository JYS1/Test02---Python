#!python


import cgi,os
form = cgi.FieldStorage()
title = form["pageId"].value
money = form["price"].value

opened_file = open('money', 'a', encoding='utf-8')
opened_file.write(money +',')

open_name = open('menu_name', 'a', encoding='utf-8')
open_name.write(title + ',')
open_name.close()


print("Location: order.py")
print()
