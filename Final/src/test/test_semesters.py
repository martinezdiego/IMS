from heapq import heappop, heappush, heapify 
from collections import deque 

N = 10005
graph = [[] for i in range(N)]
visited = [0 for i in range(N)]
edge = [0 for i in range(N)]

def dfs(v):
    if (visited[v]):
        return visited[v]
    visited[v] = 1
    for u in graph[v]:
        visited[v] += dfs(u)
    return visited[v]
    
n, k = list(map(int, input().split()))
courses = list(map(int, input().split())) 

for i in range (n):
    if (courses[i]):
        graph[courses[i]].append(i + 1)
        edge[i + 1] += 1

priority_queue = []
heapify(priority_queue)

for i in range (n):
    if (not edge[i + 1]):
        dfs(i + 1)
        heappush(priority_queue, [-1 * visited[i + 1], i + 1])

ans = 0
while (len(priority_queue)):
    ans += 1
    q = deque()
    count = 0
    while (len(priority_queue) and count < k):
        count += 1
        first, second = heappop(priority_queue)
        for i in graph[second]:
            q.append(i)
    while (len(q)):
        heappush(priority_queue, [-1 * visited[q[0]], q[0]])
        q.popleft()
print(ans)