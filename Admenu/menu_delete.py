#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-Type: text/html;charset=utf-8\r\n")
import cgi, os, view ,html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    price = open('menu/'+pageId, 'r', encoding='utf-8').read()
    title = sanitizer.sanitize(title)
    price = sanitizer.sanitize(price)
    update_link = '<a href="update.py?id={}">수정</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value={}>
            <input type="submit" value="삭제">
        </form>
    '''.format(pageId)
else:
    title = pageId = '삭제'
    price = '삭제 할 메뉴를 선택해 주세요'
    update_link=''
    delete_action=''

print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Delete menu</title>
        <link rel="stylesheet" href="AD.css">
    </head>
    <body>
    <h2>메뉴 수정 & 삭제</h2>
    <div id="grid">
        <ul>
            {listStr}
        </ul>
        <div id="menu">
                <p>메뉴 가격: {desc}</p>
                <p>{update_link}</p>
                <p>{delete_action}</p>
                <input type="button" value="이전" onclick="location.href='../Admenu.py'">
        </div>
        <div style="text-align:center;">
            사진
            <img src="coffee_image/{title}.jpg" width=100%
            style="margin-top:10px;">
        </div>

    </div>
    </body>
</html>
'''.format(title=title,
    listStr=view.getList(),
    desc=price,
    update_link=update_link,
    delete_action=delete_action))
