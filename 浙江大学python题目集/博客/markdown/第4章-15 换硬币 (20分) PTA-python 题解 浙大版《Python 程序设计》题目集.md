
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 换硬币
将一笔零钱换成5分、2分和1分的硬币，要求每种硬币至少有一枚，有几种不同的换法？

### 输入格式:

输入在一行中给出待换的零钱数额$$x\in (8, 100)$$。

### 输出格式:

要求按5分、2分和1分硬币的数量依次从大到小的顺序，输出各种换法。每行输出一种换法，格式为：“fen5:5分硬币数量, fen2:2分硬币数量, fen1:1分硬币数量, total:硬币总数量”。最后一行输出“count = 换法个数”。

### 输入样例:
```in
13
```

### 输出样例:
```out
fen5:2, fen2:1, fen1:1, total:4
fen5:1, fen2:3, fen1:2, total:6
fen5:1, fen2:2, fen1:4, total:7
fen5:1, fen2:1, fen1:6, total:8
count = 4
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
# DP
# 暴力枚举
n = int(input())
cnt = 0
for fen5 in range(n // 5, 0, -1):
    for fen2 in range(n // 2, 0, -1):
        for fen1 in range(n, 0, -1):
            if fen5 * 5 + fen2 * 2 + fen1 == n:
                print('fen5:{:d}, fen2:{:d}, fen1:{:d}, total:{:d}'.format(fen5, fen2, fen1, fen1 + fen2 + fen5))
                cnt = cnt + 1
print('count = {:d}'.format(cnt))

```