import os


def update_file(file_):
    with open(file_, 'r', encoding='UTF-8') as fp:
        print(fp.read())


PATH = os.getcwd()
print(PATH)
for root, dirs, files in os.walk('./'):
    if root == './':
        continue
    # 筛选.py 文件
    files = list(filter(lambda f: f.endswith('.py'), files))
    # print(files)
    # 切换目录
    dir_name = os.path.join(PATH, root)
    os.chdir(dir_name)
    for file in files[:1]:
        update_file(file)
        exec_status_code = os.popen(f'python {file}').readlines()
