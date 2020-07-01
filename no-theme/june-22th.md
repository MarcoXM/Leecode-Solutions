# june-22th

\22. Generate Parentheses

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## 典型的dfs 找路径 
        ## return list 就是路径和
        res = []
        self.getParenth(0, 0, n,[],res)
        return res

    def getParenth(self,l , r, n, path, res):
        if len(path) == n * 2:
            res.append("".join(path[:]))
            return

        ## 难点在于怎么遍历到下一课树,他和前面的状态有关
        if l < n :
            self.getParenth(l + 1,r,n,path + ["("],res) 
        if r < l :
            self.getParenth(l,r + 1,n,path + [")"],res)
```

\973. K Closest Points to Origin

```python
## quick select 已经忘了... 晚点再温习吧
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ### top k 还是heap吧
        ## 转化
        p = list(map(lambda x: ((x[0]**2 + x[1]**2),x),points))
        heapq.heapify(p)
        ans = []
        while K > 0:
            ans.append(heapq.heappop(p)[1])
            K -= 1

        return ans
```

