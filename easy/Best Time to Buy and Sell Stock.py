class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0 

        for price in prices: 
            if price < min_price:
                min_price = price
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit

# Test Case 1
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5

# Test Case 2
print(sol.maxProfit([7, 6, 4, 3, 1]))     # Output: 0