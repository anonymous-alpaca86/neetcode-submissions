class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            result=result+str(len(word))+"#"+word
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        
        lst=[]
        i=0
        while i<len(s):
            if s[i]=="#":
                length=int(s[:i])
                if length==0:
                    lst.append("")
                    print("blank element appended")
                else:
                    lst.append(s[i+1:i+1+length])
                s=s[i+1+length:]
                i=0
            else:
                i+=1
        
        return lst

