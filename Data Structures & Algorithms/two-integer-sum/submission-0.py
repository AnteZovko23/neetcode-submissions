class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_indexes = {}

        result = []

        for i in range(len(nums)):
            compliment = target - nums[i]

            seen_compliment = seen_indexes.get(compliment)

            if seen_compliment != None:
                return [seen_compliment, i]

            else:
                seen_indexes[nums[i]] = i