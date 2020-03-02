from heapq import heappop, heappush, heapify 
from collections import deque 
import pandas as pd

def load_courses(courses_map, path):
    data = pd.read_excel(path)
    for index, row in data.iterrows():
        courses_map[row['Asignatura']] = int(index)

def load_pensum(courses_map, graph, edge, path):
    data = pd.read_excel(path)
    for index, row in data.iterrows():
        key = row['Requerido']
        value = row['Para']
        if (not pd.isna(value)):
            graph[courses_map[key]].append(courses_map[value])
            edge[courses_map[value]] += 1

def dfs(v, graph, visited):
    if (visited[v]):
        return visited[v]
    visited[v] = 1
    for u in graph[v]:
        visited[v] += dfs(u, graph, visited)
    return visited[v]

def build_priority_queue(graph, visited, edge, courses_size):
    priority_queue = []
    heapify(priority_queue)
    for i in range (courses_size):
        if (not edge[i]):
            dfs(i, graph, visited)
            heappush(priority_queue, [-1 * visited[i], i])
    return priority_queue

def compute_min_semesters(priority_queue, graph, visited, seen, min_semesters):
    ans = 0
    while (len(priority_queue)):
        ans += 1
        q = deque()
        count = 0
        while (len(priority_queue) and seen[priority_queue[0][1]]):
            heappop(priority_queue)
        while (len(priority_queue) and count < min_semesters):
            count += 1
            first, second = heappop(priority_queue)
            seen[second] = True
            for i in graph[second]:
                q.append(i)
        while (len(q)):
            heappush(priority_queue, [-1 * visited[q[0]], q[0]])
            q.popleft()
    return ans
    