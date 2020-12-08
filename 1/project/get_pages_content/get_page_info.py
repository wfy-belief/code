import requests
import re


def get_main_page_info(url, money):
    # print(url)
    '''
    传递一个url和对应公司的工资，返回json数据
    '''
    only_id = re.findall('detail/(\d+)', url)[0]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'
    }

    response = requests.get(url=url, headers=headers)
    content = response.content.decode('utf-8')

    # 职位名字
    while not re.findall(r'<h1 title="(.*?)">', content):
        response = requests.get(url=url, headers=headers)
        content = response.content.decode('utf-8')
    name = re.findall(r'<h1 title="(.*?)">', content)[0]
    # 职位位置，工作经验，需求人视，发布时间
    info = re.findall(r'<p class="msg ltype" title="(.*?)">', content)[0]
    location, job_year, person_num, time = info.split(
        '&#160;&#160;|&#160;&#160;')

    # [\s\S] 否则换行符无法匹配
    job_info = re.findall(
        r'<div class="bmsg job_msg inbox">([\s\S]*?)<div', content)[0]
    # 数据清洗，去除空白符换行符或者 '<br>'
    job_info = re.sub(r'\s*|<br>|[;&]|nbsp', '', job_info)

    # 职能类别
    job_class = re.findall(r'el tdn[\s\S]*?>([\s\S]*?)</a>', content)
    job_class_info = re.sub(r'\s*', '', job_class[0])

    # 联系方式 上班地址
    contact = re.findall(r'上班地址：</span>([\s\S]*?)</', content)
    contact_info = re.sub(r'\s*', '', contact[0])

    # 公司信息
    company = re.findall(r'tmsg inbox">([\s\S]*?)</div>', content)
    company_info = re.sub(r'\s*|<br>|[;&]|nbsp', '', company[0])

    data = {
        "ID": only_id,
        "职位名称": name,
        "薪资": money,
        "工作地区": location,
        "工作经验": job_year,
        "需求人数": person_num,
        "发布时间": time,
        "职位信息": job_info,
        "职能类别": job_class_info,
        "上班地址": contact_info,
        "公司信息": company_info,
    }

    # json_format = json.dumps(
    #    data, indent=4, sort_keys=False, ensure_ascii=False)
    # print(json_format)
    return data


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
