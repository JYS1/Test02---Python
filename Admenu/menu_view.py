import os, html_sanitizer

def getList():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('menu')
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + '<li><a href="order.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
