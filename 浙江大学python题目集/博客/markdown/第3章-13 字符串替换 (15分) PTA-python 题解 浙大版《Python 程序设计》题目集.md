
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 字符串替换
本题要求编写程序，将给定字符串中的大写英文字母按以下对应规则替换：

| 原字母 | 对应字母 | 
|:-----: |:--------:| 
| A | Z | 
| B | Y |
| C | X |
| D | W |
|… |… |
| X | C |
| Y | B |
| Z | A |

### 输入格式：

输入在一行中给出一个不超过80个字符、并以回车结束的字符串。

### 输出格式：

输出在一行中给出替换完成后的字符串。

### 输入样例：
```in
Only the 11 CAPItaL LeTtERS are replaced.
```

### 输出样例：
```out
Lnly the 11 XZKRtaO OeGtVIH are replaced.
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
# 凯撒密码
# 明文 ord
s1 = [chr(i + 65) for i in range(26)]
# 密文
s2 = reversed(s1)
rex = dict(zip(s1, s2))

s = input()
ans = map(lambda x: rex[x] if x.isupper() else x, s)
print(*ans, sep='')

```