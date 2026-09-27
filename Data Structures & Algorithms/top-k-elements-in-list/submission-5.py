class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}


        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        return [item[0] for item in sorted(freq.items(), key=lambda item: item[1], reverse=True)[:k]]
