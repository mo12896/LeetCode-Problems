# 217. Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/
# https://www.youtube.com/watch?v=4oZsPXG9B94&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=3


class Solution:
    def containsDuplicate(self, nums):
        seen_nums = {}

        if len(nums) < 1 or len(nums) > 100000:
            return "Array length is out of bounds!"

        for i in range(len(nums)):
            if nums[i] < -10e8 or nums[i] > 10e8:
                return "Array-element is out of bounds!"
            if str(nums[i]) in seen_nums:
                return True
            seen_nums[str(nums[i])] = 1
        return False


if __name__ == "__main__":
    solution = Solution()
    # testcase 1
    input = [1,2,3,1]
    # testcase 1
    #input = [1,2,3,4]
    # testcase 1
    #input = [1,1,1,3,3,4,3,2,4,2]
    output = solution.containsDuplicate(input)
    print(output)