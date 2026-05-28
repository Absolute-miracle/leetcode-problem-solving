class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        re_set = set(nums)
        return len(re_set) < len(nums)
    


if __name__ == "__main__" :
    sol = Solution()
    #1st check 
    nums = [1,2,3,1]
    print(sol.containsDuplicate(nums))
    print("===1st check===")
    #2nd check
    nums = [1,2,3,4]
    print(sol.containsDuplicate(nums))
    print("===2nd check===")
    #3rd check
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(sol.containsDuplicate(nums))
    print("===3rd check===")


