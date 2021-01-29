
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 统计字符
本题要求编写程序，输入10个字符，统计其中英文字母、空格或回车、数字字符和其他字符的个数。

### 输入格式:

输入为10个字符。最后一个回车表示输入结束，不算在内。

### 输出格式:

在一行内按照
```
letter = 英文字母个数, blank = 空格或回车个数, digit = 数字字符个数, other = 其他字符个数
```
的格式输出。

### 输入样例:
```in
aZ &
09 Az
```

### 输出样例:
```out
letter = 4, blank = 3, digit = 2, other = 1
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
import sys

s = sys.stdin.read()
letter, digit, blank, other = 0, 0, 0, 0
for i in s[:-1]:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        blank += 1
    else:
        other += 1
print(f'letter = {letter}, blank = {blank}, digit = {digit}, other = {other}')

```