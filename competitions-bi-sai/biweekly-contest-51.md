# biweekly-contest-51

总的来说本次双周赛就是手速场,可惜自己没有掌握增量算法,这周也算是学习了吧

1844. Replace All Digits with Characters

> 给你一个下标从 0 开始的字符串 s ，它的 偶数 下标处为小写英文字母，奇数 下标处为数字。
>
> 定义一个函数 shift\(c, x\) ，其中 c 是一个字符且 x 是一个数字，函数返回字母表中 c 后面第 x 个字符。
>
> 比方说，shift\('a', 5\) = 'f' 和 shift\('x', 0\) = 'x' 。 对于每个 奇数 下标 i ，你需要将数字 s\[i\] 用 shift\(s\[i-1\], s\[i\]\) 替换。
>
> 请你替换所有数字以后，将字符串 s 返回。题目 保证 shift\(s\[i-1\], s\[i\]\) 不会超过 'z' 。

```python
class Solution:
    def replaceDigits(self, s: str) -> str:
        ## 这题没什么好说的, 就是奇数位的地方shift一下
        ans = []
        for i in range(len(s)):
            if i & 1:
                ans.append(chr(ord(s[i-1]) + int(s[i])))
                
            else:
                ans.append(s[i])
                
        return "".join(ans)
```

1845. Seat Reservation Manager

> 请你设计一个管理 n 个座位预约的系统，座位编号从 1 到 n 。
>
> 请你实现 SeatManager 类：
>
> SeatManager\(int n\) 初始化一个 SeatManager 对象，它管理从 1 到 n 编号的 n 个座位。所有座位初始都是可预约的。 int reserve\(\) 返回可以预约座位的 最小编号 ，此座位变为不可预约。 void unreserve\(int seatNumber\) 将给定编号 seatNumber 对应的座位变成可以预约。

```python
class SeatManager:
    ## 初始化list做数据结构,heap做管理
    def __init__(self, n: int):
        
        self.h = [i + 1for i in range(n)]
        

    def reserve(self) -> int:
        x = heapq.heappop(self.h)
        return x

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
```

1846. Maximum Element After Decreasing and Rearranging

> 给你一个正整数数组 arr 。请你对 arr 执行一些操作（也可以不进行任何操作），使得数组满足以下条件：
>
> arr 中 第一个 元素必须为 1 。 任意相邻两个元素的差的绝对值 小于等于 1 ，也就是说，对于任意的 1 &lt;= i &lt; arr.length （数组下标从 0 开始），都满足 abs\(arr\[i\] - arr\[i - 1\]\) &lt;= 1 。abs\(x\) 为 x 的绝对值。 你可以执行以下 2 种操作任意次：
>
> 减小 arr 中任意元素的值，使其变为一个 更小的正整数 。 重新排列 arr 中的元素，你可以以任意顺序重新排列。 请你返回执行以上操作后，在满足前文所述的条件下，arr 中可能的 最大值 。

```python
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        ## 复盘时还是会不注意到a[0] 为1 , 估计这个条件是为了防止越界减少难度吧
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i ] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
                
            
        return arr[-1]
```

1847. Closest Room

> 一个酒店里有 n 个房间，这些房间用二维整数数组 rooms 表示，其中 rooms\[i\] = \[roomIdi, sizei\] 表示有一个房间号为 roomIdi 的房间且它的面积为 sizei 。每一个房间号 roomIdi 保证是 独一无二 的。
>
> 同时给你 k 个查询，用二维数组 queries 表示，其中 queries\[j\] = \[preferredj, minSizej\] 。第 j 个查询的答案是满足如下条件的房间 id ：
>
> 房间的面积 至少 为 minSizej ，且 abs\(id - preferredj\) 的值 最小 ，其中 abs\(x\) 是 x 的绝对值。 如果差的绝对值有 相等 的，选择 最小 的 id 。如果 没有满足条件的房间 ，答案为 -1 。
>
> 请你返回长度为 k 的数组 answer ，其中 answer\[j\] 为第 j 个查询的结果。

```python
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        
        ## 可以分别把房间和query按房间size整理 
        ## 减少数据量的使用就不会超时,如果数据量一开始就非常大,每次都要二分操作依然会很慢的
        
        ## 这里可以用lowerbound 就是_right, 这时找到的就是上界, 减一就是下界
        
        from sortedcontainers import SortedList
        
        qs = [(i, pre, ms) for i,(pre , ms) in enumerate(queries)]
        qs = sorted(qs, key = lambda x: x[2])
        rooms = sorted(rooms, key = lambda x: x[1])
        sl = SortedList([-float("inf"), float("inf")])
        ans = len(qs) * [0]
        j = len(rooms) - 1
        for i in range(len(qs) - 1, - 1, -1):
            idx, pre, ms = qs[i]
            while j >= 0 and rooms[j][1] >= ms :
                sl.add(rooms[j][0])
                j -= 1
            u = sl.bisect_right(pre)
            v = u - 1
            if sl[u] - pre < pre - sl[v]:
                ans[idx] = sl[u]
            else:
                ans[idx] = sl[v]
            if abs(ans[idx]) == float("inf"):
                ans[idx] = -1
        return ans


        
```



