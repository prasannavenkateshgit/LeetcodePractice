'''
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.
'''
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        noofpeople=k+1
        left=min(sweetness)
        right=sum(sweetness)//noofpeople
        while left<right:
            mid=(left+right+1)//2
            cursweetness=0
            peoplewithchoc=0
            for s in sweetness:
                cursweetness+=s
                if cursweetness>=mid:
                    peoplewithchoc+=1
                    cursweetness=0
            if peoplewithchoc>=k+1:
                left=mid
            else:
                right=mid-1
        return right
        
