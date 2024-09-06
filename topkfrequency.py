from collections import Counter;

def solution(nums:list[int],k:int)->list[int]:
    if len(nums)==0:
        print('integer array must have one or more elements')
        return 
    numsdic={}
    for i in nums:
        exists=numsdic.get(str(i))
        if exists is not None :
            numsdic[str(i)]+=1
            #print(numsdic[str(i)])
        else:
            numsdic[str(i)]=1
    
    print(numsdic.values())
    val=[]
    for i in numsdic:
        val.append(numsdic.get(i))
   # print(res)
    val.sort(reverse=True)
    print(val)
    res=[]
    for i in range(k):
        for a,v in numsdic.items():
          if v==val[i] and int(a) not in res and len(res)<k:
                res.append(int(a))
    return(res)

print('solution 1:',solution([1,2,1,2],2))     


def solutions2(nums:list[int],k:int)->list[int]:
    if len(nums)==0:
        print('integer array must have one or more elements')
        return 
   
    num=Counter(nums)

    print(num.most_common(k))
    res=num.most_common(k)
    finalres=[]
    for i in res:
        finalres.append(i[0])
    print('solution 2:',finalres)


# solutions2([1,2,1,2,3,3,4,4],4)

# class Solution:
#         from collections import Counter
#         if len(numsdic)==0:
#             print('integer array must have one or more elements')
#             return 
   
#         num=Counter(numsdic)
#         res=num.most_common(k)
#         finalres=[]
#         for i in res:
#             finalres.append(i[0])
#         print(finalres)
#         return(finalres)



