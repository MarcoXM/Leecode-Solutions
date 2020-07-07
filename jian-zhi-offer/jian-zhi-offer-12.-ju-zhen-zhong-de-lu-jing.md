# 剑指 Offer 12. 矩阵中的路径

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if self.dfs(i, j , 0, board, word, visited):
                    return True
        return False

    def dfs(self,i,j, idx, board, word, visited):
        if idx == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in visited:
            return False
        
        if board[i][j] == word[idx]:
            # print(board[i][j], i,j,visited, idx)
            visited.add((i,j))
            ans = self.dfs(i + 1,j, idx + 1, board,word,visited) or self.dfs(i - 1, j, idx + 1, board,word,visited) or self.dfs(i ,j + 1, idx + 1, board,word,visited) or self.dfs(i, j - 1, idx + 1, board,word,visited)
            visited.remove((i,j)) ##　 撤销操作
            return ans
        return False 
        
```

