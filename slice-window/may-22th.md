# may-22th

\438. Find All Anagrams in a String

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        ## hash map 找東西必備,當然用26數組也行
        sdict = collections.defaultdict(int)
        pdict = {k : p.count(k) for k in p}
        l,r = 0,0 ## 左右指針
        match = 0 #多少個元素符合 
        while r < len(s):
            w = s[r]
            if w in pdict:
                sdict[w] += 1
                if sdict[w] == pdict[w]:
                    match += 1
            r += 1

            while match == len(pdict):
                if r - l == len(p):
                    ans.append(l)
                w1 = s[l]
                if w1 in pdict:
                    sdict[w1] -= 1
                    if sdict[w1] < pdict[w1]:
                        match -= 1
                l += 1
        return ans

     # O(N)
```

\3. Longest Substring Without Repeating Characters

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ### 維護一個unique 的滑動窗口
        sdict = collections.defaultdict(int)
        l, r = 0, 0 
        ans = 0
        while r < len(s):
            w = s[r] 
            sdict[w] += 1 # 遇到新字都家進去
            r += 1
            ## 一旦超過標準
            while sdict[w] > 1:
                w2 = s[l]
                sdict[w2] -= 1
                l += 1
            ans = max(ans,r - l)
        return ans
       ## 左右指針鏡像對稱
```

