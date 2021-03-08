# Untitled

```python

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        m = (n + k - 1)//k
        f = [[float("inf")] * 1024 for _ in range(k + 1)]
        f[0][0] = 0
        sumv = 0
        minv = float("inf")
        for i in range(1, k + 1):
            s = [0] * 1024
            l = m
            if n %k and n%k < i:l -= 1
            for j in range(l):
                s[nums[j *k + i - 1]] += 1
            maxv = 0
            for j in range(1024):
                if s[j]:
                    maxv = max(maxv , s[j])
            sumv += l - maxv
            minv = min(minv, maxv)
            for j in range(1024):
                for u in range(l):
                    x = nums[u * k + i - 1]
                    cost = l - s[x]
                    f[i][j] = min(f[i][j], f[i - 1][j ^ x] + cost)
            
        return min(minv + sumv, f[k][0])
```

