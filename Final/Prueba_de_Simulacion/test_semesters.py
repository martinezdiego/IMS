from heapq import heappop, heappush, heapify 

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
    queue = []
    count = 0
    while (len(priority_queue) and count < k):
        count += 1
        first, second = heappop(priority_queue)
        for i in graph[second]:
            queue.append(i)
    while (len(queue)):
        heappush(priority_queue, [-1 * visited[queue[0]], queue[0]])
        queue.pop(0)
print(ans)