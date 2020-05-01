## april-29th

79. **Word Search**

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
 
        N, M = len(board),len(board[0])
        visited = [[0] * M for _ in range(N)]
        print(visited)
        for i in range(N):
            for j in range(M):
                if self.dfs(board,word,0,i,j,visited):
                    return True
        return False
    
    def dfs(self,board, word,idx, i, j,visited):
        N, M = len(board),len(board[0])
        # 终止条件
        if idx == len(word):
            return True
        if i < 0 or i >= N or j < 0 or j >= M or visited[i][j] or board[i][j] != word[idx]:
            return False
        
        ##  来过, 下一层, 取消
        visited[i][j] = True
        res = self.dfs(board, word ,idx +1, i+1, j,visited) or self.dfs(board, word ,idx +1, i-1, j,visited) or self.dfs(board, word ,idx +1, i, j+1,visited) or self.dfs(board, word ,idx +1, i, j -1,visited)
        visited[i][j] = False
        return res
    
    
    
```



124. **Binary Tree Maximum Path Sum**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ## 树肯定是DFS 优先
        ## 任何一个路径,都可转换转化为 root, root.left, rooteight 和本来function 递归调用不够,加helper
        
        
        ## 求值还是global 好
        self.g_max = -float('inf')
        
        def helper(root):
            if not root:　## 到了叶子
                return 0
        
            left = max(helper(root.left),0) # 防止小于零
            right = max(helper(root.right),0)
            self.g_max = max(self.g_max, root.val + left + right)　# 当前组合是否更优
            return max(left,right) + root.val ## 选左边的解还是右边
        
        helper(root)
        return self.g_max
```

