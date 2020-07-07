# 剑指 Offer 14- I. 剪绳子

{% tabs %}
{% tab title="贪心" %}
```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4: return n - 1
        a, b = n // 3, n % 3
        if b == 0: 
            return pow(3, a)
        elif b == 1:
            return pow(3, a - 1) * 4
        else: 
            return pow(3, a) * 2

```
{% endtab %}

{% tab title="DP" %}
```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
        dp[2] = 1  # 初始化
        res = -1
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
        return dp[n]

```
{% endtab %}
{% endtabs %}

