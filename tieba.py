import time
import requests
import re

#UA
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.3282.204 Safari/537.36'}
#正则表达式
pat1 = re.compile('_content ">            '+'(.*?)'+'</div><br>',re.S)
#因为有三页所以循环三次
for page_number in range(1,4):
    page_url = 'https://tieba.baidu.com/p/5329292142?see_lz=1&pn='
    #加上页码
    page_url += str(page_number)
    #访问网页源码
    page_data = requests.get(page_url,headers=head)
    time.sleep(2)
    page_data = page_data.text
    #匹配正则，将内容提取出来
    texts = pat1.findall(page_data)
    #遍历返回的列表
    for text in texts:
        #将标签换成换行符
        text_new = text.replace('<br>','\n')
        #以追加模式写入文件
        with open('novel.txt','a',encoding='utf-8')as f:
            f.write(text_new)