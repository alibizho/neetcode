class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += "".join([str(len(i)), "#", i])

        return res

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []

        while i < len(s):
            t = ""
            cur_len = ""
            while s[i] != "#":
                cur_len += "".join(s[i])
                i+=1
            t += "".join(s[i+1:int(cur_len)+i+1])
            res.append(t)
            i += int(cur_len) + 1

        return res
