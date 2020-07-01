# may-30th

\645. Set Mismatch

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ## 排序再根据 index 来搞省空间...但是排序 nlogn
        m = [0] * len(nums)
        for n in nums:
            m[n-1] += 1
        ans = [0,0]
        for i,e in enumerate(m):
            if e == 2:
                ans[0] = i + 1
            if e == 0:
                ans[1] = i + 1


        return ans
```

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ## 排序再根据 index 来搞省空间...但是排序 nlogn
        ans = [0,0]
        for n in nums:
            if nums[abs(n) - 1] < 0:
                ans[0] = abs(n)
            else:
                nums[abs(n) - 1] *= -1 ## 变负

        for i in range(len(nums)):
            if nums[i] > 0:
                ans[1] = i + 1

        return ans
```

\532. K-diff Pairs in an Array

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ## 取巧法
        ans = 0
        for x,y in set(itertools.combinations(sorted(nums),2)):
            if abs(x-y) == k:
                ans += 1
        return ans
```

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ## 取巧法
        ans = 0
        ## 分类讨论 注意边界 
        if k < 0:
            return ans
        dit = collections.defaultdict(int)
        for i in range(len(nums)):
            dit[nums[i]] += 1

        if k == 0:
            for n in dit.values():
                if n > 1:
                    ans += 1
        if k > 0:
            for n in dit.keys():
                if n + k in dit:
                    ans += 1

        return ans
```

