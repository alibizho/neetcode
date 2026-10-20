class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals)

        l,r = 0, 1
        res = []
        curr_big = intervals[l][1]

        while r < len(intervals):
            
            if intervals[r][0] <= curr_big:
                curr_big = max(curr_big, intervals[r][1])
            else:
                res.append([intervals[l][0], curr_big])
                l = r
                curr_big = intervals[l][1]
            r+= 1

        res.append([intervals[l][0], curr_big])

        return res

    