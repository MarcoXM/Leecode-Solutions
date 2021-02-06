# 1751. Maximum Number of Events That Can Be Attended II

```python
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events, key = lambda x : x[1])
        f = [[0] * (k + 1) for _ in range(len(events) + 1)]
        ## 前i个区间中选j 个的最大值。
        
        for i in range(1, len(events) + 1):
            for j in range(1, k + 1):
                f[i][j] = f[i - 1][j]
                l = 0 
                r = i - 1
                while l < r :
                    mid = l + r + 1 >> 1
                    if events[mid - 1][1] < events[i - 1][0]: l = mid
                    else:r = mid - 1
                        
                f[i][j] = max(f[i][j],f[r][j - 1] + events[i - 1][2] )
                
        return f[-1][-1]
```

