# Untitled

{% tabs %}
{% tab title="binary" %}
```cpp
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) return false;
        int last_min = nums[0];
        map<int, int>  cnt;
        for (int i = n-1; i > 0; --i) cnt[nums[i]]++;
    
        for (int i = 1; i <n - 1; ++i){
            if (last_min >= nums[i]){
                last_min = nums[i]; // update 
            }
            else  {
                auto p = cnt.upper_bound(last_min);
                if (p!=cnt.end() && p->first<nums[i]) return true;

            }
            cnt[nums[i]]--;
            if (cnt[nums[i]] == 0 ) cnt.erase(nums[i]);
        }
        return false;
    }
};


```
{% endtab %}

{% tab title="Python Stack 0 n" %}
```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second = -float("inf")
        for n in nums[::-1]:
            if second > n : return True
            
            while stack and stack[-1] < n:
                second = stack.pop() ## stack 出来的就是比现在小的
                
            stack.append(n)
            
        return False
        
```
{% endtab %}
{% endtabs %}

