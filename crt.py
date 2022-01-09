#pwn3d
import requests,sys,re
r=sys.argv[1]
crt="https://crt.sh/?q=%s"%r
req=requests.get(crt).text
regex=re.findall('[\w\-\.]*%s'%r,req)
for i in regex:
	print(i)
