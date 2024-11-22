'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
'''

#There is a trick to this question. No need to perform these operations or switches, all you need to do is count characters.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counts1=defaultdict(int)
        counts2=defaultdict(int)
        if len(word1)!=len(word2):
            return False
        for i in word1:
            counts1[i]+=1
        for j in word2:
            counts2[j]+=1
        if set(word1)==set(word2):
            val1=[]
            for k in counts1:
                val1.append(counts1[k])
            val2=[]
            for l in counts2:
                val2.append(counts2[l])
            if sorted(val1)==sorted(val2):
                return True
            else:
                return False
        else:
            return False
