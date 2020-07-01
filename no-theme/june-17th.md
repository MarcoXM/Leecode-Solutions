# june-17th

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        step = 1
        N = n**2
        left,upper,right,down = 0,0,len(ans[0])-1,len(ans)-1
        i,j,idx = 0,0,0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        while step < N+1:
            ans[i][j] = step
            if j == right and idx == 0 :
                idx += 1
                upper += 1

            elif i == down and idx == 1 :
                idx += 1
                right -= 1

            elif j == left and idx == 2 :
                idx += 1
                down -= 1

            elif i == upper and idx == 3 :
                idx += 1
                left += 1

            ## 赋值
            idx = idx%4
            i, j = i + dirs[idx][0], j + dirs[idx][1]
            step += 1
        return ans
```

```python
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here

        ### 这题很迷...
        ### 没有空间,时间限制,不就是easy难度了 

        nums.sort()
        print(nums)
        l,r = 0,len(nums)-1
        ans = 0
        while l < r:
            while l > 0 and nums[l-1] == nums[l]:
                l += 1
            while r < len(nums)-1 and nums[r+1] == nums[r]:
                r -= 1

            ## 测试例子确实很棒
            if l < r and nums[l] + nums[r] == target:
                print(l,r)
                ans += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1

        return ans
```

