from heapq import heappop, heappush, heapify 
from collections import deque 
import pandas as pd
import time
import csv

def build_courses_map(path):
    courses_map = dict()
    data = pd.read_excel(path)
    for index, row in data.iterrows():
        courses_map[row['Asignatura']] = int(index)
    return courses_map

def build_pensum(courses_map, path):
    N = len(courses_map)
    graph = [[] for i in range(N)]
    edge = [0 for i in range(N)]
    data = pd.read_excel(path)
    for _index, row in data.iterrows():
        key = row['Requerido']
        value = row['Para']
        if (not pd.isna(value)):
            graph[courses_map[key]].append(courses_map[value])
            edge[courses_map[value]] += 1
    return graph, edge

def dfs(v, graph, visited):
    if (visited[v]):
        return visited[v]
    visited[v] = 1
    for u in graph[v]:
        visited[v] += dfs(u, graph, visited)
    return visited[v]

def build_priority_queue(graph, edge, N):
    priority_queue = []
    heapify(priority_queue)
    visited = [0 for i in range(N)]
    for i in range (N):
        if (not edge[i]):
            dfs(i, graph, visited)
            heappush(priority_queue, [-1 * visited[i], i])
    return priority_queue, visited

def build_ans(priority_queue, graph, visited, max_courses, N):
    seen = [False for i in range(N)]
    ans = 0
    while (len(priority_queue)):
        ans += 1
        q = deque()
        count = 0
        while (len(priority_queue) and seen[priority_queue[0][1]]):
            heappop(priority_queue)
        while (len(priority_queue) and count < max_courses):
            count += 1
            _first, second = heappop(priority_queue)
            seen[second] = True
            for i in graph[second]:
                q.append(i)
        while (len(q)):
            heappush(priority_queue, [-1 * visited[q[0]], q[0]])
            q.popleft()
    return ans

def compute_min_semesters(max_courses):
	courses_map	= build_courses_map('./db/pensum_list_is_sc.xlsx')
	N = len(courses_map)
	graph, edges = build_pensum(courses_map, './db/pensum_is_sc.xlsx')
	priority_queue, visited = build_priority_queue(graph, edges, N)
	ans = build_ans(priority_queue, graph, visited, max_courses, N)

	return (min(ans, N))

def get_variables(data):
	num = len(data)
	Estudiantes=[]
	for _index, row in data.iterrows():
		Estudiantes.append(row['Nombre'])
	return num,Estudiantes

def output(ESTUDIANTE_NOMBRE,MAX_MATERIAS,S_min,T_ESPERA,T_LLEGADA_EST,T_ATENCION,T_SALIDA,TOT_ESTUDIANTE):
	Dictionary = {
		'ESTUDIANTE_NOMBRE':[],
		'MAX_MATERIAS':[],
		'S_min':[],
		'T_ESPERA':[],
		'T_LLEGADA_EST':[],
		'T_ATENCION':[],
		'T_SALIDA':[],
	}

	for i in range(0,TOT_ESTUDIANTE):
		T_LL_aux = float("{0:.2f}".format(T_LLEGADA_EST[i]))
		T_ES_aux = float("{0:.2f}".format(T_ESPERA[i]))
		T_AT_aux = float("{0:.2f}".format(T_ATENCION[i]))
		T_SA_aux = float("{0:.2f}".format(T_SALIDA[i]))
		Dictionary['ESTUDIANTE_NOMBRE'].append(ESTUDIANTE_NOMBRE[i])
		Dictionary['MAX_MATERIAS'].append(MAX_MATERIAS[i])
		Dictionary['S_min'].append(S_min[i])
		Dictionary['T_ESPERA'].append(T_ES_aux)
		Dictionary['T_LLEGADA_EST'].append(T_LL_aux)
		Dictionary['T_ATENCION'].append(T_AT_aux)
		Dictionary['T_SALIDA'].append(T_SA_aux)

	ordered = [
		'ESTUDIANTE_NOMBRE',
		'MAX_MATERIAS',
		'S_min',
		'T_LLEGADA_EST',
		'T_ESPERA',
		'T_ATENCION',
		'T_SALIDA',
	]

	output_dataframe = pd.DataFrame(Dictionary)
	output_dataframe[ordered].to_csv('./Report.csv', index=0)