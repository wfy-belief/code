
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 字符串排序
本题要求编写程序，读入5个字符串，按由小到大的顺序输出。

### 输入格式：

输入为由空格分隔的5个非空字符串，每个字符串不包括空格、制表符、换行符等空白字符，长度小于80。

### 输出格式：

按照以下格式输出排序后的结果：
```
After sorted:
每行一个字符串
```

### 输入样例：
```in
red yellow blue green white
```

### 输出样例：
```out
After sorted:
blue
green
red
white
yellow
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
s = input().split()
s.sort()
print('After sorted:')
print(*s, sep='\n')

```