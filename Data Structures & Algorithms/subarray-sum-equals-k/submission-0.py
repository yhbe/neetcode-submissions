class Solution:
    def subarraySum(self, givennumbers: List[int], k: int) -> int:
        numtofreq = {0:1}
        cumulativesumarr = [0] * len(givennumbers)

        cumscore = 0
        for i,num in enumerate(givennumbers):
            cumscore += num
            cumulativesumarr[i] = cumscore
        slicecounter = 0
        for _ in range(0,len(givennumbers)):
            if (cumulativesumarr[_] - k) in numtofreq:
                slicecounter += numtofreq[cumulativesumarr[_] - k]
            numtofreq.setdefault(cumulativesumarr[_],0)
            numtofreq[cumulativesumarr[_]] += 1
        print(numtofreq)
        return slicecounter
