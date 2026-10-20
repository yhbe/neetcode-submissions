class Solution:
    def longestConsecutive(self, givenarr: List[int]) -> int:

        def countconsecutive(num):
            stcount = 1
            while num + 1 in uniqueset:
                stcount += 1
                num += 1
            self.consecutivecount = max(self.consecutivecount,stcount)

        self.consecutivecount = 1
        if len(givenarr) == 0:
            return 0
        if len(givenarr) == 1:
            return 1
        uniqueset = set(givenarr)
        for num in givenarr:
            if num - 1 not in uniqueset:
                countconsecutive(num)
        return self.consecutivecount