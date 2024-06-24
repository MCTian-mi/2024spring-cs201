# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2024 spring, Complied by ~~天幂~~ 化学与分子工程学院



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows 11 23H2

Python编程环境：Visual Studio Code 1.86.2



## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：根据定义，通过构造列表 l = [T~n-2~, T~n-1~, T~n~] 并不断在右侧增加元素 T~n+1~ = sum(l) 的同时移除最左侧元素。



##### 代码

```python
n = int(input())
l = [0, 1, 1]
if n <= 2:
    print(l[n])
else:
    for i in range(n-2):
        l.append(sum(l))
        l.pop(0)
    print(l[2])
```



代码运行截图 

![image-20240221111056693](pic\image-20240221111056693.png)





### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：从左向右读取字符串中的字符，逐次检测是否含有 “hello” 中的五个字符，通过计分判断是否通过检测。



##### 代码

```python
def check(word : str):
    checklist = "hello"
    i = 0
    for char in word:
        if char == checklist[i]:
            i += 1
            if i == 5:
                return("YES")
    return("NO")
print(check(input()))
```



代码运行截图 

![image-20240221112520685](pic\image-20240221112520685.png)



### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：依次读取原始字符串中的字符 char，若为元音字母则删除，反之则加上 "." + char。



##### 代码

```python
original = input().lower()
ans = ""
notallowed = "aeiouy"
for char in original:
    if not char in notallowed:
        ans += "." + char
print(ans)
```



代码运行截图 

![image-20240221113510395](pic\image-20240221113510395.png)





### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：双重意义上的挨个检查，简单粗暴。



##### 代码

```python
from math import ceil, sqrt

def isprime(n:int):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True

Sum = int(input())
for i in range(2, Sum//2 + 1):
    j = Sum - i
    if (isprime(i) and isprime(j)):
        print(i, j)
        break
```



代码运行截图

![image-20240221115051039](pic\image-20240221115051039.png)





### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：计算概论课做过，使用正则表达式匹配所有前方不为 +0 的 n 并将幂作为捕获组放入列表。



##### 代码

```python
import re
intermedia = input()
listy = [int(x) for x in re.findall(r".(?<!\+0)n\^(\d+)",intermedia)] + [0]
print("n^" + str(max(listy)))
```



代码运行截图 

![image-20240221131541499](pic\image-20240221131541499.png)



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：以输入数值为键，次数为值构造字典，输出所有值等于最大值对应的键。



##### 代码

```python
def addVote(dic:dict, key:int):
    if key not in dic.keys():
        dic[key] = 1
    else:
        dic[key] += 1

votes = {}
ans = []
for x in list(map(int, input().split())):
    addVote(votes, x)
max = max(votes.values())
for key in votes.keys():
    if votes[key] == max:
        ans.append(key)
ans.sort()
print(" ".join(str(x) for x in ans))
```



代码运行截图 

![image-20240221133847801](pic\image-20240221133847801.png)





## 2. 学习总结和收获

因为化院课程原因没法在去年学完计概的下个学期就接着选这门课，现在python语法忘得差不多了，所以这周的题目可以称得上是康复训练，有若干道之前计概课内做过的题，甚至要看好一会才能看懂自己当时在想什么。

其实本周还尝试写了Fraction类，不过在第二周作业里，就不放在这里了。







