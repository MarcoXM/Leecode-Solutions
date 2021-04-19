# weekly-contest-233

1800. maximum-ascending-subarray-sum

> 给你一个正整数组成的数组 nums ，返回 nums 中一个 升序 子数组的最大可能元素和。
>
> 子数组是数组中的一个连续数字序列。
>
> 已知子数组 \[numsl, numsl+1, ..., numsr-1, numsr\] ，若对所有 i（l &lt;= i &lt; r），numsi &lt; numsi+1 都成立，则称这一子数组为 升序 子数组。注意，大小为 1 的子数组也视作 升序 子数组。

```python
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                ans += nums[i]
            else:
                ans = nums[i]
                
            res = max(ans,res)
            
        return res
```



1801. number-of-orders-in-the-backlog

> 给你一个二维整数数组 orders ，其中每个 orders\[i\] = \[pricei, amounti, orderTypei\] 表示有 amounti 笔类型为 orderTypei 、价格为 pricei 的订单。
>
> 订单类型 orderTypei 可以分为两种：
>
> 0 表示这是一批采购订单 buy 1 表示这是一批销售订单 sell 注意，orders\[i\] 表示一批共计 amounti 笔的独立订单，这些订单的价格和类型相同。对于所有有效的 i ，由 orders\[i\] 表示的所有订单提交时间均早于 orders\[i+1\] 表示的所有订单。
>
> 存在由未执行订单组成的 积压订单 。积压订单最初是空的。提交订单时，会发生以下情况：
>
> 如果该订单是一笔采购订单 buy ，则可以查看积压订单中价格 最低 的销售订单 sell 。如果该销售订单 sell 的价格 低于或等于 当前采购订单 buy 的价格，则匹配并执行这两笔订单，并将销售订单 sell 从积压订单中删除。否则，采购订单 buy 将会添加到积压订单中。 反之亦然，如果该订单是一笔销售订单 sell ，则可以查看积压订单中价格 最高 的采购订单 buy 。如果该采购订单 buy 的价格 高于或等于 当前销售订单 sell 的价格，则匹配并执行这两笔订单，并将采购订单 buy 从积压订单中删除。否则，销售订单 sell 将会添加到积压订单中。 输入所有订单后，返回积压订单中的 订单总数 。由于数字可能很大，所以需要返回对 109 + 7 取余的结果。

```python

## 区间最大，流 使用heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buys = []
        # (price, amount)
        sells = []
        for price, amount, typ in orders:
            if typ == 0:
                # buy
                while amount > 0:
                    if sells and sells[0][0] <= price:
                        execute = min(amount, sells[0][1])
                        amount -= execute
                        sells[0][1] -= execute
                        if sells[0][1] == 0:
                            heappop(sells)
                    else:
                        break
                if amount > 0:
                    heappush(buys, [-price, amount])
            else:
                # sell
                while amount > 0:
                    if buys and -buys[0][0] >= price:
                        execute = min(amount, buys[0][1])
                        amount -= execute
                        buys[0][1] -= execute
                        if buys[0][1] == 0:
                            heappop(buys)
                    else:
                        break
                if amount > 0:
                    heappush(sells, [price, amount])
        ans = 0
        mod = 1000000007
        for x in buys:
            ans += x[1]
            ans %= mod
        for x in sells:
            ans += x[1]
            ans %= mod
        return ans
```

1802. maximum-value-at-a-given-index-in-a-bounded-array

> 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
>
> nums.length == n nums\[i\] 是 正整数 ，其中 0 &lt;= i &lt; n abs\(nums\[i\] - nums\[i+1\]\) &lt;= 1 ，其中 0 &lt;= i &lt; n-1 nums 中所有元素之和不超过 maxSum nums\[index\] 的值被 最大化 返回你所构造的数组中的 nums\[index\] 。
>
> 注意：abs\(x\) 等于 x 的前提是 x &gt;= 0 ；否则，abs\(x\) 等于 -x 。

```python
## 具有单调性的问题我们就可以用二分。

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lo = 1
        hi = maxSum
        while lo < hi:
            mi = hi - (hi - lo) // 2
            if self.helper(n, index, mi) <= maxSum:
                lo = mi
            else:
                hi = mi - 1
        return lo
    def helper(self, n, index, T):
        # T, T - 1, T - 2, ...
        # T, T - 1, T - 2, ...
        return T + self.helper2(index, T) + self.helper2(n - index - 1, T)
    def helper2(self, cnt, frm):
        # from - 1, from - 2, ..., from - cnt
        if cnt < frm:
            return frm * cnt - ((cnt * (cnt + 1))//2)
        # from-1,...,1,1,1,1
        return (frm*(frm-1))//2+cnt-frm+1
```



1803. count-pairs-with-xor-in-a-range

> 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。
>
> 漂亮数对 是一个形如 \(i, j\) 的数对，其中 0 &lt;= i &lt; j &lt; nums.length 且 low &lt;= \(nums\[i\] XOR nums\[j\]\) &lt;= high 。

```python
## 异或最大就要想到Trie
 
class Trie(object):
    def __init__(self):
        self.count = 0
        self.neighbors = [None for _ in range(2)]

    def insert(self, x, d=15):
        if d < 0:
            self.count += 1
        else:
            if x & (1 << d):
                idx = 1
            else:
                idx = 0
            if not self.neighbors[idx]:
                self.neighbors[idx] = Trie()
            self.neighbors[idx].insert(x, d - 1)
            self.count = 0
            for i in range(2):
                if self.neighbors[i]:
                    self.count += self.neighbors[i].count

class Solution(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        low -= 1
        trie = Trie()
        ans = 0
        for x in nums:
            now = trie
            for d in range(15, -1, -1):
                if not now:
                    break
                curr = 1 if (high & (1 << d)) else 0
                idx = 0 if ((x & (1 << d)) > 0) == ((high & (1 << d))>0) else 1
                if curr == 1:
                    ans += now.neighbors[1 - idx].count if now.neighbors[1-idx] else 0
                if d == 0:
                    ans += now.neighbors[idx].count if now.neighbors[idx] else 0
                now = now.neighbors[idx]
            now = trie
            for d in range(15, -1, -1):
                if not now:
                    break
                curr = 1 if (low & (1 << d)) else 0
                idx = 0 if ((x & (1 << d)) > 0) == ((low & (1 << d))>0) else 1
                if curr == 1:
                    ans -= now.neighbors[1 - idx].count if now.neighbors[1-idx] else 0
                if d == 0:
                    ans -= now.neighbors[idx].count if now.neighbors[idx] else 0
                now = now.neighbors[idx]
            trie.insert(x)
        return ans
```





