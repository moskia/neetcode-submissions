class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op = {'+', 'D', 'C'}
        record = []

        for c in operations:
            if c not in op:
                record.append(int(c))
            elif c == '+':
                score1 = record.pop()
                score2 = record.pop()
                record.append(score2)
                record.append(score1)
                record.append(score1 + score2)
            elif c == 'C':
                record.pop()
            else:
                score = record[-1]*2
                record.append(score)
        return sum(record)

                