class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)  

        return maxSub      

        # curr = best = nums[0]

        # for i in range(1, len(nums)):
        #     num = nums[i]

        #     curr = max(num, curr + num)
        #     best = max(best, curr)
        # return best
