'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for i in strs:
            res=res+str(len(i))+'#'+i
        return res

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i=j+1+length
        return ans
