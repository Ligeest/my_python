print('ssssssssssssss')
import re
import urllib.request

page = 2
url = 'http://www.qiushibaie.com/8hr/page/'+str(page)+'/'
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1')
opener = urllib.request.build_opener()
#opener.addheaders = [headers]
urllib.request.install_opener(opener)
#data = urllib.request.urlopen(url).read().decode('utf-8')
data = urllib.request.urlopen(url).read()
print(data)
userpat = 'target="_blank"title="(.*?)">'
contentpat = '<div class="content">(.*?)</div>'
serlist = re.compile(userpat,re.S).findall(data)
contentlist = re.compile(contentpat,re.S).findall(data)
x = 1
for content in contentlist:
    content = content.replace("╲n","")
    name = "content" + str(x)
    exec(name+'=content')
    x += 1
y = 1
for user in userlist:
    name = 'content'+str(y)
    #with open(user,'w') as f:
        #f.write()
    print('user:'+str(page)+user)
    print('sfg43y34sb2452')
    exec("print("+name+")")
    print("\n")
    y += 1





        

