class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen_vals = 0
        for i in range(len(nums)):
            if nums[i] == val:
                seen_vals += 1

            else:
                nums[i - seen_vals], nums[i] = nums[i], nums[i - seen_vals]

        for i in range(len(nums)):
            if nums[i] == val:
                nums = nums[0:i]
                break


        return len(nums)



            
