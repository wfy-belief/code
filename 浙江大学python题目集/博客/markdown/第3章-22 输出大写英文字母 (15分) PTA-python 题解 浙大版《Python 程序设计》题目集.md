
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 输出大写英文字母
本题要求编写程序，顺序输出给定字符串中所出现过的大写英文字母，每个字母只输出一遍；若无大写英文字母则输出“Not Found”。

### 输入格式：

输入为一个以回车结束的字符串（少于80个字符）。

### 输出格式：

按照输入的顺序在一行中输出所出现过的大写英文字母，每个字母只输出一遍。若无大写英文字母则输出“Not Found”。

### 输入样例1：
```in
FONTNAME and FILENAME
```

### 输出样例1：
```out
FONTAMEIL
```

### 输入样例2：
```
fontname and filrname
```

### 输出样例2：
```
Not Found
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
s = input()
ans = []
for x in s:
    if x.isupper() and x not in ans:
        ans.append(x)
print(''.join(ans) if ans else 'Not Found')

```