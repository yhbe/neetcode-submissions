class Solution:
    def productExceptSelf(self, oarr: List[int]) -> List[int]:
        carr = [1 for i in range(0, len(oarr))]
        multiplier = 1
        for i in range(0, len(oarr) - 1):
            multiplier *= oarr[i]
            carr[i + 1] *= multiplier

        multiplier = 1
        for i in range(len(oarr) - 1, 0, -1):
            multiplier *= oarr[i]
            carr[i - 1] *= multiplier
        
        return carr