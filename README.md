# March 31

1. **Reverse String**\(翻转字符串\)

```text
    def reverseString(self, s: List[str]) -> None:        if not s: # Cornner Case            return s         l = 0 # 双指针        r = len(s)-1        while l < r: # 交换            s[r], s[l] = s[l],s[r]            l += 1            r -= 1    #时间复杂度Ｏ(N), 空间Ｏ(1)
```

1. **Implement strStr\(\)**

```text
class Solution:    def strStr(self, haystack: str, needle: str) -> int:        if not needle: # Corner Case            return 0          for ind in (i for i,e in enumerate(haystack) if e == needle[0]): # 找到起始match的index, 然后再判定.            if haystack[ind:ind + len(needle)] == needle:                return ind        return -1    #时间复杂度Ｏ(MN)
```

1. **Rotate String**

```text
​x​class Solution:    def rotateString(self, A: str, B: str) -> bool:        if not A and not B: # Corner Case            return True        for _ in range(len(A)): # 遍历去找            if A == B:                return True            A = self.shift(A) # 移一位        return False    def shift(self,str):        return str[1:] + str[0]     #时间复杂度Ｏ(N^2) 空间#时间复杂度Ｏ(N)
```

1. **Find All Duplicates in an Array**

```text
    def findDuplicates(self, nums: List[int]) -> List[int]:        ans = []        nums.sort()        n = 1        while n <= len(nums)-1:            if nums[n] == nums[n-1]:                ans.append(nums[n])                n += 1            n += 1        return ans    # nlogn + nclass Solution:    def findDuplicates(self, nums: List[int]) -> List[int]:        ans = []        # [4,3,2,7,8,2,3,1]         for n in nums:            if nums[abs(n) - 1] < 0 : # 为什么会nums[i] 负数,以为已经翻转过,dup就是这样找出来的                ans.append(abs(n))            else:                nums[abs(n)-1] = -nums[abs(n)-1]        # [-4, 3, 2, -7, 8, 2, -3, -1]        # 虽然很精巧, 但是跑下来时间 内存都没上一个好...        return ans
```

1. **Search a 2D Matrix II**

```text
# O(NM)class Solution:    def searchMatrix(self, matrix, target):        """        :type matrix: List[List[int]]        :type target: int        :rtype: bool        """        # 就是遍历        for i in range(len(matrix)):            for j in range(len(matrix[0])):                if matrix[i][j] == target:                    return True        return Falseclass Solution:    def searchMatrix(self, matrix, target):        """        :type matrix: List[List[int]]        :type target: int        :rtype: bool        """        if not matrix:            return False        def helper(up,down,left,right):            if left > right or up > down:                # 大过最大,小过最小那就算了                return False            # 先判定index 再看 values 不然就failed            elif target < matrix[up][left] or target > matrix[down][right]:                # index 超出界限                return False            mid = left + (right-left)//2            row = up            while row <= down and matrix[row][mid] <= target:                if matrix[row][mid] == target:                    return True                row += 1            return helper(row,down,left,mid-1) or helper(up,row-1,mid + 1,right)        return helper(0,len(matrix) - 1, 0, len(matrix[0]) - 1)
```

1. **Spiral Matrix**

```text
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:        ans = []        if not matrix or not matrix[0]: # Cornner Case [], [[]]            return ans        l,u,r,d = 0,0,len(matrix[0])-1,len(matrix)-1        i,j = 0,0        dirs = [(0,1),(1,0),(0,-1),(-1,0)]        ind = 0         while len(ans) < len(matrix[0])*len(matrix):            # print(i,j,d)            ans.append(matrix[i][j])            if j == r and ind == 0 :  # >>>>>> i不变, j ++                ind += 1                u += 1             elif i == d and ind == 1: # i ++,j不变                ind += 1                r -= 1            elif j == l and ind == 2: # <<<<<                ind += 1                d -= 1            elif i == u and ind == 3: # ^^^^^^^,i -- j 不变                ind += 1                l += 1            ind %=4            # update i,j index values            i += dirs[ind][0]            j += dirs[ind][1]         return ans
```

1. **Serialize and Deserialize Binary Tree**

```text
# Definition for a binary tree node.# class TreeNode(object):#     def __init__(self, x):#         self.val = x#         self.left = None#         self.right = None​    def serialize(self, root):        """Encodes a tree to a single string.        :type root: TreeNode        :rtype: str        """        ans = self.decode(root,[])        # print(ans)        return " ".join(ans) # 中间要变 str    def decode(self, root, ans):        if root is None:            ans.append("#") # 井号代空,大雾        else:            ans.append(str(root.val))            self.decode(root.left, ans)            self.decode(root.right,ans)    def deserialize(self, data):        """Decodes your encoded data to tree.        :type data: str        :rtype: TreeNode        """        data = data.split()    def encode(self,data_list):        '''        if data_list[0] == "#":            return None # corner case        root = TreeNode(data_list[0])        data_list.pop(0) # 用了就删掉        root.left = self.encode(data_list)        root.right = self.encode(data_list)        return root
```

