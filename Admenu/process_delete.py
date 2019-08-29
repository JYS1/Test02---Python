#!python
'''관리자 메뉴에서 메뉴 삭제 할때 실행되는것.'''
import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('menu/'+pageId)

#Redirection
print("Location: AD_menu_delete.py")
print()
