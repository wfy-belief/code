
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 大于身高的平均值
中小学生每个学期都要体检，要量身高，因为身高可以反映孩子的生长状况。现在，一个班的身高已经量好了，请输出其中超过平均身高的那些身高。程序的输入为一行数据，其中以空格分隔，每个数据都是一个正整数。程序要输出那些超过输入的正整数的平均数的输入值，每个数后面有一个空格，输出的顺序和输入的相同。

### 输入格式:

在一行输入中一个班的身高值，以空格分隔。

### 输出格式:

在一行输出超过输入的平均数的输入值，以空格分隔。

### 输入样例:

在这里给出一组输入。例如：

```in
143 174 119 127 117 164 110 128
```

### 输出样例:

在这里给出相应的输出。例如：

```out
143 174 164 
```

### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
students = list(map(int, input().split()))
average_height = sum(students) / len(students)
ans = filter(lambda x: x > average_height, students)
print(*ans, end=' ')

```