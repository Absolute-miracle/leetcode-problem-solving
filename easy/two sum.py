class Solution:
    def twoSum(self,nums, target):
      seen ={}
      for i,num in enumerate(nums):
        com = target - num
        if com in seen : 
            return [seen[com] ,i]
        seen[num] = i
      return []



if __name__ == "__main__" : 
    Sol = Solution()
    #first check
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {Sol.twoSum(nums1, target1)}\n")

    #sec check
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {Sol.twoSum(nums2, target2)}\n")

    #third check 
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {Sol.twoSum(nums3, target3)}\n")

print("Good Boy/ Girl")