# 面试题 01.07. 旋转矩阵

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]


        for i in range(len(matrix)):
            self.reverse(matrix[i])

       



    def reverse(self, l):
        i = 0 
        j = len(l) - 1
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1

        
```

ss

