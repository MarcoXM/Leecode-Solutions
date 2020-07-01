# may-20th

\683. Word Break II

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ## 就是打印路徑 
        wd = set(wordDict)
        ## 重點,二維數組表示記錄, 好啦 要邁向DP了 
        visited = [[-1] * len(s) for _ in range(len(s))]
        res = []
        self.dfs(0, s, res, [], wd, visited)
        return res

    def dfs(self, idx, s, res,  path, wd, visited):

        if idx == len(s):
            res.append(" ".join(path[:]))
            return 

        for i in range(idx + 1, len(s) + 1):
            if visited[idx][i-1] == 0:
                return
            if s[idx:i] not in wd:
                visited[idx][i-1] == 0
            elif s[idx:i] in wd and visited[idx][i-1] == -1:
                visited[idx][i-1] == 1 
                path.append(s[idx:i])
                self.dfs(i, s, res, path, wd, visited)
                path.pop()
                visited[idx][i-1] == -1
    ## 典型的所有技巧都用上, 都被暴打.....
```

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ## 就是打印路徑 
        wd = set(wordDict)
        res = {}
        ans = self.dfs(s, res, wd)
        return list(map(lambda x: x.strip(),ans))

    def dfs(self, s, res, wd):

        if s in res.keys():
            return res[s]
        if s == "": # 類比到了葉子,返回葉子value,爲什麼是[]? 因爲遞歸函數定義就是返回list
            return [""]
        path = []
        for w in wd:
            if s[:len(w)] != w:
                continue
            left = self.dfs(s[len(w):],res,wd)
            for sub in left:
                path.append(w + " " + sub)
        res[s] = path
        return res[s]

    ##　對於　經典例子　ａａａａａ　這裏便利ｗｏｒｄｄｉｃｔ，剪得明顯．
```

\683. Word Break II

```python
class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        res = {}
        d = set(map(lambda x:x.lower(),dict))
        return self.dfs(s.lower(),d,res)


    def dfs(self, s, wd, res):

        if s in res:
            return res[s]

        count = 0 ## root的值就是零,
        if s in wd: ## 操作就一個 數葉子 !
            count += 1

        ##　想明白以後就是求按要求劃分，最後畫出來的樹的葉子數目　

        if s == "":
            return 0

        if len(s) > len(wd):
            for w in wd:
                if s[:len(w)] != w:
                    continue
                count +=  self.dfs(s[len(w):], wd, res) # 原來遞歸ｌｉｓｔ，這裏就是數字
                    ## 這裏比沒有實際的操作, root 沒有操作 
            res[s] = count
        else:
            for i in range(1, len(s)):
                if s[:i] not in wd:
                    continue
                count += self.dfs(s[i:], wd, res )
            res[s] = count
        return res[s]
        ## 還是畫樹吧
```

