# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pandas as pd
import os


def get_html_info(html):
    '''''
    *****************获取网页的有用信息并保存成字典形式****************
    '''
    try:
        soup = BeautifulSoup(html, "lxml")  # 设置解析器为“lxml”
        # 选择‘div.fixed-inner-box’下h1内的数据的第一个元素
        occ_name = soup.select('div.fixed-inner-box h1')[0]
        # 选择‘div.fixed-inner-box’下h2内的数据的第一个元素
        com_name = soup.select('div.fixed-inner-box h2 ')[0]
        # 选择‘div.welfare-tab-box’内的数据的第一个元素
        welfare = soup.select('div.welfare-tab-box')[0]
        # 选择‘div.terminalpage-left’下strong内的数据的第一个元素
        wages = soup.select('div.terminalpage-left strong')[0]
        # 选择‘div.terminalpage-left’下strong内的数据的第三个元素
        date = soup.select('div.terminalpage-left strong')[2]
        # 选择‘div.terminalpage-left’下strong内的数据的第五个元素
        exper = soup.select('div.terminalpage-left strong')[4]
        # 选择‘div.terminalpage-left’下strong内的数据的第七个元素
        num = soup.select('div.terminalpage-left strong')[6]
        # 选择‘div.terminalpage-left’下strong内的数据的第二个元素
        area = soup.select('div.terminalpage-left strong')[1]
        # 选择‘div.terminalpage-left’下strong内的数据的第四个元素
        nature = soup.select('div.terminalpage-left strong')[3]
        # 选择‘div.terminalpage-left’下strong内的数据的第六个元素
        Edu = soup.select('div.terminalpage-left strong')[5]
        # 选择‘div.terminalpage-left’下strong内的数据的第八个元素
        cate = soup.select('div.terminalpage-left strong')[7]
        # 选择‘ul.terminal-ul.clearfix’下li下strong内的数据的第九个元素
        com_scale = soup.select('ul.terminal-ul.clearfix li strong')[8]
        # 选择‘ul.terminal-ul.clearfix’下li下strong内的数据的第十个元素
        com_nature = soup.select('ul.terminal-ul.clearfix li strong')[9]
        # 选择‘ul.terminal-ul.clearfix’下li下strong内的数据的第十一个元素
        com_cate = soup.select('ul.terminal-ul.clearfix li strong')[10]
        # 选择‘div.fixed-inner-box’下h2内<a></a>内的数据的第一个元素
        com_url = soup.select('div.fixed-inner-box h2 a')[0]
        # 选择‘ul.terminal-ul.clearfix’下li下strong内的数据的最后一个元素
        com_address = soup.select('ul.terminal-ul.clearfix li strong')[-1]
        # 选择‘div.tab-inner-cont’下的数据的第一个元素
        job_descritions1 = soup.select('div.tab-inner-cont')[0]
        # 选择job_descritions1内p内的数据的除最后一个元素外的所有元素
        job_descritions = job_descritions1.select('p')[:-1]
        data = {
            "工作名称": occ_name.text.strip(),  # 选择occ_name内的文本数据并跳过空
            "公司名称": com_name.text,  # 选择com_name内文本数据
            "公司网址": com_url.get('href'),  # 获得网址
            "福利": welfare.text.strip(),  # 选择welfare内的文本数据并跳过空
            "月工资": wages.text.strip(),  # 选择wages内的文本数据并跳过空
            "发布日期": date.text.strip(),  # 选择data内的文本数据并跳过空
            "经验": exper.text.strip(),  # 选择exper内的文本数据并跳过空
            "人数": num.text.strip(),  # 选择num内的文本数据并跳过空
            "工作地点": area.text.strip(),  # 选择area内的文本数据并跳过空
            "工作性质": nature.text.strip(),  # 选择nature内的文本数据并跳过空
            "最低学历": Edu.text.strip(),  # 选择Edu内的文本数据并跳过空
            "职位类别": cate.text.strip(),  # 选择cate内的文本数据并跳过空
            "公司规模": com_scale.text.strip(),  # 选择com_scale内的文本数据并跳过空
            "公司性质": com_nature.text.strip(),  # 选择com_nature内的文本数据并跳过空
            "公司行业": com_cate.text.strip(),  # 选择com_cate内的文本数据并跳过空
            "公司地址": com_address.text.strip(),  # 选择com_address内的文本数据并跳过空
            # 选择job_descrition内的每个元素的文本数据并跳过空
            "岗位描述": [job_descrition.text.strip() for job_descrition in job_descritions],

        }
        # print(data)
        return (data)  # 返回data
    except Exception:
        pass  # 如果有异常则跳过

# 将全部信息保存成DataFrame形式，去除无用信息


def get_htmls_all_info(path):
    df = pd.DataFrame({

        "工作名称": [],
        "公司名称": [],
        "公司网址": [],
        "福利": [],
        "月工资": [],
        "发布日期": [],
        "经验": [],
        "人数": [],
        "工作地点": [],
        "工作性质": [],
        "最低学历": [],
        "职位类别": [],
        "公司规模": [],
        "公司性质": [],
        "公司行业": [],
        "公司地址": [],
        "岗位描述": [],

    })
    dirs = os.listdir(path)  # 返回path文件夹包含的文件或文件夹的名字的列表。
    for dir in dirs:
        # print(dir)
        if dir.find('swp'):  # 如果找到'swo'
            dir = dir.strip('.' and '.swp')  # 跳过'.'和'.swp'
        p = os.path.join(path, dir)  # 拼接路径path和dir
        html = open(p, encoding='UTF-8').read()  # 用'UTF-8'编码读取文件p
        data = get_html_info(html)  # 获取网页的有用信息并保存成字典形式
        print(data)  # 输出data
        df = df.append(data, ignore_index=True)  # 将data添加到df，忽略标签
    return df


if __name__ == '__main__':
    pass
    '''
    path = 'C:\data\python_pj2\jobs.zhaopin.com'  # 设置文件存储位置
    df = get_htmls_all_info(path)
    df.to_csv('C:\data\python_pj2\bigdata', index=False)  # 输出为csv文件
    print(df)  # 输出df
    '''