
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 统计学生平均成绩与及格人数
本题要求编写程序，计算学生们的平均成绩，并统计及格（成绩不低于60分）的人数。题目保证输入与输出均在整型范围内。

### 输入格式:

输入在第一行中给出非负整数N，即学生人数。第二行给出N个非负整数，即这N位学生的成绩，其间以空格分隔。 

### 输出格式:

按照以下格式输出：
```
average = 成绩均值
count = 及格人数
```
其中平均值精确到小数点后一位。 

### 输入样例:
```in
5
77 54 92 73 60
```

### 输出样例:
```out
average = 71.2
count = 4
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
n = int(input())
if n == 0:
    print("average = 0.0")
    print("count = 0")
else:
    l = list(map(int, input().split()))
    average = sum(l) / len(l)
    count_ = len([x for x in l if x >= 60])
    print(f'average = {average:.1f}')
    print(f'count = {count_}')

```