## may-14th

\125. Valid Palindrome

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''.join([i.lower() for i in s if i.isalpha() or i.isdigit()])
        return ans[::-1]==ans
    ## 无脑内存版本 
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## 双指针版本,仿肖老师结构写法 
        if not s: return True
        l, r = 0, len(s) - 1
        ## 注意区间, 注意细节, 只要走到一个idx就可
        while l < r:
            while l < r and not s[l].isalpha() and not s[l].isdigit():
                l += 1
            while  l < r and not s[r].isalpha() and not s[r].isdigit():
                r -= 1
            if  l < r and s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return l >= r
        return True
        
```



```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ## 感觉要用数据结构,单纯指针很慢 
        ## 输出int 
        ## 统计
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        ans = 0  
        ##统计结果分类讨论
        for k,v in d.items():
            if v%2 ==0:
                ans += v
            elif v%2 == 1 and ans%2 == 0:
                ans += v
            elif v%2 == 1:
                ans += v - 1
                
        return ans
```



```Python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ## 感觉要用数据结构,单纯指针很慢 
        ## 输出int 
        ## 统计
        ans = 0
        odd = 0
        for c in set(s):
            if s.count(c)%2 == 0:
                ans += s.count(c)  
            else:
                ans += s.count(c)-1
                odd = 1
        return ans + odd
    ## 这个方法速度更快,内置count by C
```



**\912. Sort an Array**

Quick Sort

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums,0,len(nums)-1)
        return nums
        
    def quickSort(self, A, start, end):
        left , right = start, end
        
        pivot = (left + right)//2

        ## 递归出口
        if start >= end : return
        while left <= right: ## 双闭区间
            ### 一定要思考终止后指针的位置及对应元素的状态
            while left <= right and A[left]<A[pivot]:
                left += 1 # 其实就是没交换
            
            while left <= right and A[right]>A[pivot]:
                right -= 1
                
            if left <= right: # A[left] >A[pivot] 同时A[right]<A[pivot]
                A[left],A[right] = A[right],A[left]
                left += 1
                right -= 1
        # 还是那句 注意边界
        self.quickSort(A,start,right)
        self.quickSort(A,left,end)
```

mergeSort

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0 , len(nums))
        return nums
        
    def mergeSort(self, A, left, right):
        ## 终止,只有一个元素
        if left >= right-1 :
            return 

        mid = (left + right)//2
        # print(left,right)
        ## 还是边界问题
        ## 左闭右开什么破事都没
        self.mergeSort(A,left,mid)
        self.mergeSort(A,mid, right)
        self.merge(A, left, mid, right)
        
    def merge(self, A, start, mid, end):
        left, right = start, mid #　两端array右起点
        temp = []
        while left < mid and right < end:
            if A[left] <= A[right]:
                temp.append(A[left])
                left += 1
            else :
                temp.append(A[right])
                right += 1
        while left < mid :
            temp.append(A[left])
            left += 1
        while right < end:
            temp.append(A[right])
            right += 1
        A[start:end] = temp
                
        
        
```

