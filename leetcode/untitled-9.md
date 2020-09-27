# Untitled

```python


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        ## 一开始做不出还是不理解，那个预收费没留意到
        cus = 0
        res = 0
        count = len(customers)
        for c in customers:
            cus += c
            if cus > 4:
                res +=  4 * boardingCost - runningCost  
                cus -= 4
                
            else:
                res +=  cus * boardingCost - runningCost  
                cus = 0
                
        if res <= 0:
            return -1
    
        while cus:
            if cus > 4:
                res +=  4 * boardingCost - runningCost  

                if 4 * boardingCost - runningCost  <= 0:
                    break
                cus -= 4

            else:
                res +=  cus * boardingCost - runningCost  
                if cus * boardingCost - runningCost <= 0:
                    break
                cus = 0

            count += 1

        return count

            
            
            
            
            
        
```

