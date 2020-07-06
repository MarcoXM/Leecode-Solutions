# 剑指 Offer 10- I. 斐波那契数列

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0

        dp = (n + 1) * [0]
        dp[1] = 1
        for i in range(2,n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        # print(dp)
        return dp[n] % (10**9 + 7)
```

