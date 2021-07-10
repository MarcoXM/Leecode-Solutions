# biweekly-contest 56

1925. Count Square Sum Triples

> 一个 **平方和三元组** `(a,b,c)` 指的是满足 `a2 + b2 = c2` 的 **整数** 三元组 `a`，`b` 和 `c` 。
>
> 给你一个整数 `n` ，请你返回满足 __`1 <= a, b, c <= n` 的 **平方和三元组** 的数目。
>
> **示例 1：**
>
> ```text
> 输入：n = 5
> 输出：2
> 解释：平方和三元组为 (3,4,5) 和 (4,3,5) 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：n = 10
> 输出：4
> 解释：平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。
> ```
>
> **提示：**
>
> * `1 <= n <= 250`

```python
class Solution:
    def countTriples(self, n: int) -> int:
        ## 特别烦一开始暴力还超时
#         nums = [i]
        
#         ans = 0
#         for i in range(n - 1):
#             for j in range(i+ 1,n):
#                 for k in range(j+ 1 ,n +1):
#                     if i **2 + j **2 == k **2:
#                         ans += 1
        from math import pow
        ans = 0
        for k in range(2,n + 1):
            l = 1
            r = k - 1
            while l <= r :
                if pow(l,2) + pow(r,2) == pow(k,2):
                    ans += 1
                    l += 1
                    r -= 1
                elif pow(l,2) + pow(r,2) < pow(k,2):
                    l += 1
                    
                elif pow(l,2) + pow(r,2) > pow(k,2):
                    r -= 1
                     
        return ans * 2
```



1926. Nearest Exit from Entrance in Maze

> 给你一个 `m x n` 的迷宫矩阵 `maze` （**下标从 0 开始**），矩阵中有空格子（用 `'.'` 表示）和墙（用 `'+'` 表示）。同时给你迷宫的入口 `entrance` ，用 `entrance = [entrancerow, entrancecol]` 表示你一开始所在格子的行和列。
>
> 每一步操作，你可以往 **上**，**下**，**左** 或者 **右** 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 `entrance` **最近** 的出口。**出口** 的含义是 `maze` **边界** 上的 **空格子**。`entrance` 格子 **不算** 出口。
>
> 请你返回从 `entrance` 到最近出口的最短路径的 **步数** ，如果不存在这样的路径，请你返回 `-1` 。
>
> **示例 1：**![](https://assets.leetcode.com/uploads/2021/06/04/nearest1-grid.jpg)
>
> ```text
> 输入：maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
> 输出：1
> 解释：总共有 3 个出口，分别位于 (1,0)，(0,2) 和 (2,3) 。
> 一开始，你在入口格子 (1,2) 处。
> - 你可以往左移动 2 步到达 (1,0) 。
> - 你可以往上移动 1 步到达 (0,2) 。
> 从入口处没法到达 (2,3) 。
> 所以，最近的出口是 (0,2) ，距离为 1 步。
> ```
>
> **示例 2：**![](https://assets.leetcode.com/uploads/2021/06/04/nearesr2-grid.jpg)
>
> ```text
> 输入：maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
> 输出：2
> 解释：迷宫中只有 1 个出口，在 (1,2) 处。
> (1,0) 不算出口，因为它是入口格子。
> 初始时，你在入口与格子 (1,0) 处。
> - 你可以往右移动 2 步到达 (1,2) 处。
> 所以，最近的出口为 (1,2) ，距离为 2 步。
> ```
>
> **示例 3：**![](https://assets.leetcode.com/uploads/2021/06/04/nearest3-grid.jpg)
>
> ```text
> 输入：maze = [[".","+"]], entrance = [0,0]
> 输出：-1
> 解释：这个迷宫中没有出口。
> ```
>
> **提示：**
>
> * `maze.length == m`
> * `maze[i].length == n`
> * `1 <= m, n <= 100`
> * `maze[i][j]` 要么是 `'.'` ，要么是 `'+'` 。
> * `entrance.length == 2`
> * `0 <= entrancerow < m`
> * `0 <= entrancecol < n`
> * `entrance` 一定是空格子。

```python
class Solution:
    def nearestExit(self, mat: List[List[str]], entrance: List[int]) -> int:
        
        q = collections.deque()
        visited = set()
        entrance = tuple(entrance)
        visited.add(entrance)
        n = len(mat)
        m = len(mat[0])
        q.append(entrance)
        step = 0
        # print(mat[0][1])
        while q:
            ls = len(q)
            for _ in range(ls):
                x,y  = q.popleft()
                # print(node,mat[node[0]][node[1]])
                if (x,y) != entrance and (x == 0 or x == n - 1 or y==0 or y==m-1):
                    # print(node)
                    return step
                
                for dx,dy in [(0,1),(-1,0),(1,0),(0,-1)]:
                    newx = dx + x
                    newy = dy + y
                    # print(mat[newx][newy],(newx,newy),mat[0][1])
                    if 0 <= newx < n and 0 <=newy< m and mat[newx][newy] != '+' and (newx,newy) not in visited :
                        visited.add((newx,newy))
                        q.append((newx,newy))
            step += 1
        return -1
        
    
```

1927. Sum Game

> Alice 和 Bob 玩一个游戏，两人轮流行动，**Alice 先手** 。
>
> 给你一个 **偶数长度** 的字符串 `num` ，每一个字符为数字字符或者 `'?'` 。每一次操作中，如果 `num` 中至少有一个 `'?'` ，那么玩家可以执行以下操作：
>
> 1. 选择一个下标 `i` 满足 `num[i] == '?'` 。
> 2. 将 `num[i]` 用 `'0'` 到 `'9'` 之间的一个数字字符替代。
>
> 当 `num` 中没有 `'?'` 时，游戏结束。
>
> Bob 获胜的条件是 `num` 中前一半数字的和 **等于** 后一半数字的和。Alice 获胜的条件是前一半的和与后一半的和 **不相等** 。
>
> * 比方说，游戏结束时 `num = "243801"` ，那么 Bob 获胜，因为 `2+4+3 = 8+0+1` 。如果游戏结束时 `num = "243803"` ，那么 Alice 获胜，因为 `2+4+3 != 8+0+3` 。
>
> 在 Alice 和 Bob 都采取 **最优** 策略的前提下，如果 Alice 获胜，请返回 `true` ，如果 Bob 获胜，请返回 `false` 。  
>
>
> **示例 1：**
>
> ```text
> 输入：num = "5023"
> 输出：false
> 解释：num 中没有 '?' ，没法进行任何操作。
> 前一半的和等于后一半的和：5 + 0 = 2 + 3 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：num = "25??"
> 输出：true
> 解释：Alice 可以将两个 '?' 中的一个替换为 '9' ，Bob 无论如何都无法使前一半的和等于后一半的和。
> ```
>
> **示例 3：**
>
> ```text
> 输入：num = "?3295???"
> 输出：false
> 解释：Bob 总是能赢。一种可能的结果是：
> - Alice 将第一个 '?' 用 '9' 替换。num = "93295???" 。
> - Bob 将后面一半中的一个 '?' 替换为 '9' 。num = "932959??" 。
> - Alice 将后面一半中的一个 '?' 替换为 '2' 。num = "9329592?" 。
> - Bob 将后面一半中最后一个 '?' 替换为 '7' 。num = "93295927" 。
> Bob 获胜，因为 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7 。
> ```
>
> **提示：**
>
> * `2 <= num.length <= 105`
> * `num.length` 是 **偶数** 。
> * `num` 只包含数字字符和 `'?'` 。

```python
class Solution:
    def sumGame(self, num: str) -> bool:
        
        lenv = len(num)//2
        
        def cnt(nums):
            s = 0
            c = 0
            for n in nums:
                if n.isdigit():
                    s += int(n)
                else:
                    c += 1
            return s, c 
        
        fs,fc = cnt(num[:lenv])
        bs,bc = cnt(num[lenv:])
        # print(fs,fc,bs,bc)
        ## 机会一样，填一样的数字
        if bc == fc:
            ## 数值相等，必定相等 
            if fs == bs:
                return False
            return True
        else:
            ## 前面机会多
            # print(fs,fc,bs,bc)
            if fc > bc:
                if fs >= bs:
                    return True
                else:
                    ## 前面和小，还有机会
                    diff = bs - fs 
                    ch = (fc - bc)//2
                    if diff ==  9 * ch  :
                        return False
                    return True
                
            else: # 后面机会多
                if fs <= bs:
                    return True
                else:
                    # 前面和大 
                    diff = fs - bs 
                    ch = (bc - fc)//2
                    if diff ==  9 * ch  :
                        return False
                    return True
        
```



1928. Minimum Cost to Reach Destination in Time

> 一个国家有 `n` 个城市，城市编号为 `0` 到 `n - 1` ，题目保证 **所有城市** 都由双向道路 **连接在一起** 。道路由二维整数数组 `edges` 表示，其中 `edges[i] = [xi, yi, timei]` 表示城市 `xi` 和 `yi` 之间有一条双向道路，耗费时间为 `timei` 分钟。两个城市之间可能会有多条耗费时间不同的道路，但是不会有道路两头连接着同一座城市。
>
> 每次经过一个城市时，你需要付通行费。通行费用一个长度为 `n` 且下标从 **0** 开始的整数数组 `passingFees` 表示，其中 `passingFees[j]` 是你经过城市 `j` 需要支付的费用。
>
> 一开始，你在城市 `0` ，你想要在 `maxTime` **分钟以内** （包含 `maxTime` 分钟）到达城市 `n - 1` 。旅行的 **费用** 为你经过的所有城市 **通行费之和** （**包括** 起点和终点城市的通行费）。
>
> 给你 `maxTime`，`edges` 和 `passingFees` ，请你返回完成旅行的 **最小费用** ，如果无法在 `maxTime` 分钟以内完成旅行，请你返回 `-1` 。
>
> **示例 1：**
>
> ![](https://assets.leetcode.com/uploads/2021/06/04/leetgraph1-1.png)
>
> ```text
> 输入：maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
> 输出：11
> 解释：最优路径为 0 -> 1 -> 2 -> 5 ，总共需要耗费 30 分钟，需要支付 11 的通行费。
> ```
>
> **示例 2：**
>
> ![](https://assets.leetcode.com/uploads/2021/06/04/copy-of-leetgraph1-1.png)
>
> ```text
> 输入：maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
> 输出：48
> 解释：最优路径为 0 -> 3 -> 4 -> 5 ，总共需要耗费 26 分钟，需要支付 48 的通行费。
> 你不能选择路径 0 -> 1 -> 2 -> 5 ，因为这条路径耗费的时间太长。
> ```
>
> **示例 3：**
>
> ```text
> 输入：maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
> 输出：-1
> 解释：无法在 25 分钟以内从城市 0 到达城市 5 。
> ```
>
> **提示：**
>
> * `1 <= maxTime <= 1000`
> * `n == passingFees.length`
> * `2 <= n <= 1000`
> * `n - 1 <= edges.length <= 1000`
> * `0 <= xi, yi <= n - 1`
> * `1 <= timei <= 1000`
> * `1 <= passingFees[j] <= 1000` 
> * 图中两个节点之间可能有多条路径。
> * 图中不含有自环。

{% tabs %}
{% tab title="AC" %}
```python
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], pf: List[int]) -> int:
        n = len(pf)
        graph = collections.defaultdict(list)
        time = collections.defaultdict(int)
        dist = [[float("inf")] * 1010 for _ in range(1010)]
        st = [[False] * 1010 for _ in range(1010)]
        q = collections.deque()

        for x, y,t in edges:
            graph[x].append(y)
            graph[y].append(x)
            time[(x,y)] = t
            time[(y,x)] = t
            
        dist[0][0] = pf[0]
        q.append((0,0))
        while q :
            node, t = q.popleft()
            st[node][t]  = False
            if node == n - 1:
                print(dist[node][t])
            
            for nxt_node in graph[node]:
                newt = t + time[(nxt_node,node)]
                if newt > maxTime:
                    continue 
                    
                if dist[nxt_node][newt] > dist[node][t] + pf[nxt_node]:
                    print(newt,dist[node][t],pf[nxt_node],dist[nxt_node][newt])
                    dist[nxt_node][newt] = dist[node][t] + pf[nxt_node]
                    # 
                    
                    if not st[nxt_node][newt]:
                        st[nxt_node][newt] = True
                        q.append((nxt_node,newt))
                
        ans = min(dist[n - 1])
        return -1 if ans == float('inf') else ans
```
{% endtab %}

{% tab title="Python - TLE" %}
```python
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], pf: List[int]) -> int:
        n = len(pf)
        graph = collections.defaultdict(list)
        timecheck = collections.defaultdict(int)
        q = collections.deque()
        for x, y,time in edges:
            graph[x].append(y)
            graph[y].append(x)
            timecheck[tuple(sorted([x, y]))] = time
            
        fees = 0
        visited = set()
        # visited.add(0)
        q.append((0,-1,pf[0],0))
        ans = float("inf")
        while q:
            ls = len(q)
            for _ in range(ls):
                node, prev, fees, stime = q.popleft()
                # print(node, prev, fees, stime)
                if node == n - 1 and stime <=maxTime:
                    # print(fees)
                    ans = min(ans, fees)
                for nxt_node in graph[node]:
                    # print(nxt_node)
                    if nxt_node in visited:
                        continue 
                    q.append((nxt_node, node, fees + pf[nxt_node], stime + timecheck[tuple(sorted([node, nxt_node]))]))
            visited.add(node)
            
        return -1 if ans == float('inf') else ans
```
{% endtab %}
{% endtabs %}

