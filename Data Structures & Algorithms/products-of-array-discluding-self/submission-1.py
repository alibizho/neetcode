class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        pref = []
        suff = []
        res = []
        product = 1

        for p in range(len(nums)):
            pref.append(product)
            product *= nums[p]
        product = 1
        for s in range(len(nums) - 1, -1, -1):
            suff.append(product)
            product *= nums[s]

        suff = suff[::-1]

        for i in range(len(nums)):
            res.append(pref[i] * suff[i])
        return res