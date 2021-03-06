
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 分段计算居民水费
为鼓励居民节约用水，自来水公司采取按用水量阶梯式计价的办法，居民应交水费$$y$$（元）与月用水量$$x$$（吨）相关：当$$x$$不超过15吨时，$$y=4x/3$$；超过后，$$y=2.5x-17.5$$。请编写程序实现水费的计算。

### 输入格式：

输入在一行中给出非负实数$$x$$。

### 输出格式：

在一行输出应交的水费，精确到小数点后2位。

### 输入样例1：
```in
12
```

### 输出样例1：
```out
16.00
```

### 输入样例2：
```
16
```

### 输出样例2：
```
22.50
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
def get_money(x):
    if x <= 15:
        return 4 * x / 3
    return 2.5 * x - 17.5


n = int(input())
print(f'{get_money(n):.2f}')

```