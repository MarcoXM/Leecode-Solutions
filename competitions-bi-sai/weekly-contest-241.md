# weekly-contest-241

1863. Sum of All Subset XOR Totals

> 一个数组的 **异或总和** 定义为数组中所有元素按位 `XOR` 的结果；如果数组为 **空** ，则异或总和为 `0` 。
>
> * 例如，数组 `[2,5,6]` 的 **异或总和** 为 `2 XOR 5 XOR 6 = 1` 。
>
> 给你一个数组 `nums` ，请你求出 `nums` 中每个 **子集** 的 **异或总和** ，计算并返回这些值相加之 **和** 。
>
> **注意：**在本题中，元素 **相同** 的不同子集应 **多次** 计数。
>
> 数组 `a` 是数组 `b` 的一个 **子集** 的前提条件是：从 `b` 删除几个（也可能不删除）元素能够得到 `a` 。

```python
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        self.ans = 0
        def check(pth):
            ans = 0
            for n in pth:
                ans ^= n
            # print(ans)
            return ans
    
        def dfs(idx, pth):
            self.ans += check(pth)
            if idx == len(nums):
                return 
            
            
            
            for i in range(idx, len(nums)):
                dfs(i + 1, pth + [nums[i]])
        
        dfs( 0, [])
        
        return self.ans
```



1864. Minimum Number of Swaps to Make the Binary String Alternating

> 给你一个二进制字符串 `s` ，现需要将其转化为一个 **交替字符串** 。请你计算并返回转化所需的 **最小** 字符交换次数，如果无法完成转化，返回 __`-1` __。
>
> **交替字符串** 是指：相邻字符之间不存在相等情况的字符串。例如，字符串 `"010"` 和 `"1010"` 属于交替字符串，但 `"0100"` 不是。
>
> 任意两个字符都可以进行交换，**不必相邻** 。

```python
class Solution:
    def minSwaps(self, s: str) -> int:
        if s == "0" or s == "1":return 0
        
        cnt = [0, 0]
        for c in s:
            cnt[int(c)] += 1
            
        if abs(cnt[0]- cnt[1]) > 1:
            return - 1
        
        ans1 = 0
        ans2 = 0
        ## 10101

        for i in range(len(s)):
            if i & 1 and s[i] == "1":
                ans1 += 1

            elif i % 2 == 0 and s[i] == "0":
                ans1 += 1
                
        for i in range(len(s)):
            if i & 1 and s[i] == "0":
                ans2 += 1

            elif i % 2 == 0 and s[i] == "1":
                ans2 += 1
                
        if cnt[1] > cnt[0]:
            return ans1//2
        elif cnt[1] < cnt[0]:
            return ans2//2
        
        return min(ans1//2, ans2//2)
                
```



1865. Finding Pairs With a Certain Sum

> 给你两个整数数组 `nums1` 和 `nums2` ，请你实现一个支持下述两类查询的数据结构：
>
> 1. **累加** ，将一个正整数加到 `nums2` 中指定下标对应元素上。
> 2. **计数** ，统计满足 `nums1[i] + nums2[j]` 等于指定值的下标对 `(i, j)` 数目（`0 <= i < nums1.length` 且 `0 <= j < nums2.length`）。
>
> 实现 `FindSumPairs` 类：
>
> * `FindSumPairs(int[] nums1, int[] nums2)` 使用整数数组 `nums1` 和 `nums2` 初始化 `FindSumPairs` 对象。
> * `void add(int index, int val)` 将 `val` 加到 `nums2[index]` 上，即，执行 `nums2[index] += val` 。
> * `int count(int tot)` 返回满足 `nums1[i] + nums2[j] == tot` 的下标对 `(i, j)` 数

```python
class FindSumPairs:
    

    def __init__(self, nums1: List[int], nums2: List[int]):
        from sortedcontainers import SortedList
        tmp =collections.defaultdict(int)
        for n in nums1:
            tmp[n] += 1
        self.l1 = tmp
        self.l2 = nums2
        
        tmp =collections.defaultdict(int)
        for n in nums2:
            tmp[n] += 1
        self.cnt2 = tmp
        

    def add(self, index: int, val: int) -> None:
        
        pre = self.l2[index]
        
        self.l2[index] += val
        
        cur = self.l2[index]
        self.cnt2[pre] -= 1
        self.cnt2[cur] += 1
        
        

    def count(self, tot: int) -> int:
        
        ans = 0
        for n in self.l1.keys():
            remain = tot - n
            
            if remain >= 1:
                cnt1 = self.l1[n]
                cnt2 = self.cnt2[remain]
                
                ans += (cnt1 * cnt2)
            
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
```



1866. Number of Ways to Rearrange Sticks With K Sticks Visible

> 有 `n` 根长度互不相同的木棍，长度为从 `1` 到 `n` 的整数。请你将这些木棍排成一排，并满足从左侧 **可以看到** **恰好** `k` 根木棍。从左侧 **可以看到** 木棍的前提是这个木棍的 **左侧** 不存在比它 **更长的** 木棍。
>
> * 例如，如果木棍排列为 `[`_**`1`**_`,`_**`3`**_`,2,`_**`5`**_`,4]` ，那么从左侧可以看到的就是长度分别为 `1`、`3` 、`5` 的木棍。
>
> 给你 `n` 和 `k` ，返回符合题目要求的排列 **数目** 。由于答案可能很大，请返回对 `109 + 7` **取余** 的结果。

```python
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        
        ## 斯特林数
        mod = 10**9 + 7 
        f = [[0] * 1010 for _ in range(1010)]
        f[0][0] = 1
        
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                f[i][j] = (f[i - 1][ j - 1]+ (i - 1) * f[i - 1][j])%mod


        return f[n][k]
        
```





