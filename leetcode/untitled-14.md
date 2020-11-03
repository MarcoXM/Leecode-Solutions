# Untitled

```python
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        pre_sum = [[0] * m for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                pre_sum[i + 1][j] = pre_sum[i][j] + matrix[i][j]


        res = 0
        for row_start in range(n):
            for row in range(row_start,n):
                dit = {}
                sum_ = 0
                for col in range(m):
                    sum_ += pre_sum[row + 1][col] - pre_sum[row_start][col]
                    if sum_ == target:
                        res += 1
## 关键在于 sum_ - target 不是target - sum_

                    if sum_ - target in dit:
                        res += dit[sum_ - target]

                    if sum_ in dit:
                        dit[sum_] = dit.get(sum_) + 1

                    else:
                        dit[sum_] = 1

        return res

```

