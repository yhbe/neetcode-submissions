class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        focalp = strs[0]
        strbuilder = ''

        for index,letter in enumerate(focalp):
            for word in strs:
                if index >= len(word) or word[index] != letter:
                    return strbuilder
            strbuilder += letter
        return strbuilder

