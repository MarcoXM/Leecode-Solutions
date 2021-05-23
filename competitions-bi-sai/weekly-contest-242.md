# weekly-contest-242



1869. Longer Contiguous Segments of Ones than Zeros

> 给你一个二进制字符串 `s` 。如果字符串中由 `1` 组成的 **最长** 连续子字符串 **严格长于** 由 `0` 组成的 **最长** 连续子字符串，返回 `true` ；否则，返回 `false` __。
>
> * 例如，`s = "`**`11`**`01`**`000`**`10"` 中，由 `1` 组成的最长连续子字符串的长度是 `2` ，由 `0` 组成的最长连续子字符串的长度是 `3` 。
>
> 注意，如果字符串中不存在 `0` ，此时认为由 `0` 组成的最长连续子字符串的长度是 `0` 。字符串中不存在 `1` 的情况也适用此规则。



```python
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        a = max(list(map(len,s.split("0"))))
        b = max(list(map(len,s.split("1"))))
        return a > b
        
```



1870. Minimum Speed to Arrive on Time

> 给你一个浮点数 `hour` ，表示你到达办公室可用的总通勤时间。要到达办公室，你必须按给定次序乘坐 `n` 趟列车。另给你一个长度为 `n` 的整数数组 `dist` ，其中 `dist[i]` 表示第 `i` 趟列车的行驶距离（单位是千米）。
>
> 每趟列车均只能在整点发车，所以你可能需要在两趟列车之间等待一段时间。
>
> * 例如，第 `1` 趟列车需要 `1.5` 小时，那你必须再等待 `0.5` 小时，搭乘在第 2 小时发车的第 `2` 趟列车。
>
> 返回能满足你准时到达办公室所要求全部列车的 **最小正整数** 时速（单位：千米每小时），如果无法准时到达，则返回 `-1` 。
>
> 生成的测试用例保证答案不超过 `107` ，且 `hour` 的 **小数点后最多存在两位数字** 。

```python
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        import math
        
        ans = - 1
        
        if hour < len(dist) - 1: return ans
        
        l = 1
        r = 10 ** 7
        
        def check(x):
            ans = 0
            for i in range(len(dist) - 1):
                ans += math.ceil(dist[i]/x)
            ans += dist[-1]/x
            return ans > hour
        
        
        while l < r :
            mid = l + r >> 1
            
            if check(mid) :
                l = mid + 1
            else:
                r = mid 
                
        return l
```

1871. Jump Game VII

> 给你一个下标从 **0** 开始的二进制字符串 `s` 和两个整数 `minJump` 和 `maxJump` 。一开始，你在下标 `0` 处，且该位置的值一定为 `'0'` 。当同时满足如下条件时，你可以从下标 `i` 移动到下标 `j` 处：
>
> * `i + minJump <= j <= min(i + maxJump, s.length - 1)` 且
> * `s[j] == '0'`.
>
> 如果你可以到达 `s` 的下标 `s.length - 1` 处，请你返回 `true` ，否则返回 `false` 。

```python
class Solution:
    def canReach(self, s: str, a: int, b: int) -> bool:
        
        
        ## 前缀和 !!!!
        n = len(s)
        f = [0] * (n + 1)
        p = [0]
        f[1] = 1
        p.append(1)
        
        for i in range(2, n + 1):
            if s[i-1] == "0" and i - a >= 1:
                l = max(1 , i - b)
                r = i - a
                if p[r] > p[l - 1]:
                    f[i] = 1
                    
            p.append(p[-1] + f[i])
        return bool(f[n])
                
```

1872.  Stone Game VIII

> Alice 和 Bob 玩一个游戏，两人轮流操作， **Alice 先手** 。
>
> 总共有 `n` 个石子排成一行。轮到某个玩家的回合时，如果石子的数目 **大于 1** ，他将执行以下操作：
>
> 1. 选择一个整数 `x > 1` ，并且 **移除** 最左边的 `x` 个石子。
> 2. 将 **移除** 的石子价值之 **和** 累加到该玩家的分数中。
> 3. 将一个 **新的石子** 放在最左边，且新石子的值为被移除石子值之和。
>
> 当只剩下 **一个** 石子时，游戏结束。
>
> Alice 和 Bob 的 **分数之差** 为 `(Alice 的分数 - Bob 的分数)` 。 Alice 的目标是 **最大化** 分数差，Bob 的目标是 **最小化** 分数差。
>
> 给你一个长度为 `n` 的整数数组 `stones` ，其中 `stones[i]` 是 **从左边起** 第 `i` 个石子的价值。请你返回在双方都采用 **最优** 策略的情况下，Alice 和 Bob 的 **分数之差** 。

```python


j = i - x 

j , j + 1, .... , i

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        
        stones = stones[::-1]
        n = len(stones)
        f = [0] * (n + 1)
        s = [0]
        for i in range(len(stones)):
            s.append(s[-1] + stones[i])
            
            
        
        v = s[n] - s[0] + f[1]
        for i in range(2, n + 1):
            f[i] = v 
            v = max(v, s[n] - s[i] - f[i])
            
        return f[n]
 
```



