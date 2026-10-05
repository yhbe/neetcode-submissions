class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentcount = 0

        i = 0
        while i < len(nums):
            iterationcount = 0
            if nums[i] == 1:
                iterationcount += 1
                while i + 1 < len(nums) and nums[i + 1] == 1:
                    iterationcount += 1
                    i += 1
            currentcount = max(currentcount, iterationcount)
            i += 1
        
        return currentcount