class Solution:
    def groupAnagrams(self, givenlist: List[str]) -> List[List[str]]:
        
        basedictionary = {}

        for word in givenlist:
            tmpmap = {}
            for w in word:
                tmpmap.setdefault(w,0)
                tmpmap[w] += 1
            key = tuple(sorted(tmpmap.items()))
            basedictionary.setdefault(key, [])
            basedictionary[key].append(word)

        returnarr = []

        for mappingkey,keylist in basedictionary.items():
            returnarr.append(keylist)
        
        return returnarr