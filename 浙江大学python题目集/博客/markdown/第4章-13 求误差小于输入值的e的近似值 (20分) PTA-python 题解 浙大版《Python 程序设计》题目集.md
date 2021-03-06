
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 求误差小于输入值的e的近似值
自然常数e可以用级数1+1/1!+1/2!+⋯+1/n!来近似计算。e<sub>i</sub>代表前i项求和。输入误差范围error,当   
e<sub>i+1</sub>-e<sub>i</sub><error,则表示e的近似值满足误差范围。

### 输入格式:

在一行输入误差范围。

### 输出格式:

在一行输出e的近似值（保留6位小数）。

### 输入样例1:

在这里给出一组输入。例如：

```in
0.01
```

### 输出样例1:

在这里给出相应的输出。例如：

```out
2.716667
```

### 输入样例2:

在这里给出一组输入。例如：

```in
0.000000001
```

### 输出样例2:

在这里给出相应的输出。例如：

```out
2.718282
```

### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
error = float(input())
e1, e2 = 1, 2
mul, n = 1, 2
while e2 - e1 >= error:
    mul *= n
    n += 1
    e1, e2 = e2, e2 + 1 / mul
print(f'{e2:.6f}')

```