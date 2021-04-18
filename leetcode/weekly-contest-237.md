# weekly-contest-237

1832. Check if the Sentence Is Pangram

```python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cnt = [0] * 26
        
        for c in sentence:
            cnt[ord(c) - ord("a")] += 1
            
        
        for c in cnt:
            if c == 0:
                return False
        return True
```

1833. Maximum Ice Cream Bars

```python

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for c in costs:
            if coins >= c :
                coins -= c
                ans += 1
                
            else:
                break
                
        return ans
```

1834. Single-Threaded CPU

```python
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        data = sorted((t[0],t[1],i) for i,t in enumerate(tasks))
        res = []
        idx = 0
        h = []
        time = data[0][0]
        while len(res) < len(data):
            while idx < len(data) and data[idx][0] <= time:
                heapq.heappush(h, (data[idx][1], data[idx][2]))
                idx += 1
            if h:
                p, i = heapq.heappop(h)
                res.append(i)
                time += p 
            elif idx < len(data):
                time = data[idx][0]
                
            
        return res
```

1835. Find XOR Sum of All Pairs Bitwise AND

```python
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(operator.xor, arr1) & reduce(operator.xor, arr2)
```

