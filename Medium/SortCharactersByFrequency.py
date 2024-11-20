'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        counts={}
        for i in s:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        ans=list(sorted(counts.items(), key=lambda item:item[1], reverse=True))
        final=""
        for i in range(len(ans)):
            for j in range(ans[i][1]):
                final+=ans[i][0]
        print(counts)
        return final
