
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 查询水果价格
给定四种水果，分别是苹果（apple）、梨（pear）、桔子（orange）、葡萄（grape），单价分别对应为3.00元/公斤、2.50元/公斤、4.10元/公斤、10.20元/公斤。

首先在屏幕上显示以下菜单：
```
[1] apple
[2] pear
[3] orange
[4] grape
[0] exit
```
用户可以输入编号1~4查询对应水果的单价。当连续查询次数超过5次时，程序应自动退出查询；不到5次而用户输入0即退出；输入其他编号，显示价格为0。

### 输入格式:

输入在一行中给出用户连续输入的若干个编号。

### 输出格式:

首先在屏幕上显示菜单。然后对应用户的每个输入，在一行中按格式“price = 价格”输出查询结果，其中价格保留两位小数。当用户连续查询次数超过5次、或主动输入0时，程序结束。

### 输入样例1:
```in
3 -1 0 2
```

### 输出样例1:
```out
[1] apple
[2] pear
[3] orange
[4] grape
[0] exit
price = 4.10
price = 0.00
```

### 输入样例2:
```
1 2 3 3 4 4 5 6 7 8
```

### 输出样例2:
```
[1] apple
[2] pear
[3] orange
[4] grape
[0] exit
price = 3.00
price = 2.50
price = 4.10
price = 4.10
price = 10.20
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
# 比较简单 题解来源于网络
print('[1] apple')
print('[2] pear')
print('[3] orange')
print('[4] grape')
print('[0] exit')
lst = list(map(int, input().split()))
for i in range(0, 5):
    c = int(lst[i])
    if c == 1:
        print('price = 3.00')
    elif c == 2:
        print('price = 2.50')
    elif c == 3:
        print('price = 4.10')
    elif c == 4:
        print('price = 10.20')
    elif c == 0:
        break
    else:
        print('price = 0.00')

```