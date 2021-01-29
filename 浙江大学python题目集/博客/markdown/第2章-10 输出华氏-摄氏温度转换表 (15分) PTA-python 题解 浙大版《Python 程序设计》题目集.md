
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 输出华氏-摄氏温度转换表
输入2个正整数`lower`和`upper`（`lower`$$\le$$`upper`$$\le$$100），请输出一张取值范围为[`lower`，`upper`]、且每次增加2华氏度的华氏-摄氏温度转换表。

温度转换的计算公式：$$C = 5 \times (F - 32) / 9$$，其中：$$C$$表示摄氏温度，$$F$$表示华氏温度。

### 输入格式:

在一行中输入2个整数，分别表示`lower`和`upper`的值，中间用空格分开。

### 输出格式:

第一行输出："fahr celsius"

接着每行输出一个华氏温度fahr（整型）与一个摄氏温度celsius（占据6个字符宽度，靠右对齐，保留1位小数）。

若输入的范围不合法，则输出"Invalid."。 

### 输入样例1:
```in
32 35
```

### 输出样例1:
```out
fahr celsius
32   0.0
34   1.1
```

### 输入样例2:
```
40 30
```

### 输出样例2:
```
Invalid.
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
lower, upper = map(int, input().split())
print("Invalid." if lower > upper else "fahr celsius")
for i in range(lower, upper + 1, 2):
    c = 5 * (i - 32) / 9
    print(f'{i}{c:>6.1f}')

```