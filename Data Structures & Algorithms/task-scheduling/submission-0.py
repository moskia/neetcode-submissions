class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        runTime = 0
        tasks = list(Counter(tasks).values())
        tasks = [-int(c) for c in tasks]
        heapq.heapify(tasks)
        queue = deque([])
        while tasks or queue: 
            runTime += 1
            if tasks: 
                task = heapq.heappop(tasks)
                task += 1
                if task < 0:
                    queue.append([runTime+n, task])
            if queue and queue[0][0] == runTime:
                _, task = queue.popleft()
                if task < 0:
                    heapq.heappush(tasks, task) 
        
        return runTime