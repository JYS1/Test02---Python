#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-Type: text/html;charset=utf-8\r\n")
import cgi, os, AD_view

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    price = open('menu/'+pageId, 'r', encoding='utf-8').read()
else:
    title = pageId = ''
    price = ''
print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Update menu</title>
    </head>
    <body>
    <h2>메뉴 수정</h2>
    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}">
        현재 커피 : <input type="text" readonly="pageId"
        value="{form_default_title}" style="
        width:85px;
        height:18px;
        ">
        <p><input type="file" name="title" value="{form_default_title}"></p>
        <p><input type="text" name="price" placeholder="price" value="{form_default_price}"></p>
        <p><input type="submit"></p>
    </form>
    </body>
</html>
'''.format(title=title,
    listStr=AD_view.getList(),
    desc=price,form_default_title=pageId , form_default_price=price))
