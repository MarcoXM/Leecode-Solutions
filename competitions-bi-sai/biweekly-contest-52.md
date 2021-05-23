# biweekly-contest-52



1859. Sorting the Sentence

> 一个 **句子** 指的是一个序列的单词用单个空格连接起来，且开头和结尾没有任何空格。每个单词都只包含小写或大写英文字母。
>
> 我们可以给一个句子添加 **从 1 开始的单词位置索引** ，并且将句子中所有单词 **打乱顺序** 。
>
> * 比方说，句子 `"This is a sentence"` 可以被打乱顺序得到 `"sentence4 a3 is2 This1"` 或者 `"is2 sentence4 This1 a3"` 。
>
> 给你一个 **打乱顺序** 的句子 `s` ，它包含的单词不超过 `9` 个，请你重新构造并得到原本顺序的句子。

```python
class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split()
        data = []
        for x in s:
            data.append((x[:-1],int(x[-1])))
        
        # print(data)
            
        data.sort(key = lambda x: x[1])
        
        ans = []
        for d in data:
            ans.append(d[0])
            
        return " ".join(ans)
```



1860. Incremental Memory Leak

> 给你两个整数 `memory1` 和 `memory2` 分别表示两个内存条剩余可用内存的位数。现在有一个程序每秒递增的速度消耗着内存。
>
> 在第 `i` 秒（秒数从 1 开始），有 `i` 位内存被分配到 **剩余内存较多** 的内存条（如果两者一样多，则分配到第一个内存条）。如果两者剩余内存都不足 `i` 位，那么程序将 **意外退出** 。
>
> 请你返回一个数组，包含 __`[crashTime, memory1crash, memory2crash]` ，其中 `crashTime`是程序意外退出的时间（单位为秒）， __`memory1crash` __和 __`memory2crash` __分别是两个内存条最后剩余内存的位数。

```python
class Solution:
    def memLeak(self, m1: int, m2: int) -> List[int]:
        
        
        ans = 0
        d = 1
        t = 0
        if not m1 and not m2:
            return [1,0,0]
        while m1 or m2:
            t += 1
            if m2 > m1:
                if d <= m2:
                    m2 -= d
                
                else:
                    return [t, m1, m2]
            else:
                if d <= m1:
                    m1 -= d
                    
                else:
                    return [t, m1, m2]
            d += 1
            
        return [t, m1, m2]
        
```



1861. Rotating the Box

> 给你一个 `m x n` 的字符矩阵 `box` ，它表示一个箱子的侧视图。箱子的每一个格子可能为：
>
> * `'#'` 表示石头
> * `'*'` 表示固定的障碍物
> * `'.'` 表示空位置
>
> 这个箱子被 **顺时针旋转 90 度** ，由于重力原因，部分石头的位置会发生改变。每个石头会垂直掉落，直到它遇到障碍物，另一个石头或者箱子的底部。重力 **不会** 影响障碍物的位置，同时箱子旋转不会产生**惯性** ，也就是说石头的水平位置不会发生改变。
>
> 题目保证初始时 `box` 中的石头要么在一个障碍物上，要么在另一个石头上，要么在箱子的底部。
>
> 请你返回一个 __`n x m`的矩阵，表示按照上述旋转后，箱子内的结果。

{% tabs %}
{% tab title="Better" %}
```python
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        n = len(box)
        m = len(box[0])

        res = [[0] * n for _ in range(m) ]
        for j in range(m):
            k = 0
            for i in range(n - 1, -1, -1):
                res[j][k] = box[i][j]
                k += 1

        for i in range(n):
            k = m
            for j in range(m - 1, -1, -1):
                if res[j][i] == "*":
                    k = j 
                elif res[j][i] == "#":
                    res[j][i] = "."
                    k -= 1
                    res[k][i] = "#"

        return res
       

```
{% endtab %}

{% tab title="Python" %}
```python
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        
        res = []
        for i in range(len(box)):
            tmp = box[i]
            r = len(box[0]) - 1
            while r >= 0 :
                if tmp[r] =="*" or tmp[r] == "#":
                    r -= 1
                elif tmp[r] == ".":
                    find = False
                    for l in range(r - 1, -1, - 1):
                        # print("i", i, "r", r, tmp[r],"l",l,tmp[l])
                        if tmp[l] =="*":
                            r = l - 1
                            find = True
                            break
                        elif tmp[l] == "#":
                            find = True
                            tmp[l] ,tmp[r] = tmp[r],tmp[l]
                            r = r - 1
                            break
                            
                    if not find:
                        break
                            
            res.append(tmp)
                            
        
        # print(res)
        n = len(res)
        m = len(res[0])
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                ans[i][j] = res[n - j - 1][i]
                
        return ans
        

        

        
```
{% endtab %}
{% endtabs %}



1862. Sum of Floored Pairs

> 给你一个整数数组 `nums` ，请你返回所有下标对 `0 <= i, j < nums.length` 的 `floor(nums[i] / nums[j])` 结果之和。由于答案可能会很大，请你返回答案对`109 + 7` **取余** 的结果。
>
> 函数 `floor()` 返回输入数字的整数部分。

{% tabs %}
{% tab title="AC" %}
```python
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        N = 100010
        p = [0] * N
        mod = 10**9 + 7
        
        for n in nums:
            p[n] += 1
        
        for i in range(1,N):
            p[i] = p[i] + p[i - 1]

        res= 0 
        for i in range(1, N):
            j = 1
            if p[i] - p[i-1]:
                while j * i < N:
                    l = i * j 
                    r = min(N - 1 , (j + 1) * i - 1)
                    sumv = (p[r] - p[l - 1])*j %mod
                    res = (res + sumv *(p[i] - p[i-1])) % mod
                    j += 1
                
        return res
```
{% endtab %}

{% tab title="TLE" %}
```python
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        
        mod = 10**9 + 7 
        
        # nums.sort()
        lenv = len(nums)
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                ans += (nums[j]//nums[i])%mod
            
        
        
        return ans % mod 
```
{% endtab %}
{% endtabs %}







