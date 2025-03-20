'''
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
'''
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums=[]
        for i,n in enumerate(nums):
            if n:
                self.nums.append((i,n))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot=0
        i=0
        j=0

        while i<len(self.nums) and j<len(vec.nums):
            iidx,inum=self.nums[i]
            jidx,jnum=vec.nums[j]

            if iidx==jidx:
                dot+=inum*jnum
                i+=1
                j+=1
            elif iidx<jidx:
                i+=1
            else:
                j+=1
        return dot

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
