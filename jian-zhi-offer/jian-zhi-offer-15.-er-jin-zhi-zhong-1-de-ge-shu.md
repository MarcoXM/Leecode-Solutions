# 剑指 Offer 15. 二进制中1的个数

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += 1
            n = n&(n - 1)

        return ans 
```

