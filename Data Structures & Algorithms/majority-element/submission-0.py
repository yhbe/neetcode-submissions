class Solution:
    def majorityElement(self, givenarr: List[int]) -> int:
        n = len(givenarr) / 2
        _mapping = {}
        for num in givenarr:
            _mapping.setdefault(num,0)
            _mapping[num] += 1
            if _mapping[num] > n:
                return num

