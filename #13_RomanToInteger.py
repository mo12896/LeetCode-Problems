class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15:
            return 0
        for char in s:
            if not char in ("I", "V", "X", "L", "C", "D", "M"):
                return 0

        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        current_sum = 0
        count = 0
        while count < len(s):
            if s[count : count + 2] in roman_dict:
                current_sum += roman_dict[s[count : count + 2]]
                count += 2
            else:
                current_sum += roman_dict[s[count]]
                count += 1

        return current_sum

    # Even better solution:
    def romanToInt2(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15:
            return 0
        for char in s:
            if not char in ("I", "V", "X", "L", "C", "D", "M"):
                return 0

        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev_value = 0
        for char in s[::-1]:
            curr_value = roman_map[char]
            if curr_value >= prev_value:
                result += curr_value
            else:
                result -= curr_value
            prev_value = curr_value
        return result


if __name__ == "__main__":
    solution = Solution()
    # testcase 1
    testcases = {
        "III": 3,
        "LVIII": 58,
        "MCMXCIV": 1994,
    }
    for input, expected_output in testcases.items():
        output = solution.romanToInt2(input)
        print(output == expected_output, output, expected_output)
