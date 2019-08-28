#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-Type: text/html;charset=utf-8\r\n")
print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>HOME</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>선택 메뉴</h1>
        <div id="home_button">
            <input type="button" value="주문" onclick="location.href='Admenu/order.py'" style="
                padding-right:23px;
                padding-left:23px;
            ">
            <input type="button" value="관리자메뉴" onclick="location.href='Admenu.py'">
        </div>
        <img src="home_coffee.jpg" class="home_coffee_image">
    </body>
</html>
''')
