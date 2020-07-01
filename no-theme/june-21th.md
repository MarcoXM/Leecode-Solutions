# june-21th

\202. Happy Number

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        ## 这题真的就是算法...
        ##　
        dit = collections.defaultdict(int)
        def sqSum(n):
            if dit.get(n) != None:
                return dit.get(n)
            s = 0
            for i in str(n):
                s += int(i)**2
            dit[n] = s
            return s

        slow = n
        fast = n # 快慢指针

        while True:
            slow = sqSum(slow)
            fast = sqSum(sqSum(fast))

            if fast == slow:
                break

        return slow == 1
```

\1488. Avoid Flood in The City

```python
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ## 这题累比应该是sotr k linked list

        ## rain,记录下雨ith 天 by lake
        rain = collections.defaultdict(collections.deque)
        ans = []
        drain_order = []
        history = set()
        ## 预处理
        for i, v in enumerate(rains):
            rain[v].append(i)

        for day, lake in enumerate(rains):
            if lake > 0 :
                if lake in history:
                    ## 还没来得及排水..
                    return []
                ## 这个lake 满了
                history.add(lake)
                rain[lake].popleft()
                ans.append(-1)
                if rain[lake]:
                    ## 后面这个湖还要下雨,将要下雨的时间push 进heap
                    heapq.heappush(drain_order,rain[lake][0]) 

            else:
                if drain_order:
                    ## 要排水了,找到最先的天
                    d = heapq.heappop(drain_order)
                    ans.append(rains[d]) 
                    history.remove(rains[d])

                else:

                    ans.append(1) ## 随便加
        return ans
```

