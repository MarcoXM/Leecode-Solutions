# may-23th

\76. Minimum Window Substring

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ## 首先这是一道hard的题!
        ## 为什么是hard 比昨天难, 为什么咧?
        ## 因为返回要求的是str, 不是返回两个指针 diff 的最大值,
        ## 而是要记录具体指针的位置,然后返回
        start, l, r = 0, 0, 0
        windows = collections.defaultdict(int)
        tdict = {k:t.count(k) for k in t}
        match = 0
        minLen = 2 << 31
        while r < len(s):
            w = s[r]
            if w in tdict:
                windows[w] += 1
                if windows[w] == tdict[w]:
                    match += 1
            r += 1

            ## 集齐所有元素
            while match == len(tdict):
                if r - l < minLen:
                    minLen = r - l 
                    start = l # 更换ans 的起始index
                w2 = s[l]
                if w2 in tdict:
                    windows[w2] -= 1
                    if windows[w2] < tdict[w2]:
                        match -= 1
                l += 1
        return s[start:start + minLen] if minLen != 2 << 31 else ""
```

\30. Substring with Concatenation of All Words

```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ## 这个比上个更难是words 里面的order matters
        ## 窗口size 定了,改变一下,维护的windows 是word级别的,不是字母级别
        ## 词与词之间就无关了
        if not s or not words:
            return []
        wLen = len(words[0])
        wordsCount = collections.Counter(words)
        windowLen = wLen * len(words)
        ans = []
        for i in range(wLen):        ## 按单词长设点起点
            windows = collections.defaultdict(int)
            l, r = i, i
            match = 0
            while r + wLen <= len(s):
                w = s[r:r+wLen]
                if w in wordsCount:
                    windows[w] += 1
                    if windows[w] == wordsCount[w]:
                        match += 1
                else:
                    windows.clear() # python dict归零
                    match = 0
                    l = r
                r += wLen  ## 每次走词长
                while match == len(wordsCount):
                    if r - l == windowLen:
                        ans.append(l)
                    w2 = s[l:l+wLen]
                    if w2 in wordsCount:
                        windows[w2] -= 1
                        if windows[w2] < wordsCount[w2]:
                            match -= 1
                    l += wLen

        return ans
```

