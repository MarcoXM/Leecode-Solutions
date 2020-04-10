## april-9th

146. **LRU Cache**

```python
class LRUCache:
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if self.cache.get(key) == None:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
        
    def put(self, key: int, value: int) -> None:
        if self.cache.get(key) != None:
            self.cache.pop(key)
        elif len(self.cache) == self.cap:
            self.cache.popitem(last=False)
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```



```go
type DLinkedList struct {
    key int
    value int
    prev *DLinkedList
    next *DLinkedList   
}

type LRUCache struct {
    capacity int
    head *DLinkedList
    tail *DLinkedList
    cache map[int]*DLinkedList
}

func Constructor(capacity int) LRUCache {
    return LRUCache {
        capacity: capacity,
        cache :   make(map[int]*DLinkedList),
    }
}


func (this *LRUCache) Get(key int) int {
    l,ok := this.cache[key]
    if !ok {
        return -1
    }
    this.removeFromChain(l)
    this.addToChain(l)
    return l.value
}


func (this *LRUCache) Put(key int, value int)  {
    l, ok := this.cache[key]
    if !ok {
        l = &DLinkedList{key:key,value:value} // return address
        this.cache[key] = l
    } else {
        l.value = value
        this.removeFromChain(l)
    }
    
    this.addToChain(l)
    
    if len(this.cache) > this.capacity {
        l := this.tail
        this.removeFromChain(l)
        delete(this.cache,l.key)
    }
    
}

func (this *LRUCache) addToChain(l *DLinkedList){
    l.next = nil
    if this.head != nil {
        this.head.next = l 
        l.prev = this.head //head > l > others
    } 
    this.head = l
    if this.tail == nil {
        this.tail = l
    }
}

func (this *LRUCache) removeFromChain(l *DLinkedList){
    
    if l == this.head {
        this.head = l.prev
    }
    if l == this.tail {
        this.tail = l.next
    }
    if l.next != nil {
        l.next.prev = l.prev
    }
    if l.prev != nil {
        l.prev.next = l.next
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
```


 680. **Split String**
```python
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """
    def splitString(self, s):
        # write your code here
        ans = []
        seq = []
        if not s:
            ans.append(seq)
            return ans
        ## 第一感觉这是dp 一步两步
        ## 发现不会 ,那就搜索DFS吧
 
        def helper(idx,seq=[]):
            if idx == len(s):
                ans.append(seq)
                return    # 终止条件
            
            for i in range(1,3): ## 只能取 1 或 2
                if idx + i <= len(s): ## 区间右开
                    helper(idx+i,seq + [s[idx:idx+i]]) ## 确保seq 本身没被修改
        helper(0)
        return ans
```



17. **Letter Combinations of a Phone Number**

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dit = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        ans = []
        if not digits:
            return ans
        
        def dfs(idx,seq):
            if idx == len(digits):
                ans.append(seq)
                return 
            
            for i in (dit[digits[idx]]):
                dfs(idx+1,seq+i)
        dfs(0,"")        
        return ans
        
```



```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return 
        candidates.sort()
        ans = []        
        self.dfs(candidates, target, 0, ans, [])
        return ans
        
    def dfs(self, nums, target, index, res, path):
        if target < 0: # 结果超出了target
            return
        elif target == 0: # 先写终止
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[index] > target:
                return
            self.dfs(nums, target - nums[i], i, res, path + [nums[i]])

```

```go
import "sort"
var ans [][]int
func combinationSum(candidates []int, target int) [][]int {
    
    sort.Ints(candidates) // sort
    ans = make([][]int,0) //二维数组
    dfs([]int{}, 0,candidates, target) // []int{} 定义了type没有赋值
    return ans
}

func dfs(seqSum []int, idx int, candidates []int, target int ) {
    //先写终止
    if target == 0 {
        ans = append(ans,seqSum)
    } else if target > 0{
        for i:= idx; i < len(candidates);i++ {
            if candidates[idx] > target {
                break
            } else {
                temp := make([]int, 0, len(seqSum)+1)
                temp = append(temp,seqSum...) // 一定要这样形成新切片,copy,不然原seq会被修改
                dfs(append(temp,candidates[i]),i,candidates,target - candidates[i])
            }
        }
    }
}
```



40. **Combination Sum II**

```python
## 暴力魔改,超时
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ## 每个元素只能用一次
        candidates.sort()
        ans = set()
        self.dfs(ans, [], 0, candidates, target)
        return list(ans)
        
    def dfs(self,ans,seq,idx,c,t):
        if t == 0 :
            if tuple(seq) not in ans:
                ans.add(tuple(seq))
            return 
        elif t < 0:
            return 
        for i in range(idx,len(c)):
            if c[idx] > t:
                return
            self.dfs(ans,seq,i+1,c,t) # 选
            self.dfs(ans,seq + [c[i]],i+1,c,t-c[i]) # 不选
            

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ## 每个元素只能用一次
        candidates.sort()
        ans = []
        self.dfs(ans, [], 0, candidates, target)
        return list(ans)
        
    def dfs(self,ans,seq,idx,c,t):
        if t == 0 :
            if seq not in ans:
                ans.append(seq)
            return 
        elif t < 0:
            return 
        for i in range(idx,len(c)):
            if c[idx] > t:
                return
            if i > idx and c[i] == c[i-1]: # while i == idx,总是加
                #数组常见去重复的方法，对于重复的数值，我们只让第一个进入循环，后面的就不要再进入循环了
                continue
            self.dfs(ans,seq + [c[i]],i+1,c,t-c[i])
            

###
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ## 如何用dp来做呢?
        ## a(n) = a(n-1)
        ## n[ints] = n-1[ints] + c[n]  
        
        ### 转移方程
        for i in range():
            
        
        
        ### 存储解构
        
        
        
        
        ### 复用
            
        return dp[-1]
```



78.**Subsets**

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if not nums:
            return res
        for i in range(len(nums)):
            for seq in res[:]:
                res.append(seq + [nums[i]])
        return res
    
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if not nums:
            return res
        for i in range(len(nums)):
            res.extend(list(map(lambda x: x + [nums[i]],res[:]))) # pythonic
        return res
    
### 回溯 
## 用回溯算法!
## 其实回溯算法关键在于:不合适就退回上一步
## 然后通过约束条件, 减少时间复杂度.
## 适合排列组合子集 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(idx, tmp):
            res.append(tmp) ### 
            for j in range(idx, n): # 
                helper(j + 1,tmp + [nums[j]] ) ## 完成下一个,并生成新的temp 子集 
        helper(0, [])
        return res  
    
    
    ## 1 我们直接来用[1,2,3] 说明例子
     1 在return上面call helper 会发生什么.
        首先result会加入一个空[].
        开始loop >>> j == 0
        	tmp 还是空list tmp : [] ---->>>> tmp:[] + [1] 
                tmp + [1] 传到helper 进行下一个loop 因为此时j == 2 
            注意在我们尚在进行的循环里面 tmp 还是 []
            此时j == 2, 这指的是还是在第一层的loop里或者说是root为[]. root.next 为 1,2,3 的节点循环里.此时 tmp 为 [], 所以 tmp + [element] 可以产生 [] + [2], [] + [3].
            我传[] + [3] 不就跳过 [2] 了吗.
            同理 适用用与 [] + [1] + [3] .
            这里是root 为 [] 的树的遍历.
            
     
        ## 回到正题.如果我们不用tmp + [element传参]
        换位 
    
```



90. Subsets II

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        nums.sort()
        def helper(idx,tmp):
            res.append(tmp)
            
            for j in range(idx,N):
                if j > idx and nums[j] == nums[j-1]:
                    continue
                helper(j+1,tmp + [nums[j]])
                
        helper(0,[])
        return res
```



46. **Permutations**

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 
        ans = []
        N = len(nums)
        def helper(left_nums,temp_list,length):
            if length == N:
                ans.append(temp_list)
            # 超时,超memry,不能传array
            for j in range(len(nums)):
                helper(left_nums[:j] + left_nums[j+1:],temp_list + [nums[j]],length + 1)
        helper(nums,[],0)
        return ans
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 
        ans = []
        N = len(nums)
        visited = [0]*N ##记录是否用过
        def helper(temp_list,length): ##参数要变，要让for j loop 变成range N
            if length == N:  ### 终止条件不变的
                ans.append(temp_list)
                
            for j in range(N):
                if visited[j] == 1:
                    continue
                visited[j] = 1
                helper(temp_list + [nums[j]],length + 1)
                visited[j] = 0 # 回溯 

        helper([],0)
        return ans
```







```python

##　Challenge
##　Can you do it without recursion?
## 这不就是的要求我们用recursive
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # write your code here
        res = []
        M = [-1] * n # 一维数组表达queens 位置 idx 行, values col
        
        def bt(q_row,temp):
            if q_row == n: # 满queen
                res.append(self.decode(temp))
                
            for i in range(n):
                if self.isValid(temp, q_row,i):
                    temp[q_row] = i # 定义 该queen 的col
                    bt(q_row + 1,temp[:]) ## call
                    temp[q_row] = -1 ## 回溯
        bt(0,M)
        return res
    
    def isValid(self,tmp,row,col):
        ## 不能同行 
        for i in range(row): ## 肯定就找false快啦
            if tmp[i]== col or abs(row - i) == abs(col - tmp[i]):
                return False
        ## 不能同列
        ## 不能对角线
        return True
    
    def decode(self,m):
        M = [['.' for _ in range(len(m))] for _ in range(len(m))]
        # print(M,m)
        for i,v in enumerate(m):
            M[i][v]= 'Q'
        return list(map(lambda x : "".join(x),M))
            
    
    
        
```

