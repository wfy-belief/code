import json
import os
import re

import requests


def read_file():
    with open('./problem_list.json', 'r', encoding='UTF-8') as file:
        data_ = json.load(file)
        data_ = data_['problemSetProblems']
        file.close()

    return [item['id'] for item in data_]


def get_page_content(id_):
    url = f'https://pintia.cn/api/problem-sets/1111652100718116864/problems/{id_}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.96 '
                      'Safari/537.36 Edg/88.0.705.50 ',
        'Accept': 'application/json;charset=UTF-8'
    }
    responses = requests.get(
        url=url,
        headers=headers,
    )
    return json.loads(responses.text)


def create_directory():
    if not os.path.exists('./markdown'):
        os.mkdir('./markdown')


def build_file(item):
    label = item['problemSetProblem']['label']
    title = item['problemSetProblem']['title']
    content = item['problemSetProblem']['content']
    score = item['problemSetProblem']['score']
    # 第1章-1 从键盘输入两个数，求它们的和并输出 (30分)
    # 第1章-1 从键盘输入两个数，求它们的和并输出(30分) PTA-python 题解 浙大版《Python 程序设计》题目集
    file_name = label + ' ' + title + f' ({score}分)' + ' PTA-python 题解 浙大版《Python 程序设计》题目集.md'
    # 构造一级标题
    title = '# ' + title + '\n'

    head_info = '''\n> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---\n'''
    thought = '''\n### 思路与视频教程\n**<font color='#e59572'>慢慢完善</font>**\n'''
    code = get_python_code(label)
    python_code = f'''\n### 代码\n```python\n{code}\n```'''

    with open('./markdown/' + file_name, 'w', encoding='UTF-8') as file:
        file.write(head_info)  # 开头语
        file.write(title)  # 标题
        file.write(content)  # 正文
        file.write(thought)  # 思路与视频教程
        file.write(python_code)  # python 代码
        file.close()


def get_python_code(label):
    first, second = re.findall(r'\d+', label)
    file_path = f'../编程题/{first}.{second}.py'
    if not os.path.exists(file_path):
        return ''
    with open(file_path, 'r', encoding='UTF-8') as file:
        content = file.read()
    return content


if __name__ == '__main__':
    data = read_file()
    create_directory()
    for item in data:
        problem = get_page_content(item)
        build_file(problem)
