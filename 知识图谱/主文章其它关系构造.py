import json
from multiprocessing import Pool
from neo4j_methods import MyNeo4j

my_noe4j = MyNeo4j()


def build_relationship(source, relationship, target, target_labels):
    my_noe4j.add_relationship(source, relationship, {'name': target}, ['paper'], target_labels,
                              build_new_nodes=[False, True])


def parse_data(items):
    id_ = items['id']
    source = {'id': id_}
    # property doi
    doi = 'https://doi.org/'
    doi += items['doi'] if 'doi' in items else ''
    # citation num_starred num_upvoted num_viewed
    citation = items['num_citation'] if 'num_citation' in items else ''
    starred = items['num_starred'] if 'num_starred' in items else ''
    up_voted = items['num_upvoted'] if 'num_upvoted' in items else ''
    viewed = items['num_viewed'] if 'num_viewed' in items else ''
    build_relationship(source, 'doi', target=doi, target_labels=['property'])
    build_relationship(source, 'citation', target=citation, target_labels=['property'])
    build_relationship(source, 'starred', target=starred, target_labels=['property'])
    build_relationship(source, 'up_voted', target=up_voted, target_labels=['property'])
    build_relationship(source, 'viewed', target=viewed, target_labels=['property'])
    # index
    pages = items['pages']['end'] if 'pages' in items else ''
    build_relationship(source, 'pages', target=pages, target_labels=['index'])
    if 'venue' in items:
        publish = items['venue']['info'] if 'info' in items['venue'] else {}  # dict
        if 'name' in publish:
            build_relationship(source, 'publish', target=publish['name'], target_labels=['index'])
        else:
            build_relationship(source, 'publish', target='', target_labels=['index'])
        issue = items['venue']['issue'] if 'issue' in items['venue'] else ''
        build_relationship(source, 'issue', target=issue, target_labels=['index'])
        volume = items['venue']['volume'] if 'volume' in items['venue'] else ''
        build_relationship(source, 'volume', target=volume, target_labels=['index'])
    else:
        publish, issue, volume = '', '', ''
        build_relationship(source, 'publish', target=publish, target_labels=['index'])
        build_relationship(source, 'issue', target=issue, target_labels=['index'])
        build_relationship(source, 'volume', target=volume, target_labels=['index'])
    year = items['year'] if '' in items else ''
    build_relationship(source, 'year', target=year, target_labels=['index'])


if __name__ == '__main__':
    with open('./paper_data.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    # print(data['data'][0].keys())
    paper_data = data['data'][0]['items']
    pool = Pool()
    pool.map(parse_data, paper_data)
