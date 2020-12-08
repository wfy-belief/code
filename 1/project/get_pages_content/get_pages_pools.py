# -*- coding:utf-8 -*-
import json
import os
import re
from multiprocessing import Pool

import requests

from get_page_info import get_main_page_info


def get_links():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'
    }
    links = []
    all_money_info = []
    for i in range(1, 21):
        url = f'http://172.20.150.50:40000/wuyou/{i}'
        response = requests.get(url=url, headers=headers)
        content = response.content.decode('utf-8')
        page_links = re.findall(r'<a.*?(/wuyou/detail/\d+).*?</a>', content)
        money = re.findall(r'<span class="t4">([\s\S]*?)</', content)
        money_info = list(map(lambda x: re.sub(r'[\s]*', '', x), money))[1:]

        all_money_info += money_info
        # 存在重复数据
        links += page_links[::2]

    links = list(map(lambda x: 'http://172.20.150.50:40000' + x, links))

    # 有重复信息
    # links = list(set(links))
    # links.sort()

    # print(*links, sep='\n')
    return links, all_money_info
# 执行多线程

def more_var(vars):
    '''
    多变量函数
    '''
    link = vars[0]
    money = vars[1]
    return get_main_page_info(link, money)
if __name__ == "__main__":
    print(os.getcwd())
    links, all_money_info = get_links()
    vars = list(zip(links, all_money_info))
    ans = []
    pool = Pool()
    ans = pool.map(more_var, vars)
    data = {
        'data': ans
    }
    print(os.getcwd())
    with open('../../data/json/page_data_codecopy.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
