#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-Type: text/html;charset=utf-8\r\n")

m = open('menu_name', mode='r', encoding='utf-8')
q = m.read().split(',')
b = len(q)
i = 0
while i<b:
    print(q[i])
    i = i + 1

f = open('money', mode='r', encoding='utf-8')
s = f.read().split(',')
print(s[0])
print(s[1])
