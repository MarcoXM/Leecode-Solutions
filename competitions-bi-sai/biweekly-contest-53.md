# biweekly-contest-53





> 如果一个字符串不含有任何重复字符，我们称这个字符串为 **好** 字符串。
>
> 给你一个字符串 `s` ，请你返回 `s` 中长度为 **3** 的 **好子字符串** 的数量。
>
> 注意，如果相同的好子字符串出现多次，每一次都应该被记入答案之中。
>
> **子字符串** 是一个字符串中连续的字符序列。
>
> **示例 1：**
>
> ```text
> 输入：s = "xyzzaz"
> 输出：1
> 解释：总共有 4 个长度为 3 的子字符串："xyz"，"yzz"，"zza" 和 "zaz" 。
> 唯一的长度为 3 的好子字符串是 "xyz" 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：s = "aababcabc"
> 输出：4
> 解释：总共有 7 个长度为 3 的子字符串："aab"，"aba"，"bab"，"abc"，"bca"，"cab" 和 "abc" 。
> 好子字符串包括 "abc"，"bca"，"cab" 和 "abc" 。
> ```
>
> **提示：**
>
> * `1 <= s.length <= 100`
> * `s`​​​​​​ 只包含小写英文字母。

```python
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ##暴力
        ans = 0
        if len(s) < 3:
            return ans
        
        for i in range(len(s)):
            if i + 3 <= len(s) :
                if len(s[i:i + 3]) == len(set(s[i:i + 3])):
                    ans += 1
                    
        return ans
                
```

1877. Minimize Maximum Pair Sum in Array

> 一个数对 `(a,b)` 的 **数对和** 等于 `a + b` 。**最大数对和** 是一个数对数组中最大的 **数对和** 。
>
> * 比方说，如果我们有数对 `(1,5)` ，`(2,3)` 和 `(4,4)`，**最大数对和** 为 `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8` 。
>
> 给你一个长度为 **偶数** `n` 的数组 `nums` ，请你将 `nums` 中的元素分成 `n / 2` 个数对，使得：
>
> * `nums` 中每个元素 **恰好** 在 **一个** 数对中，且
> * **最大数对和** 的值 **最小** 。
>
> 请你在最优数对划分的方案下，返回最小的 **最大数对和** 。
>
> **示例 1：**
>
> ```text
> 输入：nums = [3,5,2,3]
> 输出：7
> 解释：数组中的元素可以分为数对 (3,3) 和 (5,2) 。
> 最大数对和为 max(3+3, 5+2) = max(6, 7) = 7 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：nums = [3,5,4,2,4,6]
> 输出：8
> 解释：数组中的元素可以分为数对 (3,5)，(4,4) 和 (6,2) 。
> 最大数对和为 max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8 。
> ```
>
> **提示：**
>
> * `n == nums.length`
> * `2 <= n <= 105`
> * `n` 是 **偶数** 。
> * `1 <= nums[i] <= 105`

```python
class Solution:

#贪心
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0 
        j = len(nums) - 1
        ans = 0
        while i <j :
            ans = max(ans, nums[i]+ nums[j])
            i += 1
            j -= 1
            
        return ans 
            
```

> 给你一个 `m x n` 的整数矩阵 `grid` 。
>
> **菱形和** 指的是 `grid` 中一个正菱形 **边界** 上的元素之和。本题中的菱形必须为正方形旋转45度，且四个角都在一个格子当中。下图是四个可行的菱形，每个菱形和应该包含的格子都用了相应颜色标注在图中。![](https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-desc-2.png)
>
> 注意，菱形可以是一个面积为 0 的区域，如上图中右下角的紫色菱形所示。
>
> 请你按照 **降序** 返回 `grid` 中三个最大的 **互不相同的菱形和** 。如果不同的和少于三个，则将它们全部返回。
>
> **示例 1：**![](https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex1.png)
>
> ```text
> 输入：grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
> 输出：[228,216,211]
> 解释：最大的三个菱形和如上图所示。
> - 蓝色：20 + 3 + 200 + 5 = 228
> - 红色：200 + 2 + 10 + 4 = 216
> - 绿色：5 + 200 + 4 + 2 = 211
> ```
>
> **示例 2：**![](https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex2.png)
>
> ```text
> 输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
> 输出：[20,9,8]
> 解释：最大的三个菱形和如上图所示。
> - 蓝色：4 + 2 + 6 + 8 = 20
> - 红色：9 （右下角红色的面积为 0 的菱形）
> - 绿色：8 （下方中央面积为 0 的菱形）
> ```
>
> **示例 3：**
>
> ```text
> 输入：grid = [[7,7,7]]
> 输出：[7]
> 解释：所有三个可能的菱形和都相同，所以返回 [7] 。
> ```
>
> **提示：**
>
> * `m == grid.length`
> * `n == grid[i].length`
> * `1 <= m, n <= 100`
> * `1 <= grid[i][j] <= 105`

```python
class Solution:
    def getBiggestThree(self, g: List[List[int]]) -> List[int]:
        
        s1 = [[0] * 150 for _ in range(150)]
        s2 = [[0] * 150 for _ in range(150)]
        n = len(g)
        m = len(g[0])
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s1[i][j] = s1[i- 1][j-1] + g[i- 1][j-1]
                s2[i][j] = s2[i- 1][j+ 1] + g[i- 1][j-1]
                
        ans = set()
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                ans.add(g[i - 1][j - 1]) ## 一个点 
                
                k = 1 
                while i - k>= 1 and i + k <= n and j - k >= 1 and j + k <= m :
                    a = s2[i][j - k]-s2[i - k][j]
                    b = s1[i][j + k]-s1[i - k][j]
                    c = s2[i+k][j] - s2[i][j + k]
                    d = s1[i + k][j] - s1[i][j - k]
                    ans.add(a + b + c +d - g[i + k - 1][j - 1] + g[i - k - 1][j - 1])
                    k += 1

                
                
        return sorted(list(ans),reverse = True)[:3]
                
                
            
            
```





1879. Minimum XOR Sum of Two Arrays

> 给你两个整数数组 `nums1` 和 `nums2` ，它们长度都为 `n` 。
>
> 两个数组的 **异或值之和** 为 `(nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1])` （**下标从 0 开始**）。
>
> * 比方说，`[1,2,3]` 和 `[3,2,1]` 的 **异或值之和** 等于 `(1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4` 。
>
> 请你将 `nums2` 中的元素重新排列，使得 **异或值之和** **最小** 。
>
> 请你返回重新排列之后的 **异或值之和** 。
>
> **示例 1：**
>
> ```text
> 输入：nums1 = [1,2], nums2 = [2,3]
> 输出：2
> 解释：将 nums2 重新排列得到 [3,2] 。
> 异或值之和为 (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：nums1 = [1,0,3], nums2 = [5,3,4]
> 输出：8
> 解释：将 nums2 重新排列得到 [5,4,3] 。
> 异或值之和为 (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8 。
> ```
>
> **提示：**
>
> * `n == nums1.length`
> * `n == nums2.length`
> * `1 <= n <= 14`
> * `0 <= nums1[i], nums2[i] <= 107`

{% tabs %}
{% tab title="状态压缩" %}
```

```
{% endtab %}

{% tab title="Python-模拟退火，性能不行" %}
```python
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        nums2.sort()
        
        
        # t=start 1e6, end 1e-5, 衰退率 0.97
        epoch = 2**((len(nums2))//2) + len(nums2) 
        decay = 0.995
        import random 
        import numpy as np
        if len(nums2) == 1:return nums1[0]^nums2[0]
        
        
        self.ans = float("inf")
        def check():
            ans = 0
            for x,y in zip(nums1,nums2):
                ans += (x ^ y)
            self.ans = min(self.ans, ans) 
            return ans
        
        if nums1 == nums2:
            return check()
        else:
            nums2 = nums2[::-1]
        
        def simmulate_anneal():
            random.shuffle(nums2)
            t = 1e6
            while t > 1e-5 :
                a = random.randint(0, len(nums2) - 1)
                b = random.randint(0, len(nums2) - 1)
                if a == b:continue
                x = check()
                nums2[a], nums2[b] = nums2[b],nums2[a]
                y = check()
                delta = y - x  ## 变小了。。假设
                if delta < 0 :
                    continue
                else:
                    if exp(-delta / t) > random.random():
                        nums2[a], nums2[b] = nums2[b],nums2[a]
                t *= decay
                
        for i in range(epoch):
            simmulate_anneal()
        return self.ans
        
```
{% endtab %}
{% endtabs %}













