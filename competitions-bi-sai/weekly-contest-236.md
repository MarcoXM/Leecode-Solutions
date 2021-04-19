# weekly-contest-236

1822. sign-of-the-product-of-an-array

> 已知函数 signFunc\(x\) 将会根据 x 的正负返回特定值：
>
> 如果 x 是正数，返回 1 。 如果 x 是负数，返回 -1 。 如果 x 是等于 0 ，返回 0 。 给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。
>
> 返回 signFunc\(product\) 。

```python
## 暴力
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for n in nums:
            ans *= n
            
            
        if ans > 0 :return 1
        elif ans < 0 :return - 1
        return 0
```

1823. find-the-winner-of-the-circular-game

> 共有 n 名小伙伴一起做游戏。小伙伴们围成一圈，按 顺时针顺序 从 1 到 n 编号。确切地说，从第 i 名小伙伴顺时针移动一位会到达第 \(i+1\) 名小伙伴的位置，其中 1 &lt;= i &lt; n ，从第 n 名小伙伴顺时针移动一位会回到第 1 名小伙伴的位置。
>
> 游戏遵循如下规则：
>
> 从第 1 名小伙伴所在位置 开始 。 沿着顺时针方向数 k 名小伙伴，计数时需要 包含 起始时的那位小伙伴。逐个绕圈进行计数，一些小伙伴可能会被数过不止一次。 你数到的最后一名小伙伴需要离开圈子，并视作输掉游戏。 如果圈子中仍然有不止一名小伙伴，从刚刚输掉的小伙伴的 顺时针下一位 小伙伴 开始，回到步骤 2 继续执行。 否则，圈子中最后一名小伙伴赢得游戏。 给你参与游戏的小伙伴总数 n ，和一个整数 k ，返回游戏的获胜者。

```python

## 直接模拟就好了，数据量比较少，前两题都是暴力的做法 
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        nums = [i for i in range(1, n + 1)]
        start = 0
        while len(nums) > 1:
            l = len(nums)
            idx = (start + k - 1)% l
            nums = nums[:idx] + nums[idx + 1:]
            start = idx
            # print(nums)
            
        return nums[0]
```

1824. minimum-sideway-jumps

> 给你一个长度为 n 的 3 跑道道路 ，它总共包含 n + 1 个 点 ，编号为 0 到 n 。一只青蛙从 0 号点第二条跑道 出发 ，它想要跳到点 n 处。然而道路上可能有一些障碍。
>
> 给你一个长度为 n + 1 的数组 obstacles ，其中 obstacles\[i\] （取值范围从 0 到 3）表示在点 i 处的 obstacles\[i\] 跑道上有一个障碍。如果 obstacles\[i\] == 0 ，那么点 i 处没有障碍。任何一个点的三条跑道中 最多有一个 障碍。
>
> 比方说，如果 obstacles\[2\] == 1 ，那么说明在点 2 处跑道 1 有障碍。 这只青蛙从点 i 跳到点 i + 1 且跑道不变的前提是点 i + 1 的同一跑道上没有障碍。为了躲避障碍，这只青蛙也可以在 同一个 点处 侧跳 到 另外一条 跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。
>
> 比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。 这只青蛙从点 0 处跑道 2 出发，并想到达点 n 处的 任一跑道 ，请你返回 最少侧跳次数 。
>
> 注意：点 0 处和点 n 处的任一跑道都不会有障碍。
>
> 跨越跑道德成本无论多远都是1

```python
class Solution:
    def minSideJumps(self, obs : List[int]) -> int:

        f = [[0] * 3 for _ in range(len(obs))]
        f[0][0] = f[0][2] = 1
        f[0][1] = 0

        for i in range(1, len(obs)):
            for j in range(3):
                f[i][j] = float("inf")
                if obs[i] == j + 1: continue 
                for k in range(3):
                    if obs[i] == k + 1: continue
                    cost = 0 
                    if k != j : cost = 1
                    f[i][j] = min(f[i][j], f[i - 1][k] + cost)

        return min(f[-1])
```

1825. Finding MK Average

> 给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。
>
> MK 平均值 按照如下步骤计算：
>
> 如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。 从这个容器中删除最小的 k 个数和最大的 k 个数。 计算剩余元素的平均值，并 向下取整到最近的整数 。 请你实现 MKAverage 类：
>
> MKAverage\(int m, int k\) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。 void addElement\(int num\) 往数据流中插入一个新的元素 num 。 int calculateMKAverage\(\) 对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。

```python
from sortedcontainers import SortedList
class MKAverage():

    def __init__(self, m: int, k: int):
        self.l=SortedList()
        self.m=m
        self.k=k
        self.d=deque()
        self.s=0
        self.low=0
        self.high=0


    def addElement(self, num: int) -> None:
        if len(self.d)<self.m:
            self.d.append(num)
            self.s+=num
            self.l.add(num)
            if len(self.d)==self.m:
                self.low=sum(self.l[:self.k])
                self.high=sum(self.l[-self.k:])
            return
        
        self.d.append(num)
        p=self.d.popleft()
        displ=self.l.bisect_left(p)
        disph=self.l.bisect_right(p)
        self.l.discard(p)
        if displ<self.k:
            self.low-=p
            self.low+=self.l[self.k-1]
        if disph>self.m-self.k:
            self.high-=p
            self.high+=self.l[-self.k]
        self.s-=p
        self.s+=num
        pos=self.l.bisect_left(num)
        if pos<self.k:
            self.low-=self.l[self.k-1]
            self.low+=num
        if pos>=self.m-self.k:
            self.high-=self.l[-self.k]
            self.high+=num
        self.l.add(num)
        # print(self.l,num,pos,self.low,self.high)


    def calculateMKAverage(self) -> int:
        if len(self.d)<self.m:
            return -1
        # print('cal',self.l,self.low,self.high,self.s)
        return (self.s-self.low-self.high)//(self.m-2*self.k)



# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
```

