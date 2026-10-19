class Solution:

    def encode(self, givenarrofstrings: List[str]) -> str:
        buildstr = ''
        for _str in givenarrofstrings:
            buildstr = buildstr + str(len(_str)) + '#' + _str
        return buildstr


    def decode(self, givenstr: str) -> List[str]:
        i = 0
        returnarr = []
        while i < len(givenstr):
            lengthbuilder = ''
            while givenstr[i] != '#':
                lengthbuilder += givenstr[i]
                i += 1
            i += 1
            newending = i + int(lengthbuilder)
            returnarr.append(givenstr[i:newending:1])
            i = newending
        return returnarr
