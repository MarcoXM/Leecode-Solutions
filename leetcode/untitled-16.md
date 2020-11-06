# Untitled

{% tabs %}
{% tab title="Python N\*N" %}
```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ## N2
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
        print(pre_sum)
        ans = 0
        for i in range(1,n + 1):
            for j in range(i):

                if lower <= pre_sum[i] - pre_sum[j] <=upper:
                    # print(pre_sum[i] - pre_sum[j + 1])
                    ans += 1

        return ans
```
{% endtab %}
{% endtabs %}

