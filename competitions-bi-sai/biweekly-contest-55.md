# biweekly-contest 55

1909. Remove One Element to Make the Array Strictly Increasing

> 给你一个下标从 **0** 开始的整数数组 `nums` ，如果 **恰好** 删除 **一个** 元素后，数组 **严格递增** ，那么请你返回 `true` ，否则返回 `false` 。如果数组本身已经是严格递增的，请你也返回 `true` 。
>
> 数组 `nums` 是 **严格递增** 的定义为：对于任意下标的 `1 <= i < nums.length` 都满足 `nums[i - 1] < nums[i]` 。
>
> **示例 1：**
>
> ```text
> 输入：nums = [1,2,10,5,7]
> 输出：true
> 解释：从 nums 中删除下标 2 处的 10 ，得到 [1,2,5,7] 。
> [1,2,5,7] 是严格递增的，所以返回 true 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：nums = [2,3,1,2]
> 输出：false
> 解释：
> [3,1,2] 是删除下标 0 处元素后得到的结果。
> [2,1,2] 是删除下标 1 处元素后得到的结果。
> [2,3,2] 是删除下标 2 处元素后得到的结果。
> [2,3,1] 是删除下标 3 处元素后得到的结果。
> 没有任何结果数组是严格递增的，所以返回 false 。
> ```
>
> **示例 3：**
>
> ```text
> 输入：nums = [1,1,1]
> 输出：false
> 解释：删除任意元素后的结果都是 [1,1] 。
> [1,1] 不是严格递增的，所以返回 false 。
> ```
>
> **示例 4：**
>
> ```text
> 输入：nums = [1,2,3]
> 输出：true
> 解释：[1,2,3] 已经是严格递增的，所以返回 true 。
> ```
>
> **提示：**
>
> * `2 <= nums.length <= 1000`
> * `1 <= nums[i] <= 1000`

```python

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        if nums == sorted(nums) and len(set(nums)) == len(nums):
            return True
        
        for i in range(len(nums)):
            tmp = nums[:i] + nums[i + 1:]
            if tmp == sorted(tmp) and len(set(tmp)) == len(tmp):
                return True

        return False
```



1910. Remove All Occurrences of a Substring

> 给你两个字符串 `s` 和 `part` ，请你对 `s` 反复执行以下操作直到 **所有** 子字符串 `part` 都被删除：
>
> * 找到 `s` 中 **最左边** 的子字符串 `part` ，并将它从 `s` 中删除。
>
> 请你返回从 `s` 中删除所有 `part` 子字符串以后得到的剩余字符串。
>
> 一个 **子字符串** 是一个字符串中连续的字符序列。
>
> **示例 1：**
>
> ```text
> 输入：s = "daabcbaabcbc", part = "abc"
> 输出："dab"
> 解释：以下操作按顺序执行：
> - s = "daabcbaabcbc" ，删除下标从 2 开始的 "abc" ，得到 s = "dabaabcbc" 。
> - s = "dabaabcbc" ，删除下标从 4 开始的 "abc" ，得到 s = "dababc" 。
> - s = "dababc" ，删除下标从 3 开始的 "abc" ，得到 s = "dab" 。
> 此时 s 中不再含有子字符串 "abc" 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：s = "axxxxyyyyb", part = "xy"
> 输出："ab"
> 解释：以下操作按顺序执行：
> - s = "axxxxyyyyb" ，删除下标从 4 开始的 "xy" ，得到 s = "axxxyyyb" 。
> - s = "axxxyyyb" ，删除下标从 3 开始的 "xy" ，得到 s = "axxyyb" 。
> - s = "axxyyb" ，删除下标从 2 开始的 "xy" ，得到 s = "axyb" 。
> - s = "axyb" ，删除下标从 1 开始的 "xy" ，得到 s = "ab" 。
> 此时 s 中不再含有子字符串 "xy" 。
> ```
>
> **提示：**
>
> * `1 <= s.length <= 1000`
> * `1 <= part.length <= 1000`
> * `s`​​​​​​ 和 `part` 只包小写英文字母。

```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        def check(s, part):
            if len(s) < len(part):
                return s
            
            l = len(part)
            for i in range(len(s)):
                if s[i:i + l] == part:
                    s = s[:i] + s[i + l:]
                    break
            return s
        
        while check(s,part) != s:
            s = check(s,part)
            
            
        return s
        
```



1911. Maximum Alternating Subsequence Sum

> 一个下标从 **0** 开始的数组的 **交替和** 定义为 **偶数** 下标处元素之 **和** 减去 **奇数** 下标处元素之 **和** 。
>
> * 比方说，数组 `[4,2,5,3]` 的交替和为 `(4 + 5) - (2 + 3) = 4` 。
>
> 给你一个数组 `nums` ，请你返回 `nums` 中任意子序列的 **最大交替和** （子序列的下标 **重新** 从 0 开始编号）。
>
> * 
> 一个数组的 **子序列** 是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说，`[2,7,4]` 是 `[4,`**`2`**`,3,`**`7`**`,2,1,`**`4`**`]` 的一个子序列（加粗元素），但是 `[2,4,2]` 不是。
>
> **示例 1：**
>
> ```text
> 输入：nums = [4,2,5,3]
> 输出：7
> 解释：最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：nums = [5,6,7,8]
> 输出：8
> 解释：最优子序列为 [8] ，交替和为 8 。
> ```
>
> **示例 3：**
>
> ```text
> 输入：nums = [6,2,1,2,4,5]
> 输出：10
> 解释：最优子序列为 [6,1,5] ，交替和为 (6 + 5) - 1 = 10 。
> ```
>
> **提示：**
>
> * `1 <= nums.length <= 105`
> * `1 <= nums[i] <= 105`

```python

class Solution:
    def maxAlternatingSum(self, prices: List[int]) -> int:
        prices = [0] + prices
        k = len(prices)
        if not prices or not k:
            return 0
        n = len(prices)
        
        # 当k大于数组长度的一半时，等同于不限次数交易即122题，用贪心算法解决，否则LeetCode会超时，也可以直接把超大的k替换为数组的一半，就不用写额外的贪心算法函数
        if k > n//2:
            return self.greedy(prices)
        
        dp, res = [[[0]*2 for _ in range(k+1)] for _ in range(n)], []
        # dp[i][k][0]表示第i天已交易k次时不持有股票 dp[i][k][1]表示第i天已交易k次时持有股票
        # 设定在卖出时加1次交易次数
        for i in range(k+1):
            dp[0][i][0], dp[0][i][1] = 0, - prices[0]
        for i in range(1, n):
            for j in range(k+1):
                if not j:
                    dp[i][j][0] = dp[i-1][j][0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])
        # 「所有交易次数最后一天不持有股票」的集合的最大值即为问题的解
        for m in range(k+1):
            res.append(dp[n-1][m][0])
        return max(res)
    
    # 处理k过大导致超时的问题，用贪心解决
    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
```





1912. Design Movie Rental System

> 你有一个电影租借公司和 `n` 个电影商店。你想要实现一个电影租借系统，它支持查询、预订和返还电影的操作。同时系统还能生成一份当前被借出电影的报告。
>
> 所有电影用二维整数数组 `entries` 表示，其中 `entries[i] = [shopi, moviei, pricei]` 表示商店 `shopi` 有一份电影 `moviei` 的拷贝，租借价格为 `pricei` 。每个商店有 **至多一份** 编号为 `moviei` 的电影拷贝。
>
> 系统需要支持以下操作：
>
> * **Search：**找到拥有指定电影且 **未借出** 的商店中 **最便宜的 5 个** 。商店需要按照 **价格** 升序排序，如果价格相同，则 `shopi` **较小** 的商店排在前面。如果查询结果少于 5 个商店，则将它们全部返回。如果查询结果没有任何商店，则返回空列表。
> * **Rent：**从指定商店借出指定电影，题目保证指定电影在指定商店 **未借出** 。
> * **Drop：**在指定商店返还 **之前已借出** 的指定电影。
> * **Report：**返回 **最便宜的 5 部已借出电影** （可能有重复的电影 ID），将结果用二维列表 `res` 返回，其中 `res[j] = [shopj, moviej]` 表示第 `j` 便宜的已借出电影是从商店 `shopj` 借出的电影 `moviej` 。`res` 中的电影需要按 **价格** 升序排序；如果价格相同，则 ****`shopj` **较小** 的排在前面；如果仍然相同，则 `moviej` **较小** 的排在前面。如果当前借出的电影小于 5 部，则将它们全部返回。如果当前没有借出电影，则返回一个空的列表。
>
> 请你实现 `MovieRentingSystem` 类：
>
> * `MovieRentingSystem(int n, int[][] entries)` 将 `MovieRentingSystem` 对象用 `n` 个商店和 `entries` 表示的电影列表初始化。
> * `List<Integer> search(int movie)` 如上所述，返回 **未借出** 指定 `movie` 的商店列表。
> * `void rent(int shop, int movie)` 从指定商店 `shop` 借出指定电影 `movie` 。
> * `void drop(int shop, int movie)` 在指定商店 `shop` 返还之前借出的电影 `movie` 。
> * `List<List<Integer>> report()` 如上所述，返回最便宜的 **已借出** 电影列表。
>
> **注意：**测试数据保证 `rent` 操作中指定商店拥有 **未借出** 的指定电影，且 `drop` 操作指定的商店 **之前已借出** 指定电影。
>
> **示例 1：**
>
> ```text
> 输入：
> ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
> [[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
> 输出：
> [null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]
>
> 解释：
> MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
> movieRentingSystem.search(1);  // 返回 [1, 0, 2] ，商店 1，0 和 2 有未借出的 ID 为 1 的电影。商店 1 最便宜，商店 0 和 2 价格相同，所以按商店编号排序。
> movieRentingSystem.rent(0, 1); // 从商店 0 借出电影 1 。现在商店 0 未借出电影编号为 [2,3] 。
> movieRentingSystem.rent(1, 2); // 从商店 1 借出电影 2 。现在商店 1 未借出的电影编号为 [1] 。
> movieRentingSystem.report();   // 返回 [[0, 1], [1, 2]] 。商店 0 借出的电影 1 最便宜，然后是商店 1 借出的电影 2 。
> movieRentingSystem.drop(1, 2); // 在商店 1 返还电影 2 。现在商店 1 未借出的电影编号为 [1,2] 。
> movieRentingSystem.search(2);  // 返回 [0, 1] 。商店 0 和 1 有未借出的 ID 为 2 的电影。商店 0 最便宜，然后是商店 1 。
> ```
>
> **提示：**
>
> * `1 <= n <= 3 * 105`
> * `1 <= entries.length <= 105`
> * `0 <= shopi < n`
> * `1 <= moviei, pricei <= 104`
> * 每个商店 **至多** 有一份电影 `moviei` 的拷贝。
> * `search`，`rent`，`drop` 和 `report` 的调用 **总共** 不超过 `105` 次。

```python
class MovieRentingSystem:
    
    def __init__(self, n: int, entries: List[List[int]]):
        from sortedcontainers import SortedList
        self.price2shop = collections.defaultdict(SortedList)
        self.price_rent = SortedList()
        self.shop2movie = dict()
        self.rent_list = SortedList()
        for shpid,movieid,price in  entries:
            self.price2shop[movieid].add((price, shpid))
            self.shop2movie[(shpid,movieid)] = price
            

    def search(self, movie: int) -> List[int]:        
        ans = []
        for p,s in self.price2shop[movie]:
            if self.shop2movie[(s,movie)] > 0:
                ans.append(s)
            if len(ans) >= 5:
                return ans
            
        return ans



    def rent(self, shop: int, movie: int) -> None:
        self.rent_list.add((self.shop2movie[(shop,movie)],shop,movie))
        self.shop2movie[(shop,movie)] =  - self.shop2movie[(shop,movie)]
        

        

    def drop(self, shop: int, movie: int) -> None:
        self.rent_list.remove((-self.shop2movie[(shop,movie)],shop,movie))
        self.shop2movie[(shop,movie)] =  - self.shop2movie[(shop,movie)]

    def report(self) -> List[List[int]]:
        tmp = self.rent_list[:5]
        return list(map(lambda x : x[1:],tmp[:5]))
        



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
```





