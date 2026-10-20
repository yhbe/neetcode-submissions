class Solution:
    def isValidSudoku(self, givenmatrix: List[List[str]]) -> bool:
        
        for i in range(0, len(givenmatrix)):
            currentrow = givenmatrix[i]
            uniqueset = set()
            for num in currentrow:
                if num in uniqueset:
                    return False
                if num == '.':
                    continue
                else:
                    uniqueset.add(num)

        for col in range(0, len(givenmatrix[0])):
            uniqueset = set()
            for row in range(0, len(givenmatrix)):
                if givenmatrix[row][col] in uniqueset:
                    return False
                if givenmatrix[row][col] == '.':
                    continue
                else:
                    uniqueset.add(givenmatrix[row][col])

        rowstart,rowend = 0,3
        colstart,colend = 0,3
        while rowend <= 9:
            while colend <= 9:
                uniqueset = set()
                for irow in range(rowstart,rowend):
                    for jcol in range(colstart,colend):
                        if givenmatrix[irow][jcol] in uniqueset:
                            return False
                        if givenmatrix[irow][jcol] != '.':
                            uniqueset.add(givenmatrix[irow][jcol])
                colstart += 3
                colend += 3
            rowstart += 3
            rowend += 3
        
        return True