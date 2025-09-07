from collections import defaultdict
class Solution:
    def groupedAnagram(self,input:list[str]):
        res=defaultdict(list)

        for s in input:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1 #calculating the index of the character and increment counter
            res[tuple(count)].append(s)

        return res.values()

problem=Solution()
print(problem.groupedAnagram(["ate","eat","tea","rat","tar","bar","barre"]))