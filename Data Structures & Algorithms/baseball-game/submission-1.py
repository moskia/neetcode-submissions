class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op = {'+', 'D', 'C'}
        record = []

        for c in operations:
            if c == '+':
                score1 = record[-1]
                score2 = record[-2]
                record.append(score1 + score2)
            elif c == 'C':
                record.pop()
            elif c == 'D':
                score = record[-1]*2
                record.append(score)
            else:
                record.append(int(c))
        return sum(record)

                