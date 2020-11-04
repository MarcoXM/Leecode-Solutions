# Untitled

```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        ## 这题是要最优root
## 我们不需要知道最优是多少。 层次遍历就是好的选择 
        if n == 1: return [0]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
            
        q = collections.deque()
        for i in range(n):
            if indegree[i] == 1: q.append(i)
        res = []
        while q :
            ls = len(q)
            res = []
            for _ in range(ls):
                node = q.popleft()
                res.append(node)
                for nxt in graph.get(node):
                    indegree[nxt] -= 1
                    if indegree[nxt] == 1: q.append(nxt)
                        
        return res
        
```

