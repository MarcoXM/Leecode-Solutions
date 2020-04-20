## april-18th



```python 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    ## 不换时间 NlogN
    
class Solution:
    def isAnagram(self, s, t):
        dit1, dit2 = {}, {}
        for i in s:
            dit1[i] = dit1.get(i, 0) + 1
        for i in t:
            dit2[i] = dit2.get(i, 0) + 1
        return dit1 == dit2
    
    ## 其实利用的额外空间也是常量啦,
    
    
```



394. **Decode String**

```python
class Solution:
    def decodeString(self, s: str) -> str:
        ## 首先观察选着合适的数据结构
        ans = ''
        flag_num = 0
        stack = []
        for c in s:
            if c.isdigit():
                flag_num = flag_num * 10 + int(c) # 记录数字转换type
                
            elif c =="[":
                stack.append(ans)
                stack.append(flag_num)
                ans = ""
                flag_num = 0
                
            elif c == "]":
                num = stack.pop()
                pre_ans = stack.pop()
                ans = pre_ans + ans*num
                
            else:
                ans += c
                
        return ans
```

692. **Top K Frequent Words**

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        dit = defaultdict(int)
        for w in words:
            dit[w] += 1
        
        h = []
        ## heap 讨论 看到logk第一个应该联想到
        for w,v in dit.items():
            heapq.heappush(h,(-v,w))

        return [ heapq.heappop(h)[1] for _ in range(k)]
```



```bash
Loading tensorflow-py36-cuda10.1-gcc/1.15.2
  Loading requirement: openblas/dynamic/0.2.20 cudnn7.6-cuda10.1/7.6.5.32
    hdf5_18/1.8.20 keras-py36-cuda10.1-gcc/2.3.1 protobuf3-gcc/3.8.0
    nccl2-cuda10.1-gcc/2.5.6
&&&& RUNNING TensorRT.sample_movielens_mps # /cm/shared/apps/tensorrt-cuda10.1-gcc/6.0.1.5/bin/sample_movielens_mps -b 2 -p 2
Could not find movielens_ratings.txt in data directories:
	data/samples/movielens/
	data/movielens/
&&&& FAILED

```

