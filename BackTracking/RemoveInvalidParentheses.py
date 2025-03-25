'''Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest = -1
        self.res = set()
        self.dfs(s,0,[],0,0)
        return list(self.res)

    def dfs(self, string, curidx, curres, lcount, rcount):
        if curidx>=len(string):
            if lcount==rcount:
                if len(curres)>self.longest:
                    self.longest = len(curres)
                    self.res=set()
                    self.res.add("".join(curres))
                elif len(curres)==self.longest:
                    self.res.add("".join(curres))
        else:
            curchar=string[curidx]
            if curchar == "(":
                curres.append(curchar)
                self.dfs(string, curidx+1, curres, lcount+1, rcount)
                curres.pop()
                self.dfs(string, curidx+1, curres, lcount, rcount)
            elif curchar==")":
                self.dfs(string, curidx+1, curres, lcount, rcount)
                if lcount>rcount:
                    curres.append(curchar)
                    self.dfs(string, curidx+1, curres, lcount, rcount+1)
                    curres.pop()
            else:
                curres.append(curchar)
                self.dfs(string, curidx+1, curres, lcount, rcount)
                curres.pop()
            
