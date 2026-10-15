class NumMatrix:

    def __init__(self, givenarr: List[List[int]]):
        self.paddedmatrix = [[0 for i in range(0, len(givenarr[0]) + 1)] for j in range(0,len(givenarr) + 1)]
        
        for i in range(0, len(givenarr)):
            for j in range(0, len(givenarr[0])):
                self.paddedmatrix[i + 1][j + 1] = (givenarr[i][j] + self.paddedmatrix[i][j + 1] + self.paddedmatrix[i + 1][j]) - self.paddedmatrix[i][j]

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        lr,lc = row1,col1
        rr,rc = row2,col2
        return (self.paddedmatrix[rr + 1][rc + 1] + self.paddedmatrix[lr][lc]) - (self.paddedmatrix[rr + 1][lc] + self.paddedmatrix[lr][rc + 1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)