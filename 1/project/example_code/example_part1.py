import urllib.request
from urllib.parse import *
from bs4 import BeautifulSoup
import string
import random
import os
headers = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; rv:27.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:27.0) Gecko/20100101 Firfox/27.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:10.0) Gecko/20100101 Firfox/10.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/21.0.1180.110 Safari/537.36"
    "Mozilla/5.0 (X11; Ubuntu; Linux i686 rv:10.0) Gecko/20100101 Firfox/27.0"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/34.0.1838.2 Safari/537.36"
    "Mozilla/5.0 (X11; Ubuntu; Linux i686 rv:27.0) Gecko/20100101 Firfox/27.0"
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
]


def get_content(url, headers):
    # @url：需要登录的网址
    # @headers：模拟的登陆的终端
    # *********************模拟登陆获取网址********************

    random_header = random.choice(headers)  # 随机选取hearder中的一个元素
    req = urllib.request.Request(url)  # 构建请求对象
    req.add_header("User-Agent", random_header)  # 添加报头
    req.add_header("Host", "172.20.150.50:40000")  # 添加Host
    try:
        html = urllib.request.urlopen(req)  # 获取网页源代码
        contents = html.read()  # 将网页源代码赋值给contents
        if isinstance(contents, bytes):  # 判断contents是否为bytes类型
            contents = contents.decode('utf-8')  # 对contents解码，解码方式为‘utf-8’
        else:
            # 如果不是bytes类型则输出'service mysql restart'
            print('service mysql restart')
        return (contents)  # 返回解码后的contents
    except Exception as e:
        print(e)  # 如果有异常则抛出异常


def get_links_from(page):
    # @page：表示第几页信息
    # @urls：所有列表的超链接，即子页网址
    # ****************此网站需要模拟登陆**********************
    # 返回全部子网页地址
    urls = []
    for i in range(1, page):
        # 通过format函数对网页地址进行映射
        url = 'http://172.20.150.50:40000/wuyou/{0}'.format(i)
        url = quote(url, safe=string.printable)  # 对网址中特殊符号进行编码
        info = get_content(url, headers)  # 获取网页信息
        soup = BeautifulSoup(info, "lxml")  # 用BeautifulSoup和lxml解析器对网页源代码进行解析
        # 选择div dw_table div e1 span内<a a>
        link_urls = soup.select('div.dw_table div.el span.t2 a')
        for url in link_urls:
            oneurl = "http://172.20.150.50:40000"+url.get('href')  # 获取页面
            urls.append(oneurl)  # 将获取的页面存储到列表urls中
    # print(urls)
    return (urls)


def get_recuite_info(page):
    # 获取网页信息
    urls = get_links_from(page)  # 获得每页信息
    path = '/data/zhaopin/'  # 设定存储位置
    if os.path.exists(path) == False:
        os.makedirs(path)  # 如果path不存在则新建path
    for url in urls:
        print(url)  # 输出网址
        file = url.split('/')[-1]  # 用'/'分割并取最后一个元素
        print(file)  # 输出网址最后一位
        str = url.split('/')[2].split('.')[0]  # 先用'/'分割取第三个元素，再将元素用'.'分割取第一个元素
        print(str)
        html = get_content(url, headers)  # 获取网页信息
        if html != None and file != '':  # 如果html不为空且file不为空
            with open(path+file, 'w') as f:  # 打开path_file文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                f.write(html)  # 将获取的网页信息html写入文件


# *********************获取信息***************************
if __name__ == '__main__':
    pass
    # get_recuite_info(20)
