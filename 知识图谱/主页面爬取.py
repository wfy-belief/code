import requests
import json
post_body = [
    {"action": "searchapi.SearchPubsCommon",
     "parameters": {
         "offset": 0,
         "size": 1000,
         "searchType": "all",
         "switches": ["lang_zh"],
         "aggregation":["year", "author_year"],
         "query":"Cyberspace security",
         "year_interval":1
     },
     "schema":{
         "publication": ["id",
                         "year",
                         "title",
                         "title_zh",
                         "abstract",
                         "abstract_zh",
                         "authors",
                         "authors._id",
                         "authors.name",
                         "keywords",
                         "authors.name_zh",
                         "num_citation",
                         "num_viewed",
                         "num_starred",
                         "num_upvoted",
                         "is_starring",
                         "is_upvoted",
                         "is_downvoted",
                         "venue.info.name",
                         "venue.volume",
                         "venue.info.name_zh",
                         "venue.info.publisher",
                         "venue.issue",
                         "pages.start",
                         "pages.end",
                         "lang",
                         "pdf",
                         "ppt",
                         "doi",
                         "urls",
                         "flags",
                         "resources"]}}]

# https://www.aminer.cn/search/pub?q=Cyberspace%20security&t=b
url = 'https://apiv2.aminer.cn/n?a=SEARCH__searchapi.SearchPubsCommon___'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}
# data=json.dumps(post_body)
# json=post_body
# print(json.dumps(post_body), type(json.dumps(post_body)))
response = requests.post(url=url, headers=headers, json=post_body)
print(response.status_code)

# print(response.content.decode('utf-8'))
json_str = response.content.decode('utf-8')
json_str = json.loads(json_str)
json_format = json.dumps(
    json_str, indent=4, sort_keys=True, ensure_ascii=False)
# print(json_format)

with open('./paper_data.json', 'w', encoding='utf-8') as file:
    json.dump(json_str, file, indent=4, ensure_ascii=False)
