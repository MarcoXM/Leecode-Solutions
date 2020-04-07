# index

1. **First Bad Version**

   \`\`\`python

   **The isBadVersion API is already defined for you.**

   **def isBadVersion\(version\):**

class Solution: def firstBadVersion\(self, n\): """ :type n: int :rtype: int """ l = 1 while l &lt;= n: mid = l + \(n - l \) // 2 if isBadVersion\(mid\): n = mid - 1 else: l = mid + 1 return l

```text
## 这题 双闭区间, 关键是区间,不是是不是0开始
```

```text
34. **Find First and Last Position of Element in Sorted Array**

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ### 这个 must be in the order of O(log n).
        ### sorted 那就是二分法了 .
        ### 分开找两个边界 [) 
        if not nums:
            return [-1,-1]
        if target<nums[0] or target > nums[-1]:
            return [-1,-1]

        left_index = right_index = None
        l , r = 0 , len(nums)
        ## [5,7,7,8,8,10]
        ## [0,1,2,3,4,5] 
        while l < r: # 终止条件 l == r
            mid = (l + r )//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] >= target:
                r = mid 
        left_index = l
        if nums[left_index] != target:
            return [-1,-1]

        l , r = 0 , len(nums)
        while l < r:
            mid = (l + r )//2
            if nums[mid] <= target:
                l = mid + 1 # 向上缩小空间
            elif nums[mid] > target:
                r = mid 

        right_index = l - 1

        return [left_index, right_index]
```

1. **Peak Index in a Mountain Array**

```python
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        ## 看了下题目全正整数,没复杂度要求
        ## (1)
        return A.index(max(A))

        ## (2)
        ans = 0
        for i in range(len(A)):
            if A[i] >= ans:
                ans = A[i]
            else:
                return i-1

        ## 二分
        l, r = 0, len(A) -1 # 后面有mid + 1
        while l < r:
            mid = (l+r)//2
            ## 更新区间
            if A[mid] < A[mid + 1]:
                l = mid + 1
            else:
                r = mid   
        return l
```

1. **Find Minimum in Rotated Sorted Array**

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1 ## 区间 [] 这里没有target
        while l < r:
            mid = (l + r)//2
            ## mid 大于 right 
            if nums[mid] > nums[r]: 
                l = mid+1
            else:
                r = mid
        return nums[l] # 终止条件 l == r
```

1. **Find Peak Element**

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ## Your solution should be in logarithmic complexity.
        ## 二分了
        l , r = 0 , len(nums) -1 
        while l<r:
            mid = (l + r)//2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r= mid
        return l 
    ### 这也算mid? 找到一个peek
```

1. **Search in a Big Sorted Array** 

```python
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l,r = 0,1 
        while reader.get(r) < target:
            r *= 2
        # reader.get(r) 大于等于target
        ## 区间 []
        l = r//2
           while l <= r:
            mid = l + (r - l)//2
            v = reader.get(mid) ## 防止再call
            if v == target:
                return mid
            if v > target:
                l = mid - 1
            else:
                r = mid + 1 ## 双闭,区间 + - 1
        return -1
```

1. **Find K Closest Elements**

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ### 10^4 可以先排序
        return sorted(sorted(arr,key = lambda n : abs(n-x))[:k])

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:]

        l, r = 0, len(arr)-k
        ## 区间 [) 
        while l < r: ## 终止 == 
            mid = (l + r)//2
            ## [1,2,3,4,5]
            ## [0,1,2,3,4]
            ## first mid 0
            ## dis 
            ### 如何更新
            if abs(arr[mid] - x) > abs(arr[mid+k]-x):
                l = mid+1
            else:
                r = mid
        return arr[l:l+k]
```

