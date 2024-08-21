class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp=[]
        for i in range(0,len(nums)):
            s=0
            for j in range(0,len(nums)):
                if i != j:
                    x=nums[i]+nums[j]
                    if x==target:
                        tmp.append(i)
                        tmp.append(j)
                        s=1
                        
                    else:
                        pass
                else:
                    pass
            if s==1:
                break
            else:
                pass
            
        return tmp    