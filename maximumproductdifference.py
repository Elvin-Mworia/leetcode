class Solution:
    def  maxprodiff(self,nums:list[int])->int:
        max1,max2=0,0
        min1,min2=float("inf"),float("inf")


        for n in nums:

            if n>max2:
                if n>max1:
                     max1,max2=n,max1
                else:
                    max2=n
            if n<min2:
                if n<min1:
                    min1,min2=n,min1
                else:
                    min2=n
        print(max2,max1)
        print(min2,min1)            
        return ((max2*max1)-(int(min2)*int(min1)))

problem=Solution()

print(problem.maxprodiff([5,6,9,8,4]))