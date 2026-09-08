class Solution:
    def isValid(self, s: str) -> bool:
        pairs = []
        if len(s) % 2 != 0:
            return False
        for c in s:
            if c == ')':
                if len(pairs) == 0 or pairs.pop() != '(':
                    return False
            elif c == ']':
                if len(pairs) == 0 or pairs.pop() != '[':
                    return False

            elif c == '}':
                if len(pairs) == 0 or pairs.pop() != '{':
                    return False
            else:
                pairs.append(c)
        
        return True