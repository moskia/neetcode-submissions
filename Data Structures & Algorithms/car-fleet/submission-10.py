class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[s, p] for s, p in zip(speed, position)]
        pairs.sort(key=lambda x: x[1], reverse=True)
        stack = []

        for s, p in pairs:
            time = (target-p)/s 
            if stack and time <= (target-stack[-1][1])/stack[-1][0]:
                continue
            stack.append([s, p])

        return len(stack)