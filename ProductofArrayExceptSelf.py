'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?
Input: nums = [1,2,4,6]

Output: [48,24,12,8]
'''
def productExceptSelf(nums: list[int]) -> list[int]:
        numsdic={}
        res=[]
        for i in range(len(nums)): 
            elem=[]
            for a in range(len(nums)):
                if a!=i:
                    elem.append(nums[a])
            numsdic[i]=elem
        for b in range(len(numsdic)):
            numstomul=numsdic.get(b)
            prod=1
            for a in numstomul:
                prod*=a
            res.append(prod)
        return res
print(productExceptSelf([0,0]))

def productExceptSelfSol2(nums: list[int])->list[int] :
        numsdic={}
        res=[]
        for i in range(len(nums)): 
            elem=[]
            numsdic[i]=elem
        for b in range(len(numsdic)):
            numstomul=numsdic.get(b)
            for a in range(len(nums)):
                if a!=b:
                   numstomul.append(nums[a]) 
            numsdic[b]=numstomul
        for k,v in numsdic.items():
             prod=1
             numstomul=v
             for a in numstomul:
                prod*=a
             res.append(prod)
        return res

print(productExceptSelfSol2([0,0]))