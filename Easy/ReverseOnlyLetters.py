'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k',
        'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        left=0
        right=len(s)-1
        ans = []
        reversestr = []
        while left<len(s):
            if s[left].lower() in alphabet:
                reversestr.append(s[left])
            left+=1
        reversestr=reversestr[::-1]
        left=0
        reversecount=0
        while left<len(s):
            if s[left].lower() in alphabet:
                ans.append(reversestr[reversecount])
                reversecount+=1
            else:
                ans.append(s[left])
            left+=1
        return ''.join(ans)

        
