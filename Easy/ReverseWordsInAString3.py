'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        splitwords = s.split(' ')
        reversedorder = []
        for i in splitwords:
            reversedorder.append(i[::-1])
        ans=''
        for j in reversedorder:
            ans=ans+j+' '
        ans=ans.strip()
        return ans
