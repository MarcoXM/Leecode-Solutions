# weekly-contest-235

1816. truncate-sentence

> 句子 是一个单词列表，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）。
>
> 例如，"Hello World"、"HELLO" 和 "hello world hello world" 都是句子。 给你一个句子 s​​​​​​ 和一个整数 k​​​​​​ ，请你将 s​​ 截断 ​，​​​使截断后的句子仅含 前 k​​​​​​ 个单词。返回 截断 s​​​​​​ 后得到的句子。

```python
## 字符串就用python
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        return " ".join(s.split()[:k])
```

1817. finding-the-users-active-minutes

> 给你用户在 LeetCode 的操作日志，和一个整数 k 。日志用一个二维整数数组 logs 表示，其中每个 logs\[i\] = \[IDi, timei\] 表示 ID 为 IDi 的用户在 timei 分钟时执行了某个操作。
>
> 多个用户 可以同时执行操作，单个用户可以在同一分钟内执行 多个操作 。
>
> 指定用户的 用户活跃分钟数（user active minutes，UAM） 定义为用户对 LeetCode 执行操作的 唯一分钟数 。 即使一分钟内执行多个操作，也只能按一分钟计数。
>
> 请你统计用户活跃分钟数的分布情况，统计结果是一个长度为 k 且 下标从 1 开始计数 的数组 answer ，对于每个 j（1 &lt;= j &lt;= k），answer\[j\] 表示 用户活跃分钟数 等于 j 的用户数。
>
> 返回上面描述的答案数组 answer 。

```python
## Hash 记录
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        
        cnt = collections.defaultdict(set)
        for i,m in logs:
            cnt[i].add(m)
        c =collections.defaultdict(int)
        for _, v in cnt.items():
            c[len(v)] += 1
            
        ans = [0] * k 
        # print(ans )
        
        for i in range(1, k + 1):
            ans[i - 1] = c[i]
        return ans
        
```

1818. minimum-absolute-sum-difference

> 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
>
> 数组 nums1 和 nums2 的 绝对差值和 定义为所有 \|nums1\[i\] - nums2\[i\]\|（0 &lt;= i &lt; n）的 总和（下标从 0 开始）。
>
> 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
>
> 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
>
> \|x\| 定义为：
>
> 如果 x &gt;= 0 ，值为 x ，或者 如果 x &lt;= 0 ，值为 -x



```python

### 贪心二分， 通过二分找最近的数字。

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        total_sum = 0
        mod = 10**9 + 7
        for x,y in zip(nums1, nums2):
            total_sum += abs(x - y)
            total_sum 
        
        tmp = sorted(nums1)
        max_optimization = 0
        for x,y in zip(nums1, nums2):    ##尝试对nums1的每个位置，都进行替换
            cur = abs(x - y)
            pos_idx = bisect.bisect_left(tmp, y)    #借助二分，加快查找速度
            #######贪心的思想：尽量找nums1中数值大小贴近y的，去替换x
            if 0 <= pos_idx - 1:
                max_optimization = max(max_optimization, cur - (y - tmp[pos_idx - 1]))

            if pos_idx < n:
                max_optimization = max(max_optimization, cur - (tmp[pos_idx] - y))
        
        return (total_sum - max_optimization) % mod
```

1819. number-of-different-subsequences-gcds

> 给你一个由正整数组成的数组 nums 。
>
> 数字序列的 最大公约数 定义为序列中所有整数的共有约数中的最大整数。
>
> 例如，序列 \[4,6,16\] 的最大公约数是 2 。 数组的一个 子序列 本质是一个序列，可以通过删除数组中的某些元素（或者不删除）得到。
>
> 例如，\[2,5,10\] 是 \[1,2,1,2,4,1,5,10\] 的一个子序列。 计算并返回 nums 的所有 非空 子序列中 不同 最大公约数的 数目 。

```python


###  




class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        c = max(nums)
        ans = 0

        for y in range(1, c + 1):
            g = None
            for x in range(y, c + 1, y):
                if x in nums:
                    if not g:
                        g = x
                    else:
                        g = math.gcd(g, x)
                    if g == y:
                        ans += 1
                        break
        
        return ans
```

