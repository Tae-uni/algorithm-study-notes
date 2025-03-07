# Best Time to Buy and Sell Stock (LeetCode #121)
Given an array `prices`.  
Maximize profit by choosing a single day to buy one stock, different day in the future to sell that stock.  
Return the maximum profit can get transaction. If we cannot get any profit, return `0`.

**Constraints:**
> 1 <= prices.length <= 10^5  
> 0 <= prices[i] <= 10^4  

ex1:  
Input: prices = [7,1,5,3,6,4]  
Output: 5

## Solution Approaches
### Approach 1: Brute Force
**Code:** [Best Time Buy Sell - Brute Force](best_time_buy_sell_brute_force.py)
```python
def maxProfix(prices: List[int]) -> int:
    max_price = 0

    for i in range(len(prices)):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - prices[i], max_price)

    return max_price
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n^2)` Two nested loops iterate through buy-sell pairs.
- Space Complexity: `O(1)` Uses only a few variables.

---

### Approach 2: Min, Max
**Code:** [Best Time Buy Sell - MinMax](best_time_buy_sell_minmax.py)
```python
def maxProfit(self, prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Single pass through the array.
- Space Complexity: `O(1)` Two variables are used.

---

### Approach 3: Explicit
**Code:** [Best Time Buy Sell - Explicit](best_time_buy_sell_explicit.py)
```python
def maxProfit(self, prices: List[int]) -> int:
    buy_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        if buy_price > price:
            buy_price = price
            
        max_profit = max(max_profit, price - buy_price)

    return max_profit
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Single pass through the array.
- Space Complexity: `O(1)` Two variables are used.

---

## 🔥 Final Thoughts
The 1st approach(Brute Force) is straightforward, simple but inefficient for large data.  
It occurs `Time Limit Exceeded` due to `O(n^2)`.  
Min, Max is the most efficient solution.  
Explicit is functionally the same as Min, Max.

---

## References
[LeetCode #121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)