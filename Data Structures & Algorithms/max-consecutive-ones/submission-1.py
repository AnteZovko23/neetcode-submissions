class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_max = 0
        total_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_max += 1
            else:
                total_max = current_max
                current_max = 0

            if (i == len(nums) - 1):
                if total_max < current_max:
                    total_max = current_max
         

        return total_max


        