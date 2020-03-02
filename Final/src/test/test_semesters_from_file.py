from heapq import heappop, heappush, heapify 
from collections import deque 
import pandas as pd
import math

N = 10005
graph = [[] for i in range(N)]
visited = [0 for i in range(N)]
edge = [0 for i in range(N)]
courses_map = dict()
priority_queue = []
heapify(priority_queue)

data = pd.read_excel('./raw_data/courses_list.xlsx')
for index, row in data.iterrows():
    courses_map[row['Nombre']] = int(row['ID'])

data = pd.read_excel('./raw_data/courses_relations.xlsx')
for index, row in data.iterrows():
    key = row['Requerido']
    value = row['Por Ver']
    if (not pd.isna(value)):
        graph[courses_map[key]].append(courses_map[value])
        edge[courses_map[value]] += 1

k = int(input())
n = len(courses_map)

def dfs(v):
    if (visited[v]):
        return visited[v]
    visited[v] = 1
    for u in graph[v]:
        visited[v] += dfs(u)
    return visited[v]

for i in range (n):
    if (not edge[i + 1]):
        dfs(i + 1)
        heappush(priority_queue, [-1 * visited[i + 1], i + 1])

ans = 0
seen = [False for i in range(N)]

while (len(priority_queue)):
    ans += 1
    q = deque()
    count = 0
    
    while (seen[priority_queue[0][1]]):
        heappop(priority_queue)
        
    while (len(priority_queue) and count < k):
        count += 1
        first, second = heappop(priority_queue)
        seen[second] = True
        for i in graph[second]:
            q.append(i)
    while (len(q)):
        heappush(priority_queue, [-1 * visited[q[0]], q[0]])
        q.popleft()
print(ans)