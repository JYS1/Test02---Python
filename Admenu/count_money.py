#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
'''위에 부분만 넣으면 링크를 한글로 읽을수 있다.'''
import cgi,os
form = cgi.FieldStorage()
title = form["pageId"].value
money = form["price"].value

opened_file = open('order_money', 'a', encoding='utf-8')
opened_file.write(money +',')

open_name = open('order_name', 'a', encoding='utf-8')
open_name.write(title + ',')
open_name.close()


print("Location: order.py?id={}".format(title))
print()


'''
주문 내역 저장하는곳으로 보내주는것
'''
