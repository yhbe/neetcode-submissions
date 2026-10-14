class Solution:
    def topKFrequent(self, givenarr: List[int], k: int) -> List[int]:
        emptyarr = [[] for i in range(0,len(givenarr))]

        mapping = {}

        for number in givenarr:
            mapping.setdefault(number,0)
            mapping[number] += 1

        for (number,freqval) in mapping.items():
            emptyarr[freqval - 1].append(number)
        
        returnarr = []

        exit = False
        for i in range(len(emptyarr) - 1, -1, -1):
            if exit:
                break
            if emptyarr[i]:
                for number in emptyarr[i]:
                    k -= 1
                    returnarr.append(number)
                    if k == 0:
                        exit = True
                        break
                        
        
        return returnarr