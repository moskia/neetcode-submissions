class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed), reverse=True)
        for p, s in pairs:
            t = (target-p)/s
            if stack and t <= (target - stack[-1][0])/stack[-1][1]:
                continue
            stack.append([p, s])

        return len(stack)
