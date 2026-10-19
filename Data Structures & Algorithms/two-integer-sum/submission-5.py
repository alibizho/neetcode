class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        seen = set()

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(nums[i])
        return False