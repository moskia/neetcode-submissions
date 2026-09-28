class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info = [[s, p] for s, p in zip(speed, position)]
        info.sort(key=lambda x: x[1], reverse=True)
        stack = []

        for s, p in info:
            if not stack:
                stack.append([s, p])
                continue
            time = (target-stack[-1][1])/stack[-1][0]
            if time < (target-p)/s:
                stack.append([s, p])



        return len(stack)