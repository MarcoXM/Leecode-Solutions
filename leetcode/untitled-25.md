# Untitled

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        f = [ i for i in range(len(edges) + 1)]
        ## 并查集真的万能
        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            fx = find(x)
            fy = find(y)
            if fx != fy:
                f[fy] = fx
        

        for x, y in edges:
            if find(x) == find(y):
                return [x,y]
            else:
                union(x,y)

```
{% endtab %}
{% endtabs %}

