'''
Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
We can keep shifting the string in both directions to form an endless shifting sequence.

For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
'''
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic=collections.defaultdict(list)
        for i in strings:
            if len(i)==1:
                dic[(-1,)].append(i)
            else:
                diffs=[]
                s=1
                while s<len(i):
                    diffs.append((ord(i[s])-ord(i[s-1]))%26)
                    s+=1
                dic[tuple(diffs)].append(i)
        ans=[]
        for k,v in dic.items():
            ans.append(v)
        return ans
