# Use the two pointer strategy for triplets to solve this problem
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if 3 > len(nums) < 3 or len(nums) > 500:
            return 0
        for i in nums:
            if -1000 > i or i > 1000:
                return 0
        if -10000 > target or target > 10000:
            return 0

        nums.sort()
        closest_sum = 50000

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum > target:
                    r -= 1
                else:
                    l += 1
        return closest_sum
