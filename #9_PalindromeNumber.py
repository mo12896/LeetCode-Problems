# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# https://www.youtube.com/watch?v=UPdSViixmDs&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=12


class Solution:
    # Most elegant solution, but not optimal in space!
    def isPalindrome1(self, x): # O(N) time, O(N) space
        return str(x) == str(x)[::-1] # O(N) time, O(N) space

    # Better solution in terms of space!
    def isPalindrome2(self, x): # O(N) time, O(1) space
        x = str(x)
        pointer1, pointer2 = 0, len(x)-1

        while pointer1 < pointer2: # O(N) time, O(1) space
            if x[pointer1] != x[pointer2]:
                return False
            pointer1, pointer2 = pointer1+1, pointer2-1
        return True


if __name__ == "__main__":
    solution = Solution()
    # testcase 1
    input = -1213121
    output = solution.isPalindrome2(input)
    print(output)