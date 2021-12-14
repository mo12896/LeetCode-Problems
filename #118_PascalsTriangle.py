#118. Pascal's Triangle (Easy)
# https://leetcode.com/problems/pascals-triangle/
# https://www.youtube.com/watch?v=icoql2WKmbA&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=2


class Solution:
    def generate(self, numRows): # since limited to 30 rows, it runs in approx. O(1) time, O(1) space
        if numRows < 1 or numRows > 30:
            return "Out of bounds! Please select number between 1-30!"
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        output = [[1], [1,1]]
        
        for i in range(1, numRows-1): # O(N) time, O(1) space
            new_row = [1]
            for j in range(len(output[-1])-1): # O(N) time, O(1) space
                el_sum = output[i][j]+output[i][j+1]
                new_row.append(el_sum)
            new_row.append(1)
            output.append(new_row)
        return output


if __name__ == "__main__":
    solution = Solution()
    # testcase 1
    input = 30
    output = solution.generate(input)
    print(output)