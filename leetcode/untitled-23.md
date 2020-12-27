# 1705. Maximum Number of Eaten Apples

{% tabs %}
{% tab title="Python- 读题" %}
```python
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        ans = 0
        h = []
        i = 0
        while i < len(apples) or h:

            if i < len(apples) and apples[i] > 0:
                heapq.heappush(h , [i + days[i], apples[i]])

            while h and (h[0][0] <= i or h[0][1] == 0):
                heapq.heappop(h)

            if h:
                ans += 1
                h[0][1] -= 1

            i += 1


        return ans 
```
{% endtab %}

{% tab title="Python" %}
```python
class Solution:
    def eatenApples(self, A: List[int], days: List[int]) -> int:
        fin, i = 0, 0
        q = []
        while i<len(A) or q:
            if i<len(A) and A[i]>0:
                heapq.heappush(q, [i+D[i],A[i]])
            while q and (q[0][0]<=i or q[0][1]==0):
                heapq.heappop(q)
            if q:
                q[0][1] -= 1
                fin += 1
            i += 1
        return fin
```
{% endtab %}
{% endtabs %}

