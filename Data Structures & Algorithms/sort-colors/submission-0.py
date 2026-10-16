class Solution:
    def sortColors(self, givenarr: List[int]) -> None:
        st,md,end = 0,0,len(givenarr) - 1
        while md <= end:
            if st == md and givenarr[st] == 0:
                st += 1
                md += 1
            elif givenarr[md] == 0:
                givenarr[md],givenarr[st] = givenarr[st],givenarr[md]
                st += 1
            elif givenarr[md] == 1:
                md += 1
            else:
                givenarr[md],givenarr[end] = givenarr[end],givenarr[md]
                end -= 1