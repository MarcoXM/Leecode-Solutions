# april-21th

1. **Factorial Trailing Zeroes**

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ## 这tm是数学题....
        ## 0产生 99 乘法表, 2*5 10 
        count = 0
        while n > 0:
            if n%5 ==0:
                n //= 5
                count += n
            else:
                n-=1
        return count
```

135**1. Count Negative Numbers in a Sorted Matrix**

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # sorted in non-increasing order
        # 那我们就可以找上界0
        # 行二分 
        # 这是easy??

        if not grid:
            return 0
        m,n = len(grid),len(grid[0])
        count = 0
        idx = 0
        for i in range(m-1,-1,-1):
            if grid[i][0] < 0 :
                count += n
            else:
                idx = self.BSupper(grid[i],idx)
                count += (n - idx)
        return count

    def BSupper(self,nums,idx):
        l,r = idx,len(nums)
        while l < r:
            mid = (r+l)//2
            if nums[mid] < 0:
                r = mid
            else:
                l = mid + 1

    # 0(nlogn)
```

1. **Friend Circles**

```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ## 图的表征
        ## 链表 ,感觉可以回溯

        visited = [0] *len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(i, M, visited)
                count += 1
        return count

    def dfs(self,idx,M,visited):
        for j in range(len(M)):
            if M[idx][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(j,M,visited)

    # 0(n^2)
```

