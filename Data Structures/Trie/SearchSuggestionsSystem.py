'''
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.
'''
class TrieNode:
    def __init__(self):
        self.children={}
        self.suggestions=[]
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # res=[]
        # products.sort()

        # l=0
        # r=len(products)-1
        # for i in range(len(searchWord)):
        #     c=searchWord[i]

        #     while l<=r and (len(products[l])<=i or products[l][i]!=c):
        #         l+=1
        #     while l<=r and (len(products[r])<=i or products[r][i]!=c):
        #         r-=1
        #     res.append([])
        #     remain=r-l+1
        #     for j in range(min(3,remain)):
        #         res[-1].append(products[l+j])
        # return res
        root = TrieNode()
        for product in products:
            node = root
            for c in product:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]

                node.suggestions.append(product)
                node.suggestions.sort()
                if len(node.suggestions) > 3:
                    node.suggestions.pop()
        
        ans = []
        node = root
        for c in searchWord:
            if c in node.children:
                node = node.children[c]
                ans.append(node.suggestions)
            else:
                # deadend reached
                node.children = {}
                ans.append([])

        return ans
        
        
