# april-15th

1. **Trapping Rain Water**

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        ## 将问题 model化 
        ## 针对每一个方块,作为分界点,左边与右边的 数值比较,得出较小的值,再做差
        ## 方法是O(N^2)
        N = len(height)
        l, r = 0, N - 1
        ans = 0
        left_height, right_height = 0, 0 

        while l < r:
            if height[l] < height[r] : # 左边小一点,我们就用小的来遍历
                ### 避免 2 0 0 0 0 0 0 3 情况
                if height[l] >= left_height:
                    left_height = height[l]
                else:
                    ans += left_height - height[l] # 左高点,比现在指针位置高,所以height[i]上方可以纯水
                l += 1 # 移动指针

            else:
                if height[r] >= right_height:
                    right_height = height[r]
                else:
                    ans += right_height - height[r]
                r -= 1

        return ans # 空间(1) 时间(N)




class Solution:
    def trap(self, height: List[int]) -> int:
        ## 将问题 model化 
        ## 针对每一个方块,作为分界点,左边与右边的 数值比较,得出较小的值,再做差
        ## 方法是O(N^2)
        N = len(height)
        stack = []
        ans = 0
        for i in range(N):
            while stack and  height[stack[-1]] < height[i]: # 就是比较现在和上一个.如果现在小,证明上方可以存水
                ##  ##
                ###### 
                #s#p#i
                high_node = stack.pop()
                if stack:
                    ans += (min(height[i], height[stack[-1]]) - height[high_node])*(i - stack[-1] - 1)

            ### Loop 第一步    
            stack.append(i) 
        return ans


 ##最差情况单调递减，　空间(N)
```

