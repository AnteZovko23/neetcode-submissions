class Solution:
    def isValid(self, s: str) -> bool:
        pairs = []

        for c in s:
            if c == ')':
                if pairs.pop() != '(':
                    return False
            elif c == ']':
                if pairs.pop() != '[':
                    return False

            elif c == '}':
                if pairs.pop() != '{':
                    return False
            else:
                pairs.append(c)
        
        return True