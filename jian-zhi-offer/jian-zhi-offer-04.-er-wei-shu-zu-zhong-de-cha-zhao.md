# 剑指 Offer 04. 二维数组中的查找

{% tabs %}
{% tab title="迭代" %}
```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:return False
        col = len(matrix[0]) - 1
        row = 0

        while row < len(matrix) and col >= 0:
            num = matrix[row][col]

            if num == target:
                return True

            elif num > target:
                col -= 1

            else:
                row += 1

        return False
```
{% endtab %}

{% tab title="递归" %}
```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        def dfs(row,col):
            if row == len(matrix) or col == -1:
                return False
            num = matrix[row][col]
            if num == target:
                return True
            elif num > target:
                return dfs(row,col - 1)
            else:
                return dfs(row + 1, col)

        col = len(matrix[0]) - 1
        row = 0
        return dfs(row,col)

```
{% endtab %}
{% endtabs %}



