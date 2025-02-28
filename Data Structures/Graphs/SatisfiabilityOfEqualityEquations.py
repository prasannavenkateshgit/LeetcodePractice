'''
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.
'''
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par=[i for i in range(26)]
        rank=[1]*26
        
        def find(n1):
            res=n1
            while res!=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res
        
        for e in equations:
            if e[1]=="=":
                par[find(ord(e[0])-ord('a'))] = find(ord(e[3])-ord('a'))
        for e in equations:
            if e[1]=="!" and find(ord(e[0])-ord('a')) == find(ord(e[3])-ord('a')):
                return False
        return True
