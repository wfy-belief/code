
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 输出三角形面积和周长
本题要求编写程序，根据输入的三角形的三条边$$a$$、$$b$$、$$c$$，计算并输出面积和周长。注意：在一个三角形中， 任意两边之和大于第三边。三角形面积计算公式：$$area=\sqrt{s(s-a)(s-b)(s-c)}$$，其中$$s=(a+b+c)/2$$。

### 输入格式：

输入为3个正整数，分别代表三角形的3条边$$a$$、$$b$$、$$c$$。

### 输出格式：

如果输入的边能构成一个三角形，则在一行内，按照
```
area = 面积; perimeter = 周长
```
的格式输出，保留两位小数。否则，输出
```
These sides do not correspond to a valid triangle
```

### 输入样例1：
```in
5 5 3
```

### 输出样例1：
```out
area = 7.15; perimeter = 13.00
```

### 输入样例2：
```
1 4 1
```

### 输出样例2：
```
These sides do not correspond to a valid triangle
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
# 两短边之和大于长边即可
a, b, c = map(int, input().split())
# if max(a, b, c) > a + b + c - max(a, b, c)
if 2 * max(a, b, c) < a + b + c:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'area = {area:.2f}; perimeter = {s * 2:.2f}')
else:
    print('These sides do not correspond to a valid triangle')

```