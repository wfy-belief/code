import requests
import json
from typing import List, Tuple

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66 '
}


def get_page_urls() -> Tuple[List[str], List[Tuple[str, str]]]:
    """
    Returns:
        返回子页面的完整url  id和文件标题组成的（id,title）列表
    """
    with open('./paper_data.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    paper_data = data['data'][0]['items']
    paper_id_title_list = [(item['id'], item['title']) for item in paper_data]
    urls = list(
        map(lambda x: (x[0] + '/' + x[1].replace(' ', '-')), paper_id_title_list))
    host = 'https://www.aminer.cn/pub/'
    urls = list(map(lambda x: host + x, urls))
    return urls, paper_id_title_list


def get_page_cited(paper_id: str = '53e9b945b7602d970453061a',
                   offset: int = 0,
                   size: int = 30) -> str:
    """
    Args:
        paper_id:当前文章页面的唯一标识 id 字段
        offset: 爬取该文章，被引用文章的信息 起始位置
        size: 获取多少条数据

    Returns:
        返回json字符串数据
    """
    post_data = [{
        "action": "publication.CitedByPid",
        "parameters": {
            "ids": [paper_id],
            "offset": offset, "size": size}}]
    url = 'https://apiv2.aminer.cn/magic?a=getCited__publication.CitedByPid___'

    responses = requests.post(url=url,
                              headers=headers,
                              json=post_data)
    return responses.text


def get_page_reference(paper_id: str = '53e9b945b7602d970453061a',
                       offset: int = 0,
                       size: int = 30) -> str:
    """
    Args:
        paper_id:当前文章页面的唯一标识 id 字段
        offset:获取参考文献信息的起始位置
        size:获取多少条参考文献信息

    Returns:
        包含引用信息的json字符串
    """
    url = f'https://api.aminer.cn/api/pub/ref/{paper_id}/offset/{offset}/size/{size}'
    responses = requests.get(url=url,
                             headers=headers, )
    return responses.text


def get_main_page(url: str = None) -> str:
    responses = requests.get(url=url,
                             headers=headers)
    return responses.text
