#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-Type: text/html;charset=utf-8\r\n")
i = 0
f = open('menu.txt', mode='r', encoding='utf-8')
s = f.read().split(',')
print(s[0])
