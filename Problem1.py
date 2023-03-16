


class Problem1:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
    
    
    def twoSumEfficient(self, nums: List[int], target: int) -> List[int]:
        return 