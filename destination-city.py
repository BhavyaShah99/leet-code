class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        allCities = {None}
        for path in paths:
            for city in path:
                allCities.add(city)
        startCities = {None}
        for p in paths:
            startCities.add(p[0])
        diff = allCities - startCities
        dest = ''
        for c in diff:
            dest = c
        return dest