import json

# 读取json文件
data = {
    1: {2: 3},
    4: 5,
    6: [7, 8, 9, 10]
}
# dict 转换为 json
# dump str 转换为字符串 ensure_ascii 中文
json_str = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4)
print(json_str)
# dump 转换为文件的格式
with open('./data/json模块.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, sort_keys=True, ensure_ascii=False, indent=4)

# 读取 json 字符串
# json load + str
json_dict = json.loads(json_str)
print(json_dict)

# 读取文件
with open('./data/json模块.json', 'r', encoding='UTF-8') as file:
    json_dict = json.load(file)
print(json_dict)
