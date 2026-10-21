class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        cur_sum = 0

        prefix_sums_hmp = {0:1}

        for i in nums:
            cur_sum += i

            diff = cur_sum - k

            res += prefix_sums_hmp.get(diff, 0)
            prefix_sums_hmp[cur_sum] = 1 + prefix_sums_hmp.get(cur_sum, 0)

        return res