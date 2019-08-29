#!python
'''관리자 메뉴에서 메뉴 수정할때 사용하는것.'''
import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
price = form['price'].value

opened_file = open('menu/'+pageId, 'w', encoding='utf-8')
opened_file.write(price)
opened_file.close()

os.rename('menu/'+pageId, 'menu/'+title[:-4])
'''타이틀뒤에 -4를 넣는것은 .jpg때문에'''

#Redirection
print("Location: AD_menu_delete.py")
print()
