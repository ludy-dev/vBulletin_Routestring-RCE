import re
import requests
import sys
import os

def exploit(dst_addr):
        vuln_list =("/_async/AsyncResponseService", "/wls-wsat/CoordinatorPortType")
        URL="http://"+dst_addr

        for i in vuln_list:
                print(URL+i)
                res = requests.get(URL+i, verify=False)
                response = res.text
                print("Status Code : %d"% res.status_code)

                p = re.compile('elcome|eb')
                m = p.match(response)
                if m:
                        print("Vuln Found")
                else:
                        print("Not Found")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		   sys.argv.append('80')
	elif len(sys.argv) < 3:
			print('Usage: python %s <dst_ip> <dst_port>' % os.path.basename(sys.argv[0]))
			sys.exit()
	
	address =(sys.argv[1], sys.argv[2])
	dst_addr=":".join(address)
	exploit(dst_addr)
