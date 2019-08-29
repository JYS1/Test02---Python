#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-Type: text/html;charset=utf-8\r\n")
import cgi, os, menu_view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    price = open('menu/'+pageId, 'r', encoding='utf-8').read()
    title = sanitizer.sanitize(title)
    price = sanitizer.sanitize(price)
    count_money = '''
        <form action="count_money.py" method="post">
            <input type="hidden" name="pageId" value={}>
            <input type="hidden" name="price" value={}>
            <input type="submit" value="+">
        </from>
    '''.format(pageId,price)
else:
    title = pageId = '주문'
    price = '주문할 메뉴를 선택해 주세요.'
    count_money =''
print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>주문</title>
        <link rel="stylesheet" href="order.css">
    </head>
    <body>
        <div id="grid">
            <ul>
                {listStr}
            </ul>
                <img src="coffee_image/{title}.jpg">
            <div id="text">
                가격 : {price}<br>
                추가  {count_money}
            </div>
        </div>
        <input type="button" value="이전"  onclick="location.href='../home.py'">
    </body>
</html>
'''.format(title=title,
        price=price,
        listStr=menu_view.getList(),
        count_money=count_money))
print('<br>')
print('<br>')
name = open('order_name', mode='r', encoding='utf-8')
money = open('order_money', mode='r', encoding='utf-8')

name_split = name.read().split(',')
money_split = money.read().split(',')

name_len = len(name_split)
money_len = len(money_split)
print('<br>')
w_count = {}
for list in name_split:
    try: w_count[list] += 1
    except: w_count[list] =1
print('주문 현황 : ', w_count)
print('<br>')
print('<br>')
j = 0
sum = 0
while j < money_len:
    sum = sum + (int(money_split[j]))
    j = j + 1
    if j == money_len-1:
        print('총합계 : ',sum)
