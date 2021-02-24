# 1619. Mean of Array After Removing Some Elements

{% tabs %}
{% tab title="Python-game" %}
```python

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        return sum(arr[ int(n*0.05):int(n*0.95)])/(0.9*n)
```
{% endtab %}
{% endtabs %}

