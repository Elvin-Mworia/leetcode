'''Given an array of integers nums, return the length of the longest consecutive sequence of elements.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
You must write an algorithm that runs in O(n) time.
Input: nums = [2,20,4,10,3,4,5]
Output: 4
[0,3,2,5,4,6,1,1]
'''

def longestConsecutive(nums: list[int]):
    numscopy=nums.copy()
    sorted=[]
    res=set()
    if(len(nums)==0 or len(nums)==1):
        return(0)
    while len(numscopy)!=0:
        print(min(numscopy))
        sorted.append(min(numscopy)) 
        numscopy.pop(numscopy.index(min(numscopy)))
    for i in range(0,len(sorted)-1):
       print(f"{sorted[i]}--->{sorted[i+1]}")
       if(sorted[i+1]-sorted[i]==1):
           res.add(sorted[i])
       else:
           if(sorted[i+1]-sorted[i]==0):
                    if(sorted[i+2]-sorted[i+1]==1):
                        res.add(sorted[i+2]) 
       if(sorted[i+1]==sorted[-1] and sorted[-1]-sorted[i]==1):
            res.add(sorted[-1]) 
                          
    
    print(res)
    return(len(res))

    

print(longestConsecutive([0]))