# 1672. Richest Customer Wealth

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        asset = map( lambda x: sum(x),accounts)
        return max(asset)
```

