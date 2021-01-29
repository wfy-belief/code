
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 判断素数
判断一个给定的正整数是否素数

### 输入格式:

输入在第一行给出一个正整数N（≤ 10），随后N行，每行给出一个小于1000000 的需要判断的正整数

### 输出格式:

对每个需要判断的正整数，如果它是素数，则在一行中输出Yes，否则输出No

### 输入样例:

在这里给出一组输入。例如：

```in
2
11
111
```

### 输出样例:

在这里给出相应的输出。例如：

```out
Yes
No
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


for _ in range(int(input())):
    n = int(input())
    print('Yes' if is_prime(n) else 'No')

```