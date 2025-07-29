from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique = set(nums)
        pos_sum = sum(x for x in unique if x > 0)
        return pos_sum if pos_sum > 0 else max(nums)
    
Solution = Solution()
if __name__ == "__main__":
    nums = list(map(int,input("Enter the numbers seperated by space: ").split()))
    result = Solution.maxSum(nums)
    print(f"The maximum unique subarray sum after deletion is {result}")