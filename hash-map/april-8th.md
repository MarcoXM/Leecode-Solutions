# april-8th

1. **Moving Average from Data Stream**

   \`\`\`python

   class MovingAverage:

   """

   @param: size: An integer

   """

   def **init**\(self, size\):

   **do intialization if necessary**

      self.size = size

      self.l = \[\]

```text
"""
@param: val: An integer
@return:  
"""
@property 
def avg(self):
    return sum(self.l)/len(self.l)

def next(self, val):
    if len(self.l)< self.size:
        self.l.append(val)
    else:
        self.l.append(val)
        self.l = self.l[1:]

    return self.avg

    # write your code here
```

## Your MovingAverage object will be instantiated and called as such:

## obj = MovingAverage\(size\)

## param = obj.next\(val\)

```text
387. **First Unique Character in a String**

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        dit = {}
        for i in range(len(s)):
            if s[i] not in dit:
                dit[s[i]] = 1
            else:
                dit[s[i]] += 1

        for i in range(len(s)):
            if dit[s[i]] == 1:
                return i
        return -1
```

```go
func firstUniqChar(s string) int {
    if len(s) == 0 {
        return -1

    }
    var dit = make(map[string]int) //构建dit values 为int 单个
    for _,v := range s {
        dit[string(v)]++  //v 不是string
    }
    for i,v := range s {
        if dit[string(v)] == 1 {
            return i
        }
    }
    return -1
}
```

1. **Insert Delete GetRandom O\(1\)**

```python
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        ## 因为array 的插入是O(n)
        self.dit = {}
        self.list = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.dit.get(val) == None:
            self.list.append(val)
            self.dit[val] = len(self.list)- 1 ## 记录index
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.dit.get(val) == None:
            return False
        else:
            self.dit[self.list[-1]] = self.dit[val]
            self.list[self.dit[val]],self.list[-1] = self.list[-1],self.list[self.dit[val]]
            self.list.pop()
            del self.dit[val]
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.list)>0:
            return random.choice(self.list)
        return 0

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

```go
type RandomizedSet struct {
    list []int
    dict map[int]int
}


/** Initialize your data structure here. */
func Constructor() RandomizedSet {
    return RandomizedSet{
        list:  make([]int, 0),
        dict: make(map[int]int),
    }
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {//this 就是self突然觉得self 很中二
    if _,ok := this.dict[val]; ok{
        return false
    }
    this.list = append(this.list,val)
    this.dict[val] = len(this.list) - 1
    return true
}


/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
    if i,ok := this.dict[val];ok{
        // list 最后的元素,改dict 位置信息
        this.dict[this.list[len(this.list)-1]] = i

        //交换 list 元素,并更新
        this.list[i], this.list[len(this.list)-1] = this.list[len(this.list)-1], this.list[i]
        this.list = this.list[:len(this.list)-1]

        //删除记录
        delete(this.dict, val)
        return true
    }
    return false
}


/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
    if len(this.list) > 0 {
        return this.list[rand.Intn(len(this.dict))]
    }
    return 0
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
```

1. **K Closest Points to Origin**

```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        for x,y in points:
            heapq.heappush(h,(-(x**2 + y**2),[x,y]))
            if len(h)>K:
                heapq.heappop(h)
        return list(map(lambda x :x[1],h))

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ### top K 一定quick select

        if len(points) <= K:
            return points

        ## 不直接递归call kClosest,因为数据要处理为distance
        dis_list = list(map(lambda x : (x[1][0]**2+x[1][1]**2,x[1]),enumerate(points)))
        self.quickSelect(dis_list,0,len(points)-1,K)
        return list(map(lambda x: x[1], dis_list[:K]))

    def partitions(self,nums,l,r):
        pivot = nums[r]
        i = l - 1
        for j in range(l,r):
            if nums[j][0]< pivot[0]:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1],nums[r] = nums[r],nums[i+1]
        return i + 1 

    def random_partitions(self,nums,l,r):
        i = random.randint(l,r)
        nums[r],nums[i] = nums[i],nums[r]
        return self.partitions(nums,l,r)


    def quickSelect(self,nums,l,r,k):
        pos = self.random_partitions(nums, l, r)
        num = pos - l + 1
        if k < num:
            self.quickSelect(nums,l, pos -1,k)
        elif k > num:
            self.quickSelect(nums,pos + 1, r,k-num)

##　空间复杂度高,如果数据量大还是使用 heap更好
```

1. **Ugly Number**

```python
class Solution:
    def isUgly(self, num: int) -> bool:
        if not num:
            return False
        else:
            while not num % 5: num /= 5
            while not num % 3: num /= 3
            while not num % 2: num /= 2
        return num == 1
```

```go
func isUgly(num int) bool {
    if num <= 0{
        return false
    }
    if num%2 == 0 || num%3 == 0 || num%5 == 0{
        for num%2 == 0 {
            num/=2
        }
        for num%3 == 0 {
            num/=3
        }
        for num%5 == 0{
            num/=5
        }
    }
    return num == 1   
}
```

1. **Ugly Number II**

```python
## 暴力
## 超时
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ## n does not exceed 1690
        i = 0
        num = 0
        while i < n:
            num+=1
            if self.isUgly(num):
                i += 1
        return num

    def isUgly(self, num: int) -> bool:
        if not num:
            return False
        else:
            while not num % 5: num /= 5
            while not num % 3: num /= 3
            while not num % 2: num /= 2
        return num == 1

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

```go
func nthUglyNumber(n int) int {
    if n == 1 {
        return n
    }
    fives, threes, twos := 0, 0, 0
    dp := make([]int, n)
    dp[0] = 1
    for i := 1; i < n; i++ {
        dp[i] = min(dp[twos]*2, min(dp[threes]*3, dp[fives]*5))
        if dp[i] == dp[twos]*2 {
            twos++
        }
        if dp[i] == dp[threes]*3 {
            threes++
        }
        if dp[i] == dp[fives]*5 {
            fives++
        }
    }
    return dp[n-1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

