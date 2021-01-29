
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 输出字母在字符串中位置索引
输入一个字符串，再输入两个字符，求这两个字符在字符串中的索引。

### 输入格式:

第一行输入字符串    
第二行输入两个字符，用空格分开。

### 输出格式:

反向输出字符和索引，即最后一个最先输出。每行一个。

### 输入样例:

在这里给出一组输入。例如：

```in
mississippi
s p
```

### 输出样例:

在这里给出相应的输出。例如：

```out
9 p
8 p
6 s
5 s
3 s
2 s
```

### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
def get_index(ch):
    for index, value in enumerate(s[::-1]):
        if ch == value:
            print(f'{len(s) - index - 1} {value}')


s = input()
a, b = input().split()
get_index(b)
get_index(a)

```