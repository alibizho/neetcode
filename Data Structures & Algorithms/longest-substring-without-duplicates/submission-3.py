class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0    
        l, r = 0, 1
        count = defaultdict(int)
        count[s[l]] += 1
        longest = 1
        cur = 1
        while r< len(s):
            if s[r] in count:
                del count[s[l]]
                l += 1
                cur = 0
            else:
                cur = r-l+1
                count[s[r]] += 1
                r+=1

            longest = max(cur, longest)
        return longest
        