# 面试题 01.01. 判定字符是否唯一

{% tabs %}
{% tab title="non- dict" %}
```python
class Solution:
    def isUnique(self, astr: str) -> bool:
        
        mask = 0
        for c in astr:
            move = ord(c) - ord("a")
            if (mask & (1 << move)) :
                return False
            else:
                mask |= (1 << move)

        return True
        

            
```
{% endtab %}

{% tab title="Python" %}
```python
class Solution:
    def isUnique(self, astr: str) -> bool:
        
        dit = {}
        for c in astr:
            if c in dit:
                return False
            else:
                dit[c] = 1

        return True
        

            
```
{% endtab %}
{% endtabs %}

