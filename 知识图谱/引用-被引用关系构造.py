import json
from multiprocessing import Pool
from neo4j_methods import MyNeo4j
# 获取全部网页链接，获取引用和被引用文章的信息
from requests_mothods import get_page_urls, get_page_cited, get_page_reference

# 初始化数据库
my_noe4j = MyNeo4j()


# my_noe4j.delete_all()


def create_reference_relationship(paper_id, name):
    # 查询10条信息
    page_reference = get_page_reference(paper_id=paper_id, size=10)
    page_reference = json.loads(page_reference)

    for reference_info in page_reference['data']:
        # 建立关系
        my_noe4j.add_relationship({'name': name, 'id': paper_id}, 'reference',
                                  {'name': reference_info['title'], 'id': reference_info['id']}, ['paper'],
                                  ['paper', 'references_paper'])
        for author in reference_info['authors']:
            # id 异常值
            if 'id' not in author:
                author['id'] = None
            # 建立引用文献-作者关系
            my_noe4j.add_relationship({'name': reference_info['title'],
                                       'id': reference_info['id']}, 'author', {'name': author['name'],
                                                                               'id': author['id']}, ['paper'],
                                      ['person'])
    return None


def create_cited_relationship(paper_id, name):
    # 查询10条信息
    page_cited = get_page_cited(paper_id=paper_id, size=10)
    page_cited = json.loads(page_cited)
    # 没有被引用信息
    if 'items' not in page_cited['data'][0]:
        # print(paper_id, name)
        return None
    for cited_info in page_cited['data'][0]['items']:
        # 建立引用关系
        my_noe4j.add_relationship({'name': name, 'id': paper_id}, 'cited',
                                  {'name': cited_info['title'], 'id': cited_info['id']}, ['paper'],
                                  ['paper', 'cited_paper'])
        # 建立被引用文献-作者关系
        for author in cited_info['authors']:
            # id 异常值
            if 'id' not in author:
                author['id'] = None

            # 建立引用文献-作者关系
            my_noe4j.add_relationship({'name': cited_info['title'],
                                       'id': cited_info['id']}, 'author', {'name': author['name'],
                                                                           'id': author['id']}, ['paper'], ['person'])
    return None


def pool_reference_cited(data):
    paper_id, name = data[0], data[1]
    create_reference_relationship(paper_id=paper_id, name=name)
    create_cited_relationship(paper_id=paper_id, name=name)


if __name__ == '__main__':
    url_list, id_title_list = get_page_urls()
    pool = Pool()
    pool.map(pool_reference_cited, id_title_list)
