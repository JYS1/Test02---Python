#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-Type: text/html;charset=utf-8\r\n")

import os

print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Menu Add</title>
    </head>
    <body>
        <h1>메뉴 등록</h1>
        <form action="save_menu.py" method="post">
            <p><input type="file" name="title"></p>
            <p><input type="int" name="price" placeholder="가격">
            <p><input type="submit"></p>
        </form>
            <input type="button" value="이전" onclick="location.href='../Admenu.py'">
    </body>
</html>
''')
