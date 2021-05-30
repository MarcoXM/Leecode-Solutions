# weekly-contest-243

1880. Check if Word Equals Summation of Two Words

> ```text
> 输入：firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
> 输出：true
> 解释：
> firstWord 的数值为 "aaa" -> "000" -> 0
> secondWord 的数值为 "a" -> "0" -> 0
> targetWord 的数值为 "aaaa" -> "0000" -> 0
> 由于 0 + 0 == 0 ，返回 true
> ```
>
> **示例 3：**
>
> ```text
> 输入：firstWord = "aaa", secondWord = "a", targetWord = "aab"
> 输出：false
> 解释：
> firstWord 的数值为 "aaa" -> "000" -> 0
> secondWord 的数值为 "a" -> "0" -> 0
> targetWord 的数值为 "aab" -> "001" -> 1
> 由于 0 + 0 != 1 ，返回 false
> ```
>
> **示例 2：**
>
> ```text
> 输入：firstWord = "acb", secondWord = "cba", targetWord = "cdb"
> 输出：true
> 解释：
> firstWord 的数值为 "acb" -> "021" -> 21
> secondWord 的数值为 "cba" -> "210" -> 210
> targetWord 的数值为 "cdb" -> "231" -> 231
> 由于 21 + 210 == 231 ，返回 true
> ```
>
> **示例 1：**
>
> 如果 `firstWord` __和 __`secondWord` 的 **数值之和** 等于 __`targetWord` __的数值，返回 `true` ；否则，返回 __`false` __。
>
> 给你三个字符串 `firstWord`、`secondWord` 和 `targetWord` ，每个字符串都由从 `'a'` 到 `'j'` （**含** `'a'` 和 `'j'` ****）的小写英文字母组成。
>
> * 例如，`s = "acb"` ，依次连接每个字母的字母值可以得到 `"021"` ，转换为整数得到 `21` 。
>
> 对某个由小写字母组成的字符串 `s` 而言，其 **数值** 就等于将 `s` 中每个字母的 **字母值** 按顺序 **连接** 并 **转换** 成对应整数。
>
> 字母的 **字母值** 取决于字母在字母表中的位置，**从 0 开始** 计数。即，`'a' -> 0`、`'b' -> 1`、`'c' -> 2`，以此类推。

```python
class Solution:
    def isSumEqual(self, x: str, y: str, z: str) -> bool:
        
        def trans(s):
            
            ans = 0
            for c in s:
                ans *= 10
                ans += ord(c) - ord('a')
                
            return ans 
        
        return trans(x) + trans(y) == trans(z)
```



1881. Maximum Value after Insertion

> 给你一个非常大的整数 `n` 和一个整数数字 `x` ，大整数 `n` 用一个字符串表示。`n` 中每一位数字和数字 `x` 都处于闭区间 `[1, 9]` 中，且 `n` 可能表示一个 **负数** 。
>
> 你打算通过在 `n` 的十进制表示的任意位置插入 `x` 来 **最大化** `n` 的 **数值** ​​​​​​。但 **不能** 在负号的左边插入 `x` 。
>
> * 例如，如果 `n = 73` 且 `x = 6` ，那么最佳方案是将 `6` 插入 `7` 和 `3` 之间，使 `n = 763` 。
> * 如果 `n = -55` 且 `x = 2` ，那么最佳方案是将 `2` 插在第一个 `5` 之前，使 `n = -255` 。
>
> 返回插入操作后，用字符串表示的 `n` 的最大值。
>
> **示例 1：**
>
> ```text
> 输入：n = "99", x = 9
> 输出："999"
> 解释：不管在哪里插入 9 ，结果都是相同的。
> ```
>
> **示例 2：**
>
> ```text
> 输入：n = "-13", x = 2
> 输出："-123"
> 解释：向 n 中插入 x 可以得到 -213、-123 或者 -132 ，三者中最大的是 -123 。
> ```
>
> **提示：**
>
> * `1 <= n.length <= 105`
> * `1 <= x <= 9`
> * `n`​​​ 中每一位的数字都在闭区间 `[1, 9]` 中。
> * `n` 代表一个有效的整数。
> * 当 `n` 表示负数时，将会以字符 `'-'` 开始。

```python
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            
            idx = 1
            while idx < len(n) and int(n[idx]) <= x:
                idx += 1
            return n[:idx] + str(x) + n[idx:]
        
        else: 
            idx = 0
            while idx < len(n) and int(n[idx]) >= x:
                idx += 1


            return n[:idx] + str(x) + n[idx:]
```



1882. Process Tasks Using Servers

> 给你两个 **下标从 0 开始** 的整数数组 `servers` 和 `tasks` ，长度分别为 `n`​​​​​​ 和 `m`​​​​​​ 。`servers[i]` 是第 `i​​​​​​`​​​​ 台服务器的 **权重** ，而 `tasks[j]` 是处理第 `j​​​​​​` 项任务 **所需要的时间**（单位：秒）。
>
> 你正在运行一个仿真系统，在处理完所有任务后，该系统将会关闭。每台服务器只能同时处理一项任务。第 `0` 项任务在第 `0` 秒可以开始处理，相应地，第 `j` 项任务在第 `j` 秒可以开始处理。处理第 `j` 项任务时，你需要为它分配一台 **权重最小** 的空闲服务器。如果存在多台相同权重的空闲服务器，请选择 **下标最小** 的服务器。如果一台空闲服务器在第 `t` 秒分配到第 `j` 项任务，那么在 `t + tasks[j]` 时它将恢复空闲状态。
>
> 如果没有空闲服务器，则必须等待，直到出现一台空闲服务器，并 **尽可能早** 地处理剩余任务。 如果有多项任务等待分配，则按照 **下标递增** 的顺序完成分配。
>
> 如果同一时刻存在多台空闲服务器，可以同时将多项任务分别分配给它们。
>
> 构建长度为 `m` 的答案数组 `ans` ，其中 `ans[j]` 是第 `j` 项任务分配的服务器的下标。
>
> 返回答案数组 __`ans`​​​​ 。
>
> **示例 1：**
>
> ```text
> 输入：servers = [3,3,2], tasks = [1,2,3,2,1,2]
> 输出：[2,2,0,2,1,2]
> 解释：事件按时间顺序如下：
> - 0 秒时，第 0 项任务加入到任务队列，使用第 2 台服务器处理到 1 秒。
> - 1 秒时，第 2 台服务器空闲，第 1 项任务加入到任务队列，使用第 2 台服务器处理到 3 秒。
> - 2 秒时，第 2 项任务加入到任务队列，使用第 0 台服务器处理到 5 秒。
> - 3 秒时，第 2 台服务器空闲，第 3 项任务加入到任务队列，使用第 2 台服务器处理到 5 秒。
> - 4 秒时，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 5 秒。
> - 5 秒时，所有服务器都空闲，第 5 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。
> ```
>
> **示例 2：**
>
> ```text
> 输入：servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
> 输出：[1,4,1,4,1,3,2]
> 解释：事件按时间顺序如下：
> - 0 秒时，第 0 项任务加入到任务队列，使用第 1 台服务器处理到 2 秒。
> - 1 秒时，第 1 项任务加入到任务队列，使用第 4 台服务器处理到 2 秒。
> - 2 秒时，第 1 台和第 4 台服务器空闲，第 2 项任务加入到任务队列，使用第 1 台服务器处理到 4 秒。
> - 3 秒时，第 3 项任务加入到任务队列，使用第 4 台服务器处理到 7 秒。
> - 4 秒时，第 1 台服务器空闲，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 9 秒。
> - 5 秒时，第 5 项任务加入到任务队列，使用第 3 台服务器处理到 7 秒。
> - 6 秒时，第 6 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。
> ```
>
> **提示：**
>
> * `servers.length == n`
> * `tasks.length == m`
> * `1 <= n, m <= 2 * 105`
> * `1 <= servers[i], tasks[j] <= 2 * 105`

```python
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        ## 权重最小
        res = []
        avail = sorted([(weight, idx , 0) for idx, weight in enumerate(servers)])
        busy = []

        # heapq.heapify(avail)
        
        for idx in range(len(tasks)):
            # print(idx,busy)
            while busy and busy[0][0]<= idx: ## have mission 
                avail_time,server_weight,server_idx = heapq.heappop(busy)
                heapq.heappush(avail,(server_weight,server_idx,avail_time))
            # print("avail", avail)
            if len(avail):
                
                server_weight, server_idx, avail_time = heapq.heappop(avail)
                res.append(server_idx)
                heapq.heappush(busy,(idx + tasks[idx],server_weight,server_idx))
                
            else :
                avail_time,server_weight,server_idx = heapq.heappop(busy)
                res.append(server_idx)
                heapq.heappush(busy,(avail_time + tasks[idx],server_weight,server_idx))
            # print("used",server_idx,tasks[idx])
        return res
            
                
                
                

```



1883. Minimum Skips to Arrive at Meeting On Time

> 给你一个整数 `hoursBefore` ，表示你要前往会议所剩下的可用小时数。要想成功抵达会议现场，你必须途经 `n` 条道路。道路的长度用一个长度为 `n` 的整数数组 `dist` 表示，其中 `dist[i]` 表示第 `i` 条道路的长度（单位：**千米**）。另给你一个整数 `speed` ，表示你在道路上前进的速度（单位：**千米每小时**）。
>
> 当你通过第 `i` 条路之后，就必须休息并等待，直到 **下一个整数小时** 才能开始继续通过下一条道路。注意：你不需要在通过最后一条道路后休息，因为那时你已经抵达会议现场。
>
> * 例如，如果你通过一条道路用去 `1.4` 小时，那你必须停下来等待，到 `2` 小时才可以继续通过下一条道路。如果通过一条道路恰好用去 `2` 小时，就无需等待，可以直接继续。
>
> 然而，为了能准时到达，你可以选择 **跳过** 一些路的休息时间，这意味着你不必等待下一个整数小时。注意，这意味着与不跳过任何休息时间相比，你可能在不同时刻到达接下来的道路。
>
> * 例如，假设通过第 `1` 条道路用去 `1.4` 小时，且通过第 `2` 条道路用去 `0.6` 小时。跳过第 `1` 条道路的休息时间意味着你将会在恰好 `2` 小时完成通过第 `2` 条道路，且你能够立即开始通过第 `3` 条道路。
>
> 返回准时抵达会议现场所需要的 **最小跳过次数** ，如果 **无法准时参会** ，返回 `-1` 。
>
> **示例 1：**
>
> ```text
> 输入：dist = [1,3,2], speed = 4, hoursBefore = 2
> 输出：1
> 解释：
> 不跳过任何休息时间，你将用 (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 小时才能抵达会议现场。
> 可以跳过第 1 次休息时间，共用 ((1/4 + 0) + (3/4 + 0)) + (2/4) = 1.5 小时抵达会议现场。
> 注意，第 2 次休息时间缩短为 0 ，由于跳过第 1 次休息时间，你是在整数小时处完成通过第 2 条道路。
> ```
>
> **示例 2：**
>
> ```text
> 输入：dist = [7,3,5,5], speed = 2, hoursBefore = 10
> 输出：2
> 解释：
> 不跳过任何休息时间，你将用 (7/2 + 1/2) + (3/2 + 1/2) + (5/2 + 1/2) + (5/2) = 11.5 小时才能抵达会议现场。
> 可以跳过第 1 次和第 3 次休息时间，共用 ((7/2 + 0) + (3/2 + 0)) + ((5/2 + 0) + (5/2)) = 10 小时抵达会议现场。
> ```
>
> **示例 3：**
>
> ```text
> 输入：dist = [7,3,5,5], speed = 1, hoursBefore = 10
> 输出：-1
> 解释：即使跳过所有的休息时间，也无法准时参加会议。
> ```
>
> **提示：**
>
> * `n == dist.length`
> * `1 <= n <= 1000`
> * `1 <= dist[i] <= 105`
> * `1 <= speed <= 106`
> * `1 <= hoursBefore <= 107`

```python
class Solution:
    def minSkips(self, dist: List[int], speed: int, hour: int) -> int:
       ##  f[i][j] ## i段路， 然后 j 次操作 
        import math
        eps = 1e-8
        inf = 10**9
        
        ## 操作i f[i - 1][j] + di/speed 
        
        f = [[0] * 1010 for _ in range(1010)]
        n = len(dist)
        
        for i in range(1, n + 1):
            t = dist[i - 1]/speed
            for j in range(i + 1):
                f[i][j] = inf 
                if j <= i - 1:
                    f[i][j] = math.ceil(f[i- 1][j] + t - eps)
                if j :
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + t)
                    
        for i in range(n + 1):
            if f[n][i] <= hour:
                return i
            
        return -1
        
               
        
    
    
```

