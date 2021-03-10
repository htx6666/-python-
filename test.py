import os
import re
import time
import random
from urllib import parse
import pyquery
import requests
import threading
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

def get_html(url):
    time.sleep(random.randint(2,6))
    doc=pyquery.PyQuery(url,headers=headers,encoding='gb2312')
    imgs=doc('.title')
    for x in imgs.items():
        href=x('span a').attr('href')
        # get_next_html(href)
        t1=threading.Thread(target=get_next_html,args=[href,])
        t1.start()
        'document.querySelector("body > div.Clbc_Game > div.wrappic > div.pages > ul > li:nth-child(10)")'

    next_page=doc('.pages ul li:nth-last-child(2)')
    end_page=doc('.pages ul li:nth-last-child(1)')

    # 设置递归函数
    #
    time.sleep(random.randint(2, 6))
    if end_page.text()=='末页':
        href=next_page('a').attr('href')

        url=parse.urljoin(url,href)
        get_html(url)


def down_load(path,title,url):
    time.sleep(random.randint(2, 6))
    with open(os.path.join(path,f'{title}.jpg'),'wb')as fp:
        fp.write(requests.get(url,headers=headers).content)
        print(f'{title}__ok!')

def get_next_html(url):
    time.sleep(random.randint(2, 6))
    doc=pyquery.PyQuery(url,headers=headers,encoding='gb2312')
    # print(doc)
    imgs=doc('.down-btn').attr('href')
    title = doc('.wrapper.clearfix.imgtitle h1').text().replace('/','-')
    #找到下一页标签
    next_url = doc('#nl a').attr('href')

    Title=re.sub(r'[(\-)0-9]+','',title)
    print(Title, title, imgs)

    path=os.path.join('images',Title)
    if not os.path.exists(path):
        os.makedirs(path)
    down_load(path,title,imgs)

    #设置递归函数。爬取每一页
    if  next_url!='##':
        url=parse.urljoin(url,next_url)
        get_next_html(url)

def main():
    url = 'https://www.mmonly.cc/tag/cs/'
    get_html(url)


if __name__ == '__main__':
    main()
