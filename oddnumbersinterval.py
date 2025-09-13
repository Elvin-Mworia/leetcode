def countOddNumbers(low:int,high:int)->int:
    length=high-low+1
    count=length // 2

    if length % 2 and low % 2:
        count+=1

    return count

print(countOddNumbers(3,10))