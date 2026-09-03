from collections import deque

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        q = deque()
        for i in range(len(nums)):
            if nums[i] == val:
                q.append(i)

            elif bool(q):
                index = q.popleft()
                nums[index] = nums[i]
                nums[i] = '_'

        print(nums)

        return 0




            
