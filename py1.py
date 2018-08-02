import re
import urllib.request

page = 2
url = 'https://www.qiushibaike.com/8hr/page/'+str(page)+'/'
headers = ('User-Agent','Mozilla/5.0 (Windows NT 12.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.1453.94 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode('utf-8')
#data = urllib.request.urlopen(url).read()
userpat = 'target="_blank"title="(.*?)">'
contentpat = '<div class="content">(.*?)</div>'
userlist = re.compile(userpat,re.S).findall(data)
contentlist = re.compile(contentpat,re.S).findall(data)
x = 1
for content in contentlist:
    content = content.replace("╲n","")
    name = "content" + str(x)
    #exec(name+'=content')
    print(content)
    x += 1
y = 1
for user in userlist:
    name = 'content'+str(y)
    #with open(user,'w') as f:
        #f.write()
    print('user:'+str(page)+user)
    print('内容是:')
    exec("print("+name+")")
    print("\n")
    y += 1
