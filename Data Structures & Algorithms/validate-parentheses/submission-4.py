class Solution:
    def isValid(self, s: str) -> bool:
        pairs = []

        opening = ['(', '{', '[']
        closing = [')', '}', ']']

        for c in s:
            if c in opening:
                pairs.append(c)

            elif c in closing:
                pairs.pop()

        return len(pairs) == 0
