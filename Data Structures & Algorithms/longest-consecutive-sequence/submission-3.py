class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        num = 0
        max_count = 0
        for i in nums:
            count = 1

            if i - 1 not in nums:
                num = i
                while num + 1 in nums:
                    count+=1
                    num+=1
            max_count = max(max_count, count)

        return max_count
