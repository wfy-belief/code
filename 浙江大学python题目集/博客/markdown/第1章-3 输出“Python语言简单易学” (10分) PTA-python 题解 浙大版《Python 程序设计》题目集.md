
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 输出“Python语言简单易学”
### 输入格式:

无

### 输出格式:

输出一句短语，Python语言简单易学。


如果包含汉字，用"print(s.encode("utf-8"))"输出.

如：    

         s="人生苦短，我学Python"  
         print(s.encode("utf-8"))

### 输入样例:

```in
无
```

### 输出样例:

"人生苦短，我学Python" 的输出：

```out
b'\xe4\xba\xba\xe7\x94\x9f\xe8\x8b\xa6\xe7\x9f\xad\xef\xbc\x8c\xe6\x88\x91\xe5\xad\xa6Python'
```

### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
s = "Python语言简单易学"
print(s.encode("utf-8"))

```