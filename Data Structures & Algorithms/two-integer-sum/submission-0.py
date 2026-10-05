class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosummapping = {}
        for i in range(0,len(nums)):
            compliment = target - nums[i]
            if compliment in twosummapping:
                return [twosummapping[compliment], i]
            twosummapping[nums[i]] = i