class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        occurrences = []
        for key in d:
            occurrences.append(d[key])
        occurrences.sort()
        j = 1
        while j < len(occurrences):
            if occurrences[j] == occurrences[j-1]:
                return False
            else:
                j+=1
        return True
        