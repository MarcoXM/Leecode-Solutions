## may-19th



```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        visited = [-1] * len(s)
        return self.dfs(0, s, wd,visited)
        
    def dfs(self, idx, s,wd,visited):
        if idx == len(s):
            return True
        if visited[idx] != -1:
            return visited[idx]
        
        for i in range(idx+1,len(s)+1): 
            if (s[idx:i] in wd) and self.dfs(i,s,wd,visited):
                visited[idx] = 1
                return True
        visited[idx] = 0
        return False
    
    
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        
        wd = set(wordDict)
        visited = [0] * len(s)
        ## 這題就是 真假, 找不着得到東西
        
        q = collections.deque()
        q.append(0)
        while q:
            node = q.popleft() ## 換一下又是DFS
            if visited[node] == 1:
                continue
            
            for i in range(node+1,len(s)+1):
                if s[node:i] in wd:
                    q.append(i)
                    
                    ## 恰巧走到最後 
                    if i == len(s):
                        return True
            ## 成功掃描完畢
            visited[node] = 1
            
        return False
```

\120. **Triangle**

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        ## 既然是path 那就dfs
        return self.dfs(0, 0, triangle)
        
        
        
    def dfs(self,level, idx, nums):
        if level == len(nums) - 1: # 到葉子了
            return nums[level][idx]
        
        ## 對比 root.left 
        left = self.dfs(level+1,idx,nums)
        right =  self.dfs(level+1,idx + 1,nums)
        root = nums[level][idx] + min(left,right)
        
        ## 後序
        return root 
        
```

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        ## 既然是path 那就dfs
        visited = [[-1] *(i+1) for i in range(len(triangle))]
        return self.dfs(0, 0, triangle,visited)
        
        
        
    def dfs(self,level, idx, nums,visited):
        if level == len(nums) - 1: # 到葉子了
            return nums[level][idx]
        
        if visited[level][idx]!=-1:
            return visited[level][idx]
        
        ## 對比 root.left 
        left = self.dfs(level+1,idx,nums,visited)
        right =  self.dfs(level+1,idx + 1,nums,visited)
        root = nums[level][idx] + min(left,right)
        visited[level][idx] = root
        
        ## 後序
        return root 
        
 class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ## 下到上
        dp = [0] * len(triangle[-1])
        dp[:] = triangle[-1]
        ## 行
        for i in range(len(triangle)-2,-1,-1):
            ## 列,
            for j in range(0, i+1):
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]
        return dp[0]
        
```





