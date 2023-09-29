import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter：')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)
print('User count:', len(info))
sum=0
for thing in info['comments']:
    num=thing['count']
    print(num)
    sum=sum+num
print(sum)
