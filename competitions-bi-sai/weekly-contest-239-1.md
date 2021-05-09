# weekly-contest-239

前两题快，第三，四题想到

1854.  Maximum Population Year

> 给你一个二维整数数组 logs ，其中每个 logs\[i\] = \[birthi, deathi\] 表示第 i 个人的出生和死亡年份。
>
> 年份 x 的 人口 定义为这一年期间活着的人的数目。第 i 个人被计入年份 x 的人口需要满足：x 在闭区间 \[birthi, deathi - 1\] 内。注意，人不应当计入他们死亡当年的人口中。
>
> 返回 人口最多 且 最早 的年份。

```python
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        cnt = collections.defaultdict(int)
        
        for x, y in logs:
            for i in range(x, y):
                cnt[i] += 1
                
        mavx = max(cnt.values())
        
        for c in sorted(cnt.keys()):
            if cnt[c] == mavx:
                return c
```

1855. Maximum Distance Between a Pair of Values

> 给你两个 非递增 的整数数组 nums1​​​​​​ 和 nums2​​​​​​ ，数组下标均 从 0 开始 计数。
>
> 下标对 \(i, j\) 中 0 &lt;= i &lt; nums1.length 且 0 &lt;= j &lt; nums2.length 。如果该下标对同时满足 i &lt;= j 且 nums1\[i\] &lt;= nums2\[j\] ，则称之为 有效 下标对，该下标对的 距离 为 j - i​​ 。​​
>
> 返回所有 有效 下标对 \(i, j\) 中的 最大距离 。如果不存在有效下标对，返回 0 。
>
> 一个数组 arr ，如果每个 1 &lt;= i &lt; arr.length 均有 arr\[i-1\] &gt;= arr\[i\] 成立，那么该数组是一个 非递增 数组。

```python
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        ## i = 
        ans = 0
        i = len(nums1) - 1
        j = len(nums2) - 1
        while i >= 0 and j >= 0 :
            a = nums1[i]
            b = nums2[j]
            
            if a <=b :
                ans = max(ans, j - i)
                i -= 1
            else:
                j -= 1
            
        return ans
```



1856. Maximum Subarray Min-Product

> 一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。
>
> 比方说，数组 \[3,2,5\] （最小值是 2）的最小乘积为 2  _\(3+2+5\) = 2_  10 = 20 。 给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。由于答案可能很大，请你返回答案对 109 + 7 取余 的结果。
>
> 请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。
>
> 子数组 定义为一个数组的 连续 部分。

```python
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
## 先确定中点， 固定一个值，然后再优化另外一个值
        pre_sum = [0]
        nums = [0] + nums + [0]
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
            
        
        left = [ i for i in range(len(nums))]
        right = [ i for i in range(len(nums))]
        
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
                
            stack.append(i)
          
        stack = []
        for i in range(len(nums) - 1, - 1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
                
            stack.append(i)
        # print(left, right )
        ans = 0
        for i in range(len(nums)):
            
            r = right[i] 
            if r != i:
                r -= 1
            
            l = left[i]
            if l!= i:
                l += 1
            ans = max(ans , nums[i] * (pre_sum[r + 1] - pre_sum[l]))
        return ans % 1000000007
```

1857.Largest Color Value in a Directed Graph

> 给你一个 **有向图** ，它含有 `n` 个节点和 `m` 条边。节点编号从 `0` 到 `n - 1` 。
>
> 给你一个字符串 `colors` ，其中 `colors[i]` 是小写英文字母，表示图中第 `i` 个节点的 **颜色** （下标从 **0** 开始）。同时给你一个二维数组 `edges` ，其中 `edges[j] = [aj, bj]` 表示从节点 `aj` 到节点 `bj` 有一条 **有向边** 。
>
> 图中一条有效 **路径** 是一个点序列 `x1 -> x2 -> x3 -> ... -> xk` ，对于所有 `1 <= i < k` ，从 `xi` 到 `xi+1` 在图中有一条有向边。路径的 **颜色值** 是路径中 **出现次数最多** 颜色的节点数目。
>
> 请你返回给定图中有效路径里面的 **最大颜色值 。**如果图中含有环，请返回 `-1` 。

```python
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        
        ## 这是有向图
        g = collections.defaultdict(list)
        d = collections.defaultdict(int)
        f = [[0] * 26 for _ in range(len(colors))]
        for x , y in edges :
            d[y] += 1
            g[x].append(y)
            
        q = collections.deque()
        for i in range(len(colors)):
            if d[i] == 0:
                q.append(i)
        p = []
        while q :
            node = q.popleft()
            p.append(node)
            for nxt in g[node]:
                d[nxt] -= 1
                if d[nxt ]== 0:
                    q.append(nxt)
        
        if len(p) < len(colors) :
            return - 1
        
        res = 0
        for i in p:
            c = ord(colors[i]) - ord("a")
            f[i][c] = max(f[i][c], 1)
            for j in range(26):
                for k in g[i]:
                    t = 0
                    if ord(colors[k]) - ord("a") == j  :
                        t = 1
                    f[k][j] = max(f[i][j] + t , f[k][j])
                    
                res = max(res, f[i][j])
            
        return res
                    
        
  
```



 

