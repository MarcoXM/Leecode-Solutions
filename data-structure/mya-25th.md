## may-25th

\762. **Prime Number of Set Bits in Binary Representation**

```python
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        ## 位操作,1 出现的次数为prime
        ## 还是要熟悉输入的的边界,2 的 20 次方已经可以cover 所有input了
        ans = 0
        for i in range(L, R + 1):
            if self.isPrime(self.countOne(i)):
                ans += 1
        return ans
        
    ## 优化了这里 
    def isPrime(self, number):
        if number in {2, 3, 5, 7, 11, 13, 17, 19}:
            return True
        else:
            return False
        
    
    def countOne(self, num):
        ans = 0
        while num > 0:
            ans += 1
            num &= (num-1)
        return ans
```

\1380. Log Sorting

```python
class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        ## 正常人逻辑,预处理,排序
        ## pre
        if not logs:
            return []
            
        return sorted(logs,key=self.sort_key)
        
    def sort_key(self, text):
        id, *content = text.split(" ")
        ## 字母为先, 
        ## 数字默认是在字母前, 不能直接操作
        if content[0].isalpha():
            return (0, content, id)
        else:
            ## 如果是数字,我们只需要放到后面就可,所以就只有一重比较....f
            return (1, ) ## 当然,强迫症,补位一致都可
```



