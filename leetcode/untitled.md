# 414. Third Maximum Number

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        ##　这个与top k 最大不同就是k 是定值
        f_ = s_ = t_ = -2 << 32
        for n in nums:
            if n > t_ : # 大于3rd
                if n > s_: # 大于2nd
                    if n > f_: # 大于1st
                        t_ = s_
                        s_ = f_
                        f_ = n ## top3 都换人
                        
                    elif n < f_:
                        t_ = s_
                        s_ = n
                elif n < s_:
                    t_ = n
        ## 最后检查         
        if t_ == (-2 << 32):
            return f_
        else:
            return t_
```
{% endtab %}

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}

