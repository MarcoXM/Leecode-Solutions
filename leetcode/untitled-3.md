# Untitled

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pa = []
        rever = {}
        ans = []
        for i,v in enumerate(words):
            rever[v[::-1]] = i
            if v == v[::-1]:
                pa.append(i)


        for i, v in enumerate(words):
            if v:
                for j in range(len(v)):
                    l , r = v[:j],v[j:]
                    # AA B
                    if r == r[::-1] and l in rever and i != rever[l]:
                        ans.append([i, rever[l]])


                    if l == l[::-1] and r in rever and i != rever[r]:
                        ans.append([rever[r], i])
                    # 同理
                    
            else:
                for p in pa:
                    if p != i:
                        ans.append([i, p])

        return ans
```
{% endtab %}

{% tab title="TLE" %}
```python
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = [] 
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j :
                    continue
                if words[i] + words[j] == (words[i] + words[j])[::-1]:
                    # print(i,j)
                    ans.append([i,j])
        return ans
```
{% endtab %}
{% endtabs %}

