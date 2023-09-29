import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url=input('Enter：')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

tree = ET.fromstring(data)
sum=0
lst=tree.findall('comments/comment')
for item in lst:
    count = item.find('count').text
    value=int(count)
    sum=sum+value
print('sum=',sum)
