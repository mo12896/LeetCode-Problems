# 167. Two Sum II - Input Array Is Sorted (Easy)
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# https://www.youtube.com/watch?v=sAQT4ZrUfWo&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=5


class Solution: # O(N) time, O(1) space
    def twoSum(self, numbers, target):
        pointer1 = 0
        pointer2 = len(numbers)-1
        
        while pointer1 < pointer2: # O(N) time, O(1) space
            curr_sum = numbers[pointer1] + numbers[pointer2]
            if curr_sum < target:
                pointer1 += 1
            elif curr_sum > target:
                pointer2 -= 1
            else:
                return [pointer1+1, pointer2+1]


if __name__ == "__main__":
    solution = Solution()
    # testcase 1
    numbers = [2,7,11,15]
    target = 9
    output = solution.twoSum(numbers, target)
    print(output)