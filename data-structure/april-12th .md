## april-12th



Two Sum III - **Data structure design**

```PYTHON
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        from collections import defaultdict
        self.cache = defaultdict(int)
    
    def add(self, number):
        # write your code here
        ## add(5) >>> self.cache {5:0} 
        self.cache[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        ## 最难就是两个一样
        for k in self.cache.keys(): 
            if k == value-k:
                if self.cache.get(value-k) > 1:
                    return True
            else :
                if self.cache.get(value-k):
                    return True
        return False
    
    # 插入0(1),查找O(N)
```



283. **Move Zeroes**

```PYTHON
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        
        zi = 0
        ### 由于原来array 就sorted
        ### 一定要读题呀，这是都是非负整数，提供的而外信息就是要利用
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zi],nums[i] = nums[i],nums[zi]
                zi+=1 # zi 就是 不为零的数的idx
                
   # time  O(n), space  O(1)
```



Two Sum II - Input Array is Sorted

```python

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ##　sorted in ascending order
        ## where index1 must be less than index2. 引诱我们双指针？
        ## 然后这是查找题,就要像是不是binary search 也可以做 
        
        if not numbers:
            return [-1,-1]
        l,r = 0,len(numbers) - 1       
        for l in range(len(numbers)-1):
            r = self.bs(l+1,len(numbers),target - numbers[l],numbers)
            # print(l,r)
            if l < r:
                return [l+1,r+1]
            
        return [-1,-1]
             
    def bs(self,l,r,val,nums):
        while l < r:
            mid = (l+r)//2
            if nums[mid] == val:
                return mid
            elif nums[mid] < val:
                l = mid + 1
            else:
                r = mid    
        return -1
    
    ### 做完是真的搞笑,这idx 为啥不是0 起的 时间O(NlgN) 空间O(1)
    ## 直接用双指针也行
```



15. **3Sum**

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ## 3个相加就是 加法结合律,和2sum差不多 多一个loop.
        ## 然后还要打印结果
        ## 回溯
        nums.sort()
        res = []
        
        def helper(idx,ans,level):
            if level == 3 and sum(ans) == 0:
                res.append(ans)
            if level > 3 or sum(ans) > 0:
                return 
            for i in range(idx,len(nums)):# 最前面的 非两个
                if i >idx and nums[i] == nums[i-1]: # 
                    continue # pass
                helper(i+1,ans + [nums[i]],level + 1)
        ans = []
        helper(0,ans,0)
        return res
    
    ## 做法是没问题的,但是超时了,优化搜索效率,或者这样就是要利用空间记录
            
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ## 3个相加就是 加法结合律,和2sum差不多 多一个loop.
        ## 然后还要打印结果
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: 
                continue # 
            i, j = k + 1, len(nums) - 1
            ## 下面就是 2 sum 的逻辑
            while i < j: 
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1 # 小了大一点
                    while i < j and nums[i] == nums[i - 1]:#去重
                        i += 1
                elif s > 0:
                    j -= 1 # 打了小一点
                    while i < j and nums[j] == nums[j + 1]: #去重
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res
##  
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):# 开始2sum
            if i >= 1 and v == nums[i-1]: # 
                continue # pass
            d = {}
            for x in nums[i+1:]: # 
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)
            
            
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ##　Could you come up with a one-pass algorithm using only constant space
        
        ##
        zero_idx = 0
        i = 0
        two_idx = len(nums)
        ## [2,0,2,1,1,0]
        ## [0,0,1,1,2,2]
        ## 在moving zero 学到0排头
        ## 这里就是翻转2排尾
        while i < two_idx: # 这里two的时候右边区间开的,所以左右相等便是空
            
            if nums[i] == 0:
                nums[zero_idx],nums[i] = nums[i],nums[zero_idx]
                zero_idx+=1
                i+=1
            elif nums[i] == 1:
                i+=1
            elif nums[i] == 2: # 对次跟换的元素要进行判定,i不增加
                two_idx -= 1
                nums[two_idx],nums[i] = nums[i],nums[two_idx]

                    
            
            
```



31. **Partition Array**

```python
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        l, r = 0,len(nums)
        i = len(nums) -1
        
        ## 反向遍历,类比二分当时找lower_bound
        
        while l <= i:
            if nums[i]<k :
                nums[i],nums[l]= nums[l],nums[i]
                l += 1 
                
            elif nums[i] > k:
                r -= 1
                nums[i],nums[r]= nums[r],nums[i]
                print(nums)
                i -= 1
                
            else:
                i -= 1
        return i+1

```

