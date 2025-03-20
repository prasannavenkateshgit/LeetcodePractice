'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.
'''
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordptr = abbrptr = 0
        while wordptr<len(word) and abbrptr<len(abbr):
            if abbr[abbrptr].isdigit():
                steps=0
                if abbr[abbrptr]=="0":
                    return False
                while abbrptr<len(abbr) and abbr[abbrptr].isdigit():
                    steps=steps*10+int(abbr[abbrptr])
                    abbrptr+=1
                wordptr+=steps
            else:
                if word[wordptr]!=abbr[abbrptr]:
                    return False
                wordptr+=1
                abbrptr+=1
        return wordptr==len(word) and abbrptr==len(abbr)
        
