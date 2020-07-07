# 面试题 16.11. 跳水板

{% tabs %}
{% tab title="数学" %}
```python
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k :return []
        diff  = longer - shorter
        base = k * shorter
        ans = [base]
        if not diff:
            return ans
    
        for i in range(1,k+1):
            ans.append(base+ i * diff)

        return ans
```
{% endtab %}

{% tab title="递归" %}
```python
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        # 递归的方法（会超过max）
        # if k == 0:
        #     return []
        # if k == 1:
        #     return [shorter, longer]
        # else:
        #     arr_shorter = [x + shorter for x in self.divingBoard(shorter, longer, k - 1)]
        #     arr_longer = [x + longer for x in self.divingBoard(shorter, longer, k - 1)]
        #     return list(set(arr_shorter + arr_longer))

        # 题解
        if k == 0:
            return []
        if shorter == longer:
            return [k * shorter]
        else:
            return [(k - i) * shorter + i * longer for i in range(k + 1)]


```
{% endtab %}
{% endtabs %}

