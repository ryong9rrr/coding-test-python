# 23ms(98.93%), 14MB
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for line in range(numRows):
            row = [1] * (line + 1)
            if line >= 2:
                for i in range(1, line):
                    row[i] = result[line - 1][i - 1] + result[line - 1][i]
            result.append(row)
            
        return result