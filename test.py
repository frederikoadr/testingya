from typing import List

# Pascal's Triangle Problem
class Solution:
    def generate(numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]

testCase = 5
print(Solution.generate(testCase))
