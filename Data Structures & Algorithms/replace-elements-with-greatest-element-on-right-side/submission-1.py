class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = 0
        for i in range(len(arr)):

            if i == len(arr) - 1 or arr[i] > arr[i + 1]:
                while l < i:
                    arr[l] = arr[i]
                    l += 1

        arr[len(arr) - 1] = -1
        return arr

            

            