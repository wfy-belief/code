import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts

ALL_DATA = []


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')

    soup = BeautifulSoup(text, 'lxml')
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            if index == 0:
                city_td = tds[1]
            city_td = tds[0]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'city': city, 'min_temp': int(min_temp)})


def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml'
    ]
    # url = 'http://www.weather.com.cn/textFC/gat.shtml'
    for url in urls:
        parse_page(url)

    ALL_DATA.sort(key=lambda x: x['min_temp'])
    # print(ALL_DATA)
    data = ALL_DATA[0:10]

    cities = list(map(lambda x: x['city'], data))
    temps = list(map(lambda x: int(x['min_temp']), data))
    print(cities)
    print(temps)
    chart = (
        Bar()
            .add_xaxis(cities)
            .add_yaxis("温度", temps)
            .set_global_opts(title_opts=opts.TitleOpts(title="中国天气最低气温排行榜"),
                             # xaxis_opts=opts.AxisOpts(position='top'),
                             yaxis_opts=opts.AxisOpts(is_inverse=True)
                             )
            # .set_series_opts(label_opts=opts.LabelOpts(is_show=False)
            .render("temp.html")
    )


if __name__ == '__main__':
    main()
