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
        <title>주문</title>
        <style>
            table{
                width:100%;
            }
            table, th, td{
                border: 1px solid;
            }
        </style>
    </head>
    <body>
        <table>
            <caption>주   문<caption>
            <thead>
                <tr>
                    <th>커피이름</th>
                    <th>가격</th>
                    <th>선택</th>
                </tr>
            </thead>
            <tbody>
                
            </tbody>
        </table>
    </body>
</html>
''')
