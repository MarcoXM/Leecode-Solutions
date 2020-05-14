## Two Pointer



1. 双指针问题总结:

   1. 相向双指针：

      Two Sum 问题及其变种：

      Two Sum III - Data Structure Design  https://www.lintcode.com/problem/two-sum-iii-data-structure-design/?_from=ladder&&fromId=1

      ```python
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
              ## add(5) >>> self.cache {5:0} self.buff = [5]
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
          
          ## 这题系统设计非常经典,明白了cache 的作用和本身的结构
      ```

      

      Two Sum II - Input Array is Sortedhttps://leetcode.com/problems/two-sum-ii-input-array-is-sorted

      ```python
      class Solution:
          def twoSum(self, numbers: List[int], target: int) -> List[int]:
              ##　sorted in ascending order
              ## where index1 must be less than index2. 引诱我们双指针？
              ## 然后这是查找题,就要像是不是binary search 也可以做
              ## 但是list 都sorted 了, 不用 binarySearch 不是开玩笑吗
              
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
      ```

      

      3Sumhttps://leetcode.com/problems/3sum

      ```python
      class Solution:
          def threeSum(self, nums: List[int]) -> List[List[int]]:
              
              ## 做这题前你肯定要做过 2 sum 呀!!! 没做就来做
              ## 简单的做法就是2 sum 外面套 一个循环 
              ## 而且这个是和为零, 就是说 a + b = - c
              nums.sort()
              res = set()
              for i, v in enumerate(nums[:-2]):
                  
                  # 开始2sum
                  if i >= 1 and v == nums[i-1]: # 
                      continue # pass
                  d = {}
                  for x in nums[i+1:]: # 
                      if x not in d:
                          d[-v-x] = 1
                      else:
                          res.add((v, -v-x, x))
              return map(list, res)
      ```

      

   2. 二分法类问题：

      Find First and Last Position of Element in Sorted Arrayhttps://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

      ````python
      class Solution:
          def searchRange(self, nums: List[int], target: int) -> List[int]:
              ### 这个 must be in the order of O(log n).
              ### 还有就是都sorted了, 那肯定得二分. 
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
              
              ### 这个是模仿 stl 的逻辑
              ### 分别做两次bs, 找出上界和下界
              while l < r: # 终止条件 l == r
                  mid = (l + r )//2
                  if nums[mid] < target:
                      l = mid + 1
                  elif nums[mid] >= target:
                      r = mid 
              left_index = l
              
              ### 找出下界判断一下,避免无畏的两次搜索 
              if nums[left_index] != target:
                  return [-1,-1]
              
              
              l , r = 0 , len(nums) ## 区间 左闭右开 
              while l < r:
                  mid = (l + r )//2
                  if nums[mid] <= target: 
                      l = mid + 1 # 向上缩小空间
                  elif nums[mid] > target:
                      r = mid 
                      
              right_index = l - 1 # 因为最后 mid 加了1
              
              return [left_index, right_index]
                  
      ````

      

      Peak Index in a Mountain Arrayhttps://leetcode.com/problems/peak-index-in-a-mountain-array/

      ```python
      class Solution:
          def peakIndexInMountainArray(self, A: List[int]) -> int:
              ### 还是首先要明白的是这个 peak 是什么定义
              ### 就是max的index,然后A 也必定是山
              ### 有序的查找, 二分
              ### 找什么呢? d[i] > d[i-1]的lower bound ,或者是前端的upper bound
              
              l, r = 0, len(A) - 1 # [) 单调递增不可能
              while l < r:
                  mid = (l+r)//2
                  ## 更新区间
                  ## mid == 无意义的,可以去掉
                  if A[mid] <= A[mid + 1]:
                      l = mid + 1
                  else:
                      r = mid   
              return l ## 这里已经加1了
                      
                      
              
      ```

      

      Find K Closest Elementshttps://leetcode.com/problems/find-k-closest-elements/

      ```python
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
                  if x - arr[mid] > arr[mid+k]-x:
                      l = mid+1
                  else:
                      r = mid
              return arr[l:l+k]
              
              
      ```

      

      Find Minimum in Rotated Sorted Arrayhttps://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

      ```python
      class Solution:
          def findMin(self, nums: List[int]) -> int:
              l, r = 0, len(nums)-1 ## 区间 [) 这里没有target
              while l < r:
                  mid = (l + r)//2
                  ## mid 大于 right 
                  if nums[mid] > nums[r]: 
                      l = mid+1
                  else:
                      r = mid
              return nums[l] # 终止条件 l == r 
      
              
      ```

      

      Find Peak Elementhttps://leetcode.com/problems/find-peak-element/

      ```python
      class Solution:
          def findPeakElement(self, nums: List[int]) -> int:
              ## Your solution should be in logarithmic complexity.
              ## 二分了
              l , r = 0 , len(nums) -1 ## 保证mid + 1 不越界
              
              while l < r:
                  mid = (l + r)//2
                  if nums[mid] < nums[mid + 1]:
                      l = mid + 1
                  else:
                      r= mid
              return l 
      
      ```

      

      Search in a Big Sorted Array https://www.lintcode.com/problem/search-in-a-big-sorted-array/description?_from=ladder&&fromId=

      Find Bad Versionhttps://leetcode.com/problems/first-bad-version/

      ```python
      # The isBadVersion API is already defined for you.
      # @param version, an integer
      # @return a bool
      # def isBadVersion(version):
      
      class Solution:
          def firstBadVersion(self, n):
              """
              :type n: int
              :rtype: int
              """
              r = 1
              while r <= n: ## 这是双闭 
                  mid = r + (n - r ) // 2
                  if isBadVersion(mid):
                      n = mid - 1
                  else:
                      r = mid + 1
              return r ## 依然二分 找下界
      ```

      

   3. Partition类问题：

      (QuickSort的延申)31. Partition Arrayhttps://www.lintcode.com/problem/partition-array/description?_from=ladder&&fromId=

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
                      i -= 1
                      
                  else:
                      i -= 1
              return i+1 ## 这就是找下界
      
      ```

      

      Sort Colorshttps://leetcode.com/problems/sort-colors

      ```python
      class Solution:
          def sortColors(self, nums: List[int]) -> None:
              """
              Do not return anything, modify nums in-place instead.
              """
              ##　Could you come up with a one-pass algorithm using only constant space
              
              ##
              zero_idx = 0
              i = 0
              two_idx = len(nums) - 1
              ## [2,0,2,1,1,0]
              ## [0,0,1,1,2,2]
              ## 在moving zero 学到0排头
              ## 这里就是翻转2排尾
              while i <= two_idx: # 这里two的时候右边区间开的,所以左右相等便是空
                  if nums[i] == 0:
                      nums[zero_idx],nums[i] = nums[i],nums[zero_idx]
                      zero_idx+=1
                      i+=1
                  elif nums[i] == 1:
                      i+=1
                  elif nums[i] == 2: # 对次跟换的元素要进行判定,i不增加
                      nums[two_idx],nums[i] = nums[i],nums[two_idx]
                      two_idx -= 1
      
      ```

      

       Kth Largest Element in an Array:https://leetcode.com/problems/kth-largest-element-in-an-array/

      ```python
      class Solution:
          def findKthLargest(self, nums: List[int], k: int) -> int:
              ## 首先要不quick sort 要不 merge 要不heapq
              
              p = random.choice(nums)
              nums1,nums2 = [],[]
              for i in range(len(nums)):
                  if nums[i]<p:
                      nums1.append(nums[i])
                      
                  elif nums[i]>p:
                      nums2.append(nums[i]) # 根据p 来将 nums 分成两堆qs 是排了再分,dc是分了再排
              # len(nums1) + len(nums2) < len(nums)
              if k <= len(nums2): # 大的这堆里面的数字个数,比K多,那么我们的k就在里面
                  return self.findKthLargest(nums2,k)
      
              if k > len(nums)-len(nums1): # 反之,K在小堆里面
                  return self.findKthLargest(nums1,k -(len(nums)-len(nums1)))#更新K 值
              return p 
          ##　肖思阳写法就优雅　
          
      ```

      

      Kth Smallest Element in a BST：https://leetcode.com/problems/kth-smallest-element-in-a-bst/

      ```python
      # Definition for a binary tree node.
      # class TreeNode:
      #     def __init__(self, x):
      #         self.val = x
      #         self.left = None
      #         self.right = None
      
      class Solution:
          def kthSmallest(self, root: TreeNode, k: int) -> int:
              
              ### intuitive 就是preorder 的第K个
              stack = [root]
              while True:
                  while root:
                      stack.append(root)
                      root = root.left ## 疯狂往左 
                  root = stack.pop()
                  k -= 1
                  if not k:
                      return root.val 
                  root = root.left
             ## 必背 
      ```

      

   4. Reverse类问题：151. Reverse Words in a Stringhttps://leetcode.com/problems/reverse-words-in-a-string

      ```python
      class Solution:
          def reverseWords(self, s: str) -> str:
              s = s.strip()
              return " ".join(s.split()[::-1])
      ```

      

      Reverse Stringhttps://leetcode.com/problems/reverse-string/

      ```python
      class Solution:
          def reverseString(self, s: List[str]) -> None:
              """
              Do not return anything, modify s in-place instead.
              """
              if not s:
                  return s 
              l = 0
              r = len(s)-1
              ### 这个必背
              while l < r:
                  s[r], s[l] = s[l],s[r]
                  l += 1
                  r -= 1
      ```

      

      Reverse Words in a String IIhttps://www.lintcode.com/problem/reverse-words-in-a-string-ii/

      ```python
      class Solution:
          """
          @param str: a string
          @return: return a string
          """
          def reverseWords(self, str):
              # write your code here
              w_list = str.split()
              
              new = []
              def helper(idx):
                  if idx < 0:
                      return
                  new.append(w_list[idx])
                  helper(idx-1)
                  
              helper(len(w_list)-1)
              return " ".join(new) # 递归 
      ```

      

2. 背向双指针：	658. Find K Closest Elementshttps://leetcode.com/problems/find-k-closest-elements/	
   
   上面有
   
3. 同向双指针：	

      1. 滑动窗口类：283. Move Zeroeshttps://leetcode.com/problems/move-zeroes

         ````python
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
         ````

         

          Remove Duplicates from Sorted Array https://leetcode.com/problems/remove-duplicates-from-sorted-array/ 

         ```python
         class Solution:
             def removeDuplicates(self, nums: List[int]) -> int:
                 if len(nums) == 0:
                     return 0
                 curr = 0
                 for i in range(len(nums)):
                     if nums[i] != nums[curr]:
                         curr+=1
                         nums[curr] = nums[i]
                 return curr+1
                 
         ```

         

      2. 快慢指针类：876. Middle of Linked Listhttps://leetcode.com/problems/middle-of-the-linked-list/

         ```python
         # Definition for singly-linked list.
         # class ListNode:
         #     def __init__(self, x):
         #         self.val = x
         #         self.next = None
         
         class Solution:
             def middleNode(self, head: ListNode) -> ListNode:
                 if not head:
                     return
                 
                 root = ListNode(-1)
                 root.next = head
                 s,f = head,head
                 ## 一步 两步, 我就套你的圈 
                 while f and f.next:
                     f = f.next.next
                     s = s.next
                     
                 return s
         ```

         

4. 三根指针：	264. Ugly Numbers IIhttps://leetcode.com/problems/ugly-number-ii/

      ```python
      class Solution:
          def nthUglyNumber(self, n: int) -> int:
              ## n does not exceed 1690
              ## 记录 已经有的 ugly # n th : value
              dp = [0] * n
              dp[0] = 1 ## 1 就是ugly
              num_2, num_3, num_5 = 0, 0, 0
              for i in range(1,n):      
                  u2, u3, u5 = 2 * dp[num_2], 3 * dp[num_3], 5 * dp[num_5]
                  dp[i] = min((u2, u3, u5))
                  ## 和stone game 相似,if不能用elif
                  if dp[i] == u2 : ##每个都加1
                      num_2 += 1
                  if dp[i] == u3:
                      num_3 += 1
                  if dp[i] == u5:
                      num_5 += 1
              return dp[-1]
      ```

      