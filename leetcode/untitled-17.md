# Untitled

{% tabs %}
{% tab title="dfs" %}
```python
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ## 转一下算一步
        ## 按一下算一步 
        
        dit = collections.defaultdict(list)
        for idx in range(len(ring)):
            dit[ring[idx]].append(idx)

        
        @functools.lru_cache(None)
        def dfs( cur_idx, k ):
            if k == len(key):
                return 0
            res = float("inf")
            for idx in dit[key[k]]:
                tmp = abs(cur_idx - idx) ## 海象毫无必要
                res = min(res, min(tmp, len(ring) - tmp) + 1 + dfs(idx, k + 1))
            return res

        return dfs(0, 0 )


```
{% endtab %}

{% tab title="Plain Text" %}
```python
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ## 转一下算一步
        ## 按一下算一步 
        n = len(ring)
        m = len(key)
        dp = [[float("inf")] * n for _ in range(m)]
        ##  ring
        ## k
        ## e
        ## y 
        ##自由之路真的难
        dit = collections.defaultdict(list)
        for i in range(len(ring)):
            dit[ring[i]].append(i)

        for idx in dit[key[0]]:
            dp[0][idx] = min(idx , n - idx) + 1 ## 因为是 0 based 所以要 + 1

        for i in range(1, m):
            for word_now_idx in dit[key[i]]:
                for pre_word_idx in dit[key[i-1]]:

                    dp[i][word_now_idx] = min(dp[i][word_now_idx],  ## 和自己以前的结果比较 
                                    dp[i-1][pre_word_idx] + min(abs(pre_word_idx - word_now_idx),n - abs(pre_word_idx - word_now_idx)) + 1)


        return min(dp[-1])




```
{% endtab %}
{% endtabs %}

