# 1041. Robot Bounded In Circle

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start = [0,0]
        dx, dy = 0,1
        
        for s in instructions:
            if s == "G":
                start[0] += dx
                start[1] += dy
            elif s =="L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        
        return start == [0,0] or (dx, dy) != (0,1)
```
{% endtab %}
{% endtabs %}

