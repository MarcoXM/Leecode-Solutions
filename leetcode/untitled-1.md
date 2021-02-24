# 746. Min Cost Climbing Stairs

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float("inf")] * (n + 1)

        if n < 3: return cost[-1]

        dp[0] = 0
        dp[1] = 0

        for i in range(2,n + 1):
            for j in (1,2):
                dp[i] = min(dp[i],dp[i-j] + cost[i-j])
        # print(dp)
        return dp[-1]
```

