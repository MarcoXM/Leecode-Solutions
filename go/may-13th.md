# may-13th

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ## preprocessing the data into list
        s1 = version1.split('.')
        s2 = version2.split('.')

        ## Padding [0] and keep both of them with same length
        max_len = max(len(s1),len(s2))
        s1 = self.zeroPadding(s1,max_len)
        s2 = self.zeroPadding(s2,max_len)
        i = 0

        ## Compare version
        while i < len(s1) and i<len(s2):
            if int(s1[i])== int(s2[i]):
                i += 1
            elif int(s1[i]) > int(s2[i]):
                return 1
            else:
                return -1
        return 0

    def zeroPadding(self,s,max_len):
        if len(s) < max_len:
            return s + [0] * (max_len -len(s))
        return s
```

```python
class Solution:
    """
    @param matrix: the height matrix
    @param R: the row of (R,C)
    @param C: the columns of (R,C)
    @return: Whether the water can flow outside
    """
    def waterInjection(self, matrix, R, C):
        # Write your code here

        stack = [(R, C)]
        visited = [[0] *len(matrix[0]) for _ in range(len(matrix))]

        while stack :
            x, y = stack.pop()
            visited[x][y] = 1

            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx, ny = x + dx , y + dy

                ## 先处理越界
                if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]):
                    return "YES"

                if visited[nx][ny] == 1:
                    continue 
                if matrix[nx][ny] < matrix[x][y]:

                    stack.append((nx,ny))

        return "NO"
```

