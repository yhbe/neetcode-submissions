class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        greatestseen = [0 for i in range(0, len(arr))]
        greatestseen[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            greatestseen[i] = max(greatestseen[i + 1], arr[i + 1])
        return greatestseen
