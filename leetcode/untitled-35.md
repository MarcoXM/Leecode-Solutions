# 1802. Maximum Value at a Given Index in a Bounded Array

```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
    
    ## 有单调性就能二分
        lo = 1 ## positive 
        hi = maxSum
        while lo < hi:
            mi = hi - (hi - lo) // 2
            if self.helper(n, index, mi) <= maxSum:
                lo = mi
            else:
                hi = mi - 1
        return lo
    def helper(self, n, index, T):
        # T, T - 1, T - 2, ...
        # T, T - 1, T - 2, ...
        return T + self.helper2(index, T) + self.helper2(n - index - 1, T)
    def helper2(self, cnt, frm):
        # from - 1, from - 2, ..., from - cnt
        
        ## 底座  小 
        if cnt < frm:
            return frm * cnt - ((cnt * (cnt + 1))//2)
        # from-1,...,1,1,1,1
        
        ## 底座大
        return (frm*(frm-1))//2+cnt-frm+1
```

