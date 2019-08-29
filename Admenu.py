#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-Type: text/html;charset=utf-8\r\n")

import csv
print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Administer menu</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>관리자 메뉴</h1>
        <div id="adbutton_button">
            <input type="button" value="메뉴 추가" onclick="location.href='Admenu/AD_menu_add.py'">
            <input type="button" value="메뉴 수정 및 삭제" onclick="location.href='Admenu/AD_menu_delete.py'">
            <input type="button" value="이전" onclick="location.href='home.py'" style="
                padding-right:15px;
                padding-left:15px;
            ">
            <br>
            <br>
            <br>
        </div>
    </body>
</html>
''')
