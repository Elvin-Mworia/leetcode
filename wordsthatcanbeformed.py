from collections import Counter,defaultdict
class Solution:
    def wordscount(self,words:list[str],chr:str)->int:
        charCount=Counter(chr)#hashmap of chr
        res=0

        for w in words:
            curr_word=defaultdict(int)#if c not encountered in dictionary default count value is 0
            good=True
            for c in w:
                curr_word[c]+=1
                if c not in charCount or curr_word[c]>charCount[c]:
                    good=False
                    break
            if good:
                res+=len(w)

        return res

problem=Solution()

print(problem.wordscount(["ba","bat","cat"],"acba"))

