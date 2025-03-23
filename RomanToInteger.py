'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        total=0
        if s[0]=="I":
            total+=1
        elif s[0]=="V":
            total+=5
        elif s[0]=="X":
            total+=10
        elif s[0]=="L":
            total+=50
        elif s[0]=="C":
            total+=100
        elif s[0]=="D":
            total+=500
        elif s[0]=="M":
            total+=1000
        i=1
        while i<len(s):
            if s[i]=="I":
                total+=1
            elif s[i]=="V":
                if s[i-1]=="I":
                    total-=1
                    total+=4
                else:
                    total+=5
            elif s[i]=="X":
                if s[i-1]=="I":
                    total-=1
                    total+=9
                else:
                    total+=10
            elif s[i]=="L":
                if s[i-1]=="X":
                    total-=10
                    total+=40
                else:
                    total+=50
            elif s[i]=="C":
                if s[i-1]=="X":
                    total-=10
                    total+=90
                else:
                    total+=100
            elif s[i]=="D":
                if s[i-1]=="C":
                    total-=100
                    total+=400
                else:
                    total+=500
            elif s[i]=="M":
                if s[i-1]=="C":
                    total-=100
                    total+=900
                else:
                    total+=1000
            i+=1
        return total
