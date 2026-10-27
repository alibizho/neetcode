class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            
        
        nums.sort()
        res = set()
        # -4, -1, -1, 0, 1, 2

        for i in range(len(nums)):
            l, r = i+1, len(nums) -1
            while l<r:
                if nums[l] + nums[r] + nums[i] == 0:
                    res.add(tuple([nums[l], nums[r], nums[i]]))
                if nums[l] + nums[r] + nums[i] <= 0:
                    l+=1
                else:
                    r-=1
            
        return list(list(x) for x in res )
