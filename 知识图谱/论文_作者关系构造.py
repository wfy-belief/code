import json
from multiprocessing import Pool
from neo4j_methods import MyNeo4j

my_noe4j = MyNeo4j()


# 清洗数据
# 多线程
def transform(detail_data):
    # 定义文章属性
    paper = {
        'name': detail_data['title'],
        'id': detail_data['id'],
        'abstract': detail_data['abstract'] if 'abstract' in detail_data else 'None',
        'keywords': detail_data['keywords'] if 'keywords' in detail_data else 'None',
        'score': detail_data['score']}
    # 部分数据异常
    # paper['id'] = data['id']
    # 部分数据异常
    # print(paper)
    # 提取作者相关信息，存在不合法数据
    if 'authors' in detail_data:
        for author in detail_data['authors']:
            # name异常值
            if 'name' not in author:
                continue
            # id 异常值
            if 'id' not in author:
                author['id'] = None
            my_noe4j.add_relationship(paper, 'author', {'name': author['name'],
                                                        'id': author['id']}, ['paper'], ['person'])
    return None


if __name__ == '__main__':
    my_noe4j.delete_all()
    with open('./paper_data.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    # print(data['data'][0].keys())
    paper_data = data['data'][0]['items']
    pool = Pool()
    pool.map(transform, paper_data)
