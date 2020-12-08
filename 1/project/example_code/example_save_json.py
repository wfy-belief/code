import json

json_str = {'ssg': 13, 'sgagdsa': [13131, 1313],
            'dsgsg': {'agjaslg': 12346}, 'is_lskg': True}

json_format = json.dumps(json_str, indent=4, sort_keys=True)
print(json_format)

with open('../json/data.json', 'w', encoding='utf-8') as file:
    json.dump(json_str, file, indent=4)
