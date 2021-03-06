# code

code

```git
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/wfy-belief/code.git
git push -u origin main
```

Sync: 上传完成。Gist ID:3f2068e8e192bd0d665ae5e272d8d28b。请复制这个 ID 并将其用于其他设备来下载配置。

账号同步 <https://zhuanlan.zhihu.com/p/137631576>
第一提交到main

**修改一个重大的结构**
调整内容框架,结构树见附件tree.txt

```bash
C:.
|   README.md
|   tree.txt
|   
+---.pytest_cache
|   |   .gitignore
|   |   CACHEDIR.TAG
|   |   README.md
|   |   
|   \---v
|       \---cache
|               stepwise
|               
+---.vscode
|       launch.json
|       settings.json
|       
+---1
|   |   README.md
|   |   
|   +---data
|   |   +---csv
|   |   |       bigdata.csv
|   |   |       bigdata_for_graph.csv
|   |   |       
|   |   \---json
|   |           data.json
|   |           page_data.json
|   |           page_data_codecopy.json
|   |           
|   \---project
|       |   main.py
|       |   __init__.py
|       |   
|       +---example_code
|       |       example_part1.py
|       |       example_part2.py
|       |       example_save_json.py
|       |       
|       +---get_pages_content
|       |   |   get_pages.py
|       |   |   get_pages_pools.py
|       |   |   get_page_info.py
|       |   |   __init__.py
|       |   |   
|       |   \---__pycache__
|       |           get_pages.cpython-37.pyc
|       |           get_pages_pools.cpython-37.pyc
|       |           get_page_info.cpython-37.pyc
|       |           __init__.cpython-37.pyc
|       |           
|       +---tests
|       |   |   test_get_page_content.py
|       |   |   test_main.py
|       |   |   __init__.py
|       |   |   
|       |   \---__pycache__
|       |           test_get_page_content.cpython-37-pytest-6.1.2.pyc
|       |           test_main.cpython-37-pytest-6.1.2.pyc
|       |           __init__.cpython-37.pyc
|       |           
|       \---__pycache__
|               test_main.cpython-37-pytest-6.1.2.pyc
|               __init__.cpython-37.pyc
|               
\---typings
```
