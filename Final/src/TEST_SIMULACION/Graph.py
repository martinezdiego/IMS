from utils import load_courses, load_pensum, dfs, build_priority_queue, compute_min_semesters

def  pensum_graph(min_semesters):
	N = 100
	graph = [[] for i in range(N)]
	visited = [0 for i in range(N)]
	edge = [0 for i in range(N)]
	seen = [False for i in range(N)]

	courses_map = dict()

	load_courses(courses_map, './db/pensum_list_is_sc.xlsx') #'./test/raw_data/courses_list.xlsx')
	load_pensum(courses_map, graph, edge, './db/pensum_is_sc.xlsx') #'./test/raw_data/courses_relations.xlsx')
	priority_queue = build_priority_queue(graph, visited, edge, len(courses_map))
	ans = compute_min_semesters(priority_queue, graph, visited, seen, min_semesters)

	return (min(len(courses_map), ans))