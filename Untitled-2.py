from typing import List


def singleNumber(nums: List[int]) -> int:
        for i in nums:
            if(nums.count(i) == 1):
                return(i)
                
nums = [4,1,2,1,2]
num = [2,2,1]
print(singleNumber(num))
