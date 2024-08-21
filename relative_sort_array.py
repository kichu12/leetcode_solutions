class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sample=[]
        rem=[]
        for h in arr1:
            if h not in arr2:
                rem.append(h)
        for i in arr2:

            for j in arr1:
                if j==i:
                    sample.append(j)
            
        
        rem.sort()        
        sample.extend(rem)
        return sample
                
        
        