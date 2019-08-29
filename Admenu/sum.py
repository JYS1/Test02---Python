#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-Type: text/html;charset=utf-8\r\n")

name = open('order_name', mode='r', encoding='utf-8')
money = open('order_money', mode='r', encoding='utf-8')

name_split = name.read().split(',')
money_split = money.read().split(',')
name_split.remove('\n')

name_len = len(name_split)
money_len = len(money_split)

print('<br>')
w_count = {}
for list in name_split:
    try: w_count[list] += 1
    except: w_count[list] =1
print(w_count)
print('<br>')
print('''<input type="button" value="이전"onclick="location.href='order.py'"style="
margin-top: 20px;
margin-right: 10px;">
''')
j = 0
sum = 0
while j < money_len:
    sum = sum + (int(money_split[j]))
    j = j + 1
    if j == money_len-1:
        print('총합계 : ',sum)

'''
리스트 중복 체크 하는방법
w_count = {}
for list in name_split:
    try: w_count[list] += 1
    except: w_count[list] =1
print(w_count)
print('<br>')
counter=collections.Counter(name_split)
print(counter.values())
print('<br>')
'''
'''
참고 자료 순서대로 읽는것 + 숫자 더하기
m = open('order_name', mode='r', encoding='utf-8')
q = m.read().split(',')
b = len(q)
i = 0
while i<b:
    print(q[i])
    i = i + 1

print(int(money_split[1])+int(money_split[2]))
'''
