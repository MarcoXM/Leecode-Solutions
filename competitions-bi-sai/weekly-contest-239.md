# weekly-contest-239

这次太非常不顺

1848. Minimum Distance to the Target Element

> 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数 target 和 start ，请你找出一个下标 i ，满足 nums\[i\] == target 且 abs\(i - start\) 最小化 。注意：abs\(x\) 表示 x 的绝对值。
>
> 返回 abs\(i - start\) 。
>
> 题目数据保证 target 存在于 nums 中。

```python
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        ## 抽象化的能力
        res = 100000
        for i in range(len(nums)):
            if target == nums[i]:
                res = min(res, abs(start - i) )
                
        return res
```

1849. Splitting a String Into Descending Consecutive Values

> 给你一个仅由数字组成的字符串 s 。
>
> 请你判断能否将 s 拆分成两个或者多个 非空子字符串 ，使子字符串的 数值 按 降序 排列，且每两个 相邻子字符串 的数值之 差 等于 1 。
>
> 例如，字符串 s = "0090089" 可以拆分成 \["0090", "089"\] ，数值为 \[90,89\] 。这些数值满足按降序排列，且相邻值相差 1 ，这种拆分方法可行。 另一个例子中，字符串 s = "001" 可以拆分成 \["0", "01"\]、\["00", "1"\] 或 \["0", "0", "1"\] 。然而，所有这些拆分方法都不可行，因为对应数值分别是 \[0,1\]、\[0,1\] 和 \[0,0,1\] ，都不满足按降序排列的要求。 如果可以按要求拆分 s ，返回 true ；否则，返回 false 。
>
> 子字符串 是字符串中的一个连续字符序列。

{% tabs %}
{% tab title="位运算" %}
```python
class Solution:
    def splitString(self, s: str) -> bool:
        
        n = len(s)
        for i in range(1, 1 << n - 1):
            flag = True # 表示是否成功
            last = - 1
            x = int(s[0])
            for j in range(n - 1):
                if i >> j & 1: 
                    if last != -1 and x != last - 1:
                        flag = False
                        break
                        
                    last = x 
                    x = int(s[j + 1])
                else:
                    x = x * 10 + int(s[j + 1])
                    
                    
            if last - 1 != x :flag = False
            if flag:return True
            
        return False
            
```
{% endtab %}

{% tab title="DFS" %}
```python

class Solution:
    def splitString(self, s: str) -> bool:
        ## 抽象画的能力, 就是要看到组最后的序列cnt数是否大于2,过程里面不需要使用pth这样容器记录过程
        def dfs(idx, prev, cnt):
            if idx == len(s):
                return cnt > 1
            
            for i in range(idx,len(s)):
                x = int(s[idx:i + 1])

                if prev == - 1 or (prev != - 1 and x == prev - 1):
                    if dfs(i + 1 , x, cnt + 1):
                        return True
            return False
        
        return dfs(0, -1, 0 )

```
{% endtab %}
{% endtabs %}



1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number

```python
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        nums = [int(x) for x in num]
        n = len(nums)
        a = nums[:]
        while k :
            self.nextPermutation(nums)
            k -= 1
            
        b = nums[:]
        c = len(a) *[0]
        cnt = [0] * 10
        # print(a, b)
        for i in range(n):
            x = a[i]
            cnt[x] += 1
            y = cnt[x]
            # print(x, cnt[x],i)
            for j in range(n):
                if b[j] == x:
                    y -= 1
                    
                if y == 0:
                    c[i] = j
                    break
        res = 0
        print(c)
        for i in range(n):
            for j in range(i + 1,n):
                if c[i] > c[j]:
                    res += 1
                    
        return res
            
        
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                j = i
                while j < n and nums[j] > nums[i-1]:
                    idx = j
                    j += 1
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
                nums[i:] = sorted(nums[i:])
                return
        nums.reverse()
```



> 给你一个二维整数数组 `intervals` ，其中 `intervals[i] = [lefti, righti]` 表示第 `i` 个区间开始于 `lefti` 、结束于 `righti`（包含两侧取值，**闭区间**）。区间的 **长度** 定义为区间中包含的整数数目，更正式地表达是 `righti - lefti + 1` 。
>
> 再给你一个整数数组 `queries` 。第 `j` 个查询的答案是满足 `lefti <= queries[j] <= righti` 的 **长度最小区间 `i` 的长度** 。如果不存在这样的区间，那么答案是 `-1` 。
>
> 以数组形式返回对应查询的所有答案。

```python
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ls = [(i,r - l + 1, l, r) for i, (l, r) in enumerate(intervals)]
        ls = sorted(ls , key = lambda x : x[1])
        
        xs = set()
        for l, r in intervals:
            xs.add(l)
            xs.add(r)
            
        for q in queries:
            xs.add(q)
            
        xs = list(xs)
        xs.sort()
        get = collections.defaultdict(int)
        for i in range(len(xs)):
            get[xs[i]] = i
        
        n = len(xs)
        f = [i for i in range(n + 1)]
        w = [-1 for i in range(n + 1)]
        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        
        for i in range(len(ls)):
            l = get[ls[i][2]]
            r = get[ls[i][3]]
            lenv = ls[i][1]
            while find(l) <= r:
                l = find(l)
                w[l] = lenv
                f[l] = l + 1
        
        ans = []
        for q in queries:
            ans.append(w[get[q]])
            
        return ans
            
```

