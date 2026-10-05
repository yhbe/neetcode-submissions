class NumArray:

    def __init__(self, nums: List[int]):
        self.numberarr = nums
        

    def sumRange(self, left: int, right: int) -> int:
        summary = 0
        
        for i in range(left, right + 1, 1):
            summary += self.numberarr[i] 

        return summary


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)