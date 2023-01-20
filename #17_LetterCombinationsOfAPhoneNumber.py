# Use the backtracking algorithm to solve this problem
from ast import List


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if 0 > len(digits) or len(digits) > 4:
            return []
        for i in digits:
            if not i in [str(i) for i in range(2, 10)]:
                return []
        if not digits:
            return []

        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        # A good inutition is the Tree structure of the problemwhich
        # is recursively exploited with the backtracking algorithm
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            for letter in digit_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        return res


if __name__ == "__main__":
    digits = "23"
    expected_output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(expected_output == Solution().letterCombinations(digits))
