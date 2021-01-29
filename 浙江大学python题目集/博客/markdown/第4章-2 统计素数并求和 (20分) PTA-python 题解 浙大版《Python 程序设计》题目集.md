
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 统计素数并求和
本题要求统计给定整数$$M$$和$$N$$区间内素数的个数并对它们求和。

### 输入格式:

输入在一行中给出两个正整数$$M$$和$$N$$（$$1\le M\le N\le 500$$）。


### 输出格式:

在一行中顺序输出$$M$$和$$N$$区间内素数的个数以及它们的和，数字间以空格分隔。

### 输入样例:
```in
10 31
```

### 输出样例:
```out
7 143
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


left, right = map(int, input().split())
count_, sum_ = 0, 0
for i in range(left, right + 1):
    if is_prime(i):
        count_ += 1
        sum_ += i
print(count_, sum_)

```