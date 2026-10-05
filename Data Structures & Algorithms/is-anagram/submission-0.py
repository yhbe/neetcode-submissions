class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sarr = [0 for i in range(26)]
        tarr = [0 for j in range(26)]

        for i in range(0, len(s)):
            sarr[ord(s[i]) - ord('a')] += 1

        for i in range(0, len(t)):
            tarr[ord(t[i]) - ord('a')] += 1

        return True if tarr == sarr else False