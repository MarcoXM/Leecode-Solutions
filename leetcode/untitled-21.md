---
description: 勇夺2021最难周赛头名
---

# 1716. Calculate Money in Leetcode Bank

{% tabs %}
{% tab title="Math" %}
```python
class Solution:
    def totalMoney(self, n: int) -> int:
        m = (n-1)//7
        k = (n-1)%7+1
        sum1 = (28+28+(m-1)*7)*m//2
        sum2 = (m+1+m+k)*k//2
        return sum1+sum2
```
{% endtab %}

{% tab title="Python-模拟" %}
```python
class Solution:
    def totalMoney(self, n: int) -> int:
        m = 1
        week = 0
        ans = 0
        days = 0
        p_m = 0
### 模拟题不是算法， 那就一个地去模拟
        while n:
            if week%7 == 0:
                m = p_m + 1
                p_m = m
            else:
                m += 1
            ans += m   
            week += 1
            n -= 1
            
        return ans 
```
{% endtab %}
{% endtabs %}

