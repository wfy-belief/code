# -*- coding:utf-8 -*-
import json
import re

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

if __name__ == "__main__":
    links, all_money_info = get_links()
    data = {
        'data': []
    }
    for url, money in zip(links, all_money_info):
        data['data'].append(get_main_page_info(url=url, money=money))
        print(f'正在处理{url}页面信息')
    with open('../../data/json/page_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

