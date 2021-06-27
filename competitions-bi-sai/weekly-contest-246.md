# weekly-contest-246

1913. Maximum Product Difference Between Two Pairs

> 两个数对 `(a, b)` 和 `(c, d)` 之间的 **乘积差** 定义为 `(a * b) - (c * d)` 。
>
> * 例如，`(5, 6)` 和 `(2, 7)` 之间的乘积差是 `(5 * 6) - (2 * 7) = 16` 。
>
> 给你一个整数数组 `nums` ，选出四个 **不同的** 下标 `w`、`x`、`y` 和 `z` ，使数对 `(nums[w], nums[x])` 和 `(nums[y], nums[z])` 之间的 **乘积差** 取到 **最大值** 。
>
> 返回以这种方式取得的乘积差中的 **最大值** 。
>
> **示例 1：**
>
> ```text
> 输入：nums = [5,6,2,7,4]
> 输出：34
> 解释：可以选出下标为 1 和 3 的元素构成第一个数对 (6, 7) 以及下标 2 和 4 构成第二个数对 (2, 4)
> 乘积差是 (6 * 7) - (2 * 4) = 34
> ```
>
> **示例 2：**
>
> ```text
> 输入：nums = [4,2,5,9,7,4,8]
> 输出：64
> 解释：可以选出下标为 3 和 6 的元素构成第一个数对 (9, 8) 以及下标 1 和 5 构成第二个数对 (2, 4)
> 乘积差是 (9 * 8) - (2 * 4) = 64
> ```
>
> **提示：**
>
> * `4 <= nums.length <= 104`
> * `1 <= nums[i] <= 104`

```python
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
```



1914. Cyclically Rotating a Grid

> 给你一个大小为 `m x n` 的整数矩阵 `grid`​​​ ，其中 `m` 和 `n` 都是 **偶数** ；另给你一个整数 `k` 。
>
> 矩阵由若干层组成，如下图所示，每种颜色代表一层：
>
> ![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png)
>
> 矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 **逆时针** 方向的相邻元素。轮转示例如下：![](https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg)
>
> 返回执行 `k` 次循环轮转操作后的矩阵。
>
> **示例 1：**![](https://assets.leetcode.com/uploads/2021/06/19/rod2.png)
>
> ```text
> 输入：grid = [[40,10],[30,20]], k = 1
> 输出：[[10,20],[40,30]]
> 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
> ```
>
> **示例 2：**![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png) ![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png) ![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png)
>
> ```text
> 输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
> 输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
> 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
> ```
>
> **提示：**
>
> * `m == grid.length`
> * `n == grid[i].length`
> * `2 <= m, n <= 50`
> * `m` 和 `n` 都是 **偶数**
> * `1 <= grid[i][j] <= 5000`
> * `1 <= k <= 109`

```python
class Solution:
    def rotateGrid(self, g: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(g)
        m = len(g[0])
        a = n 
        b = m
        i = 0
        res = [[0] * m for _ in range(n)]
        while a and b :
            x = i 
            y = i 
            stack = []
            for j in range(b - 1):
                stack.append((x , y + 1))
                y += 1
            
            for j in range(a - 1):
                stack.append((x + 1,y))
                x += 1
                
            for j in range(b - 1):
                stack.append((x , y - 1))
                y -= 1
                
            for j in range(a - 1):
                stack.append((x - 1, y))
                x -= 1
                
            for j in range(len(stack)):
                t = (j + k) % len(stack)
                res[stack[j][0]][stack[j][1]] = g[stack[t][0]][stack[t][1]]

            a -= 2 
            b -= 2
            i += 1
            
        return res
        
        
        
```

1915. Number of Wonderful Substrings

> 如果某个字符串中 **至多一个** 字母出现 **奇数** 次，则称其为 **最美** 字符串。
>
> * 例如，`"ccjjc"` 和 `"abab"` 都是最美字符串，但 `"ab"` 不是。
>
> 给你一个字符串 `word` ，该字符串由前十个小写英文字母组成（`'a'` 到 `'j'`）。请你返回 `word` 中 **最美非空子字符串** 的数目_。_如果同样的子字符串在 __`word` 中出现多次，那么应当对 **每次出现** 分别计数_。_
>
> **子字符串** 是字符串中的一个连续字符序列。
>
> **示例 1：**
>
> ```text
> 输入：word = "aba"
> 输出：4
> 解释：4 个最美子字符串如下所示：
> - "aba" -> "a"
> - "aba" -> "b"
> - "aba" -> "a"
> - "aba" -> "aba"
> ```
>
> **示例 2：**
>
> ```text
> 输入：word = "aabb"
> 输出：9
> 解释：9 个最美子字符串如下所示：
> - "aabb" -> "a"
> - "aabb" -> "aa"
> - "aabb" -> "aab"
> - "aabb" -> "aabb"
> - "aabb" -> "a"
> - "aabb" -> "abb"
> - "aabb" -> "b"
> - "aabb" -> "bb"
> - "aabb" -> "b"
> ```
>
> **示例 3：**
>
> ```text
> 输入：word = "he"
> 输出：2
> 解释：2 个最美子字符串如下所示：
> - "he" -> "h"
> - "he" -> "e"
> ```
>
> **提示：**
>
> * `1 <= word.length <= 105`
> * `word` 由从 `'a'` 到 `'j'` 的小写英文字母组成

1916. Count Ways to Build Rooms in an Ant Colony

> 你是一只蚂蚁，负责为蚁群构筑 `n` 间编号从 `0` 到 `n-1` 的新房间。给你一个 **下标从 0 开始** 且长度为 `n` 的整数数组 `prevRoom` 作为扩建计划。其中，`prevRoom[i]` 表示在构筑房间 `i` 之前，你必须先构筑房间 `prevRoom[i]` ，并且这两个房间必须 **直接** 相连。房间 `0` 已经构筑完成，所以 `prevRoom[0] = -1` 。扩建计划中还有一条硬性要求，在完成所有房间的构筑之后，从房间 `0` 可以访问到每个房间。
>
> 你一次只能构筑 **一个** 房间。你可以在 **已经构筑好的** 房间之间自由穿行，只要这些房间是 **相连的** 。如果房间 `prevRoom[i]` 已经构筑完成，那么你就可以构筑房间 `i`。
>
> 返回你构筑所有房间的 **不同顺序的数目** 。由于答案可能很大，请返回对 `109 + 7` **取余** 的结果。
>
> **示例 1：**![](https://assets.leetcode.com/uploads/2021/06/19/d1.JPG)
>
> ```text
> 输入：prevRoom = [-1,0,1]
> 输出：1
> 解释：仅有一种方案可以完成所有房间的构筑：0 → 1 → 2
> ```
>
> **示例 2：**![](https://assets.leetcode.com/uploads/2021/06/19/d2.JPG)
>
> ```text
> 输入：prevRoom = [-1,0,0,1,2]
> 输出：6
> 解释：
> 有 6 种不同顺序：
> 0 → 1 → 3 → 2 → 4
> 0 → 2 → 4 → 1 → 3
> 0 → 1 → 2 → 3 → 4
> 0 → 1 → 2 → 4 → 3
> 0 → 2 → 1 → 3 → 4
> 0 → 2 → 1 → 4 → 3
> ```
>
> **提示：**
>
> * `n == prevRoom.length`
> * `2 <= n <= 105`
> * `prevRoom[0] == -1`
> * 对于所有的 `1 <= i < n` ，都有 `0 <= prevRoom[i] < n`
> * 题目保证所有房间都构筑完成后，从房间 `0` 可以访问到每个房间



```python
mod = 10**9 + 7
        
        n = len(prevRoom)
        # fac[i] 表示 i!
        # inv[i] 表示 i! 的乘法逆元
        fac, inv = [0] * n, [0] * n
        fac[0] = inv[0] = 1
        for i in range(1, n):
            fac[i] = fac[i - 1] * i % mod
            # 使用费马小定理计算乘法逆元
            inv[i] = pow(fac[i], mod - 2, mod)
        
        # 构造树
        edges = defaultdict(list)
        for i in range(1, n):
            edges[prevRoom[i]].append(i)
        
        f, cnt = [0] * n, [0] * n
        
        def dfs(u: int) -> None:
            f[u] = 1
            for v in edges[u]:
                dfs(v)
                # 乘以左侧的 f[ch] 以及右侧分母中 cnt[ch] 的乘法逆元
                f[u] = f[u] * f[v] * inv[cnt[v]] % mod
                cnt[u] += cnt[v]
            # 乘以右侧分子中的 (cnt[i] - 1)!
            f[u] = f[u] * fac[cnt[u]] % mod
            cnt[u] += 1
        
        dfs(0)
        return f[0]
```





