class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string = list(s)
        copy = string[:]
        for i in range(0,len(string)):
            string[indices[i]] = copy[i]
        outStr = ''
        for st in string:
            outStr += st
        return outStr