# 1774. Closest Dessert Cost

```python
class Solution:
    def closestCost(self, b: List[int], t: List[int], target: int) -> int:
        
        ans = 0
        # b.sort()
        # t.sort()
        seen = set()
        def dfs(value,jdx):
            if jdx == len(t):
                return 

            # seen.add(value)
            for j in range(0, 3):

                dfs(value + t[jdx] * j,jdx + 1)
                seen.add(value + t[jdx] * j)
                
        for i in range(len(b)):
            dfs(b[i],0)

        s = sorted(list(seen))
        b = sorted(b)
        if not s:
            return b[0]
        # print(s)
        idx = bisect.bisect_left(s,target)
        # print(idx,s[idx])
        if idx == len(s):
            return b[0]
        elif s[idx] == target:
            return target
        elif idx == 0:
            return s[0]
        else:
            if target - s[idx - 1] <= s[idx] - target:
                return s[idx - 1]
            else:
                return s[idx]
```

