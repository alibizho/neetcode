class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valids = {"}" : "{", "]": "[", ")": "("}


        for i in s:
            if i in valids.values():
                stack.append(i)
            elif i in valids:
                if not stack or valids.get(i) != stack[-1]:
                    return False
                else:
                    stack.pop()
                    continue
        return not stack