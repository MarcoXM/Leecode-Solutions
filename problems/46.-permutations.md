# 46. Permutations

{% tabs %}
{% tab title="TLE" %}
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
    

```
{% endtab %}

{% tab title="Done" %}
```python
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
{% endtab %}
{% endtabs %}

