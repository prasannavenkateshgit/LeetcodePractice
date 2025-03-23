'''
Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        decimal=False
        number=False

        i=0
        if s[i] in ['+','-']:
            i+=1
        while i<len(s):
            curr=s[i]
            if curr.isalpha():
                if curr not in ['e','E']:
                    return False
                else:
                    return number and self.isvalid(s[i+1:])
            elif curr=='.':
                if decimal:
                    return False
                else:
                    decimal=True
            elif curr in ['+','-']:
                return False
            else:
                number = True
            i+=1
        return number

    def isvalid(self, test):
        if not test:
            return False
        i=0
        number=False
        if test[i] in ['+','-']:
            i+=1
        while i<len(test):
            curr=test[i]
            if not curr.isdigit():
                return False
            else:
                number=True
            i+=1
        return number      
