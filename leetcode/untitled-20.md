# 1702. Maximum Binary String After Change

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maximumBinaryString(self, s: str) -> str:        
        ones = zeros = 0
        ans = []
        for c in s:
            if c == "0":
                zeros += 1
                
            elif zeros == 0:
                ones += 1
            ans.append("1")
            
        if ones < len(s):
            ans[ones + zeros - 1] = "0"
            
        return "".join(ans)
```
{% endtab %}

{% tab title="Python" %}
```python
def maximumBinaryString(self, s):
        k, n = s.count('1', (s + '0').find('0')), len(s)
        return '1' * (n - k - 1) + '0' + '1' * k
```
{% endtab %}
{% endtabs %}

