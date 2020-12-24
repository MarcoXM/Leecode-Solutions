# 面试题 01.04. 回文排列

{% tabs %}
{% tab title="python-bit" %}
```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        result = 0
        for c in s:
            result ^= 1<< ord(c)

        return result & (result - 1) == 0


```
{% endtab %}

{% tab title="Python" %}
```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        dit = {}
        for c in s:
            dit[c] = dit.get(c, 0) +  1

        cnt_odd = 0
        for v in dit.values():

            if v % 2 == 1:
                cnt_odd +=  1

            if cnt_odd > 1: return False

        return True
```
{% endtab %}
{% endtabs %}

