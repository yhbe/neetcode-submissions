class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        #create a prefix sum for nums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        for pointer in range(0,len(nums)):
            leftofp = nums[pointer - 1] if pointer - 1 >= 0 else 0
            rightofp = nums[-1] - nums[pointer] if pointer + 1 < len(nums) else 0
            if leftofp == rightofp:
                return pointer

        return -1



        
