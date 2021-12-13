#118 Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# https://www.youtube.com/watch?v=icoql2WKmbA&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=2


class Solution:
    def generate(self, numRows):
        if numRows < 1 or numRows > 30:
            return "Out of bounds! Please select number between 1-30!"
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        output = [[1], [1,1]]
        
        for i in range(1, numRows-1):
            new_row = []
            for j in range(len(output[-1])-1):
                el_sum = output[i][j]+output[i][j+1]
                new_row.append(el_sum)
            new_row.insert(0, 1)
            new_row.append(1)
            output.append(new_row)
        return output


if __name__ == "__main__":
    solution = Solution()
    # testcase 1
    input = 3
    output = solution.generate(input)
    print(output)