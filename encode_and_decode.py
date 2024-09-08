'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

'''
def encode(strs:list[str])->str:
     if len(strs)==0:
            return " "
     dic={}
     for i in range(len(strs)):
        dic[str(i)]=strs[i]

     strlist=list(dic.values())
     finalstring=" ".join(strlist)
     return finalstring


print(encode([]))
def decode(s: str) -> list[str]:
    res=[]
    if s==[] or s.strip()=="":
        return res
    strlist=s.split(" ")
    return strlist

print(decode(encode(["neet","code","love","you"])))
