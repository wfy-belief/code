
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 输出10个不重复的英文字母
随机输入一个字符串，把最左边的10个不重复的英文字母（不区分大小写）挑选出来。
如没有10个英文字母，显示信息“not found”

### 输入格式:

在一行中输入字符串

### 输出格式:

在一行中输出最左边的10个不重复的英文字母或显示信息“not found"

### 输入样例1:

在这里给出一组输入。例如：

```in
poemp134
```

### 输出样例1:

在这里给出相应的输出。例如：

```out
not found
```
### 输入样例2

在这里给出一组输入。例如：

```in
This is a test example
```

### 输出样例2:

在这里给出相应的输出。例如：

```out
Thisaexmpl
```

### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
ans = []
for s in input():
    if s.isalpha() and s.lower() not in ans and s.upper() not in ans:
        ans.append(s)
    if len(ans) == 10:
        print(''.join(ans))
        break
else:
    print('not found')

```