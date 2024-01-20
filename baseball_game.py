class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []
        ans = 0

        for optn in operations:
            if optn not in {'+', 'C', 'D'}:
                record.append(int(optn))
                ans += int(optn)
            elif optn == '+':
                record.append(record[-1] + record[-2])
                ans += record[-1]
            elif optn == 'C':
                ans -= record.pop()
            elif optn == 'D':
                record.append(2*(record[-1]))
                ans += record[-1]
        return ans