import itertools

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = list(itertools.combinations(nums,3))
        res = []
        if len(lst) == 0:
            res = [] 
        elif lst == [0]:
            res = []
        elif isinstance(lst):  
            for i in lst:
                if sum(i) == 0:
                    res = list(i)
        return res