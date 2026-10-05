class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointerA = 0
        notequaltoval = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[pointerA], nums[i] = nums[i],nums[pointerA]
                notequaltoval += 1
                pointerA += 1
        
        return notequaltoval
        