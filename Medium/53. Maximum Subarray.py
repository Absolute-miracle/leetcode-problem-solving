class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]  
        max_sum = nums[0]  

        for num in nums[1:]:  
            current_sum = max(num, current_sum + num)  
            max_sum = max(max_sum, current_sum)       

        return max_sum
    


if __name__ == "__main__" :
    sol = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(f"Max Sum is : {sol.maxSubArray(nums)}       '#EX Out : 6'\n======================================")


    nums = [1]
    print(f"Max Sum is : {sol.maxSubArray(nums)}       '#EX Out : 1'\n======================================")


    nums = [5,4,-1,7,8]
    print(f"Max Sum is : {sol.maxSubArray(nums)}       '#EX Out : 23'\n======================================")


