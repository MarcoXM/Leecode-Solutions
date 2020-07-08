# 面试题 17.13. 恢复空格

{% tabs %}
{% tab title="DP" %}
```python
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        
        d = set(dictionary)
        dp = [0] * (len(sentence) + 1) ## 字符串还是要长度加1 
        for i in range(1,len(sentence) + 1):
            dp[i] = dp[i -1] + 1 ## 假设就是没有找到， 把值做大
            for j in range(i):
                if sentence[j:i] in d:
                    dp[i] = min(dp[i],dp[j])
            
        return dp[-1]
```
{% endtab %}

{% tab title="递归" %}
```python
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        lens = list({len(w) for w in dictionary})
        lens.sort(reverse = True)
        N, res, i = len(sentence), 0, 0
        ##　我真的觉得functoools 就像作弊。
        @functools.lru_cache(maxsize=1000)
        def dfs(i):
            if i == N : return 0
            res = []
            for l in lens:
                if i+l <= N and sentence[i:i+l] in dictionary:
                    res.append(dfs(i+l))
            res += [1+dfs(i+1)]
            return (min(res) if res else 0)

        return dfs(0)
```
{% endtab %}
{% endtabs %}

