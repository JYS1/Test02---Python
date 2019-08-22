#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import cgi ,os
form = cgi.FieldStorage()
title = open('save_menu.py', 'r', encoding='utf-8').read()

print("Content-Type: text/html;charset=utf-8\r\n")
print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Delete menu</title>
    </head>
    <body>
    <h2>메뉴 삭제</h2>
        {title}
    </body>
</html>
'''.format(title = title))
